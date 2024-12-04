from odoo import fields,models,api
from datetime import datetime, timedelta
from io import BytesIO
import base64
import xlsxwriter

class EmployeeLoan(models.Model):
    _name='employee.loan'
    _description='Employee Loan'
    _inherit = ['mail.thread']

    name=fields.Many2one('hr.employee',string='Employee Name',required=True)
    loan_amount=fields.Float(string='Loan Amount', required=True)
    emi_count = fields.Integer(string='Total EMIs', required=True)
    emi_amount = fields.Float(string='EMI Amount', compute='_compute_emi_amount', store=True, readonly=True)
    date = fields.Date(string='Loan Date', default=fields.Date.today)
    emi_lines =fields.One2many('employee.loan.line','loan_id',string='EMI Schedule')
    employee_image = fields.Binary(related='name.image_1920', string="", readonly=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
    ], string='Status', default='draft', tracking=True)

    def action_confirm(self):
        self.generate_emi_list()
        self.state = 'confirm'

    def action_edit(self):
        self.write({'state': 'draft'})


    @api.depends('loan_amount', 'emi_count')
    def _compute_emi_amount(self):
        for record in self:
            if record.loan_amount and record.emi_count:
                record.emi_amount = record.loan_amount / record.emi_count
            else:
                record.emi_amount = 0.0


    def generate_emi_list(self):

        if not self.loan_amount or not self.emi_count:
            raise ValueError("Loan Amount and Total EMIs must be provided.")

        self.emi_lines.unlink()

        emi_date = fields.Date.from_string(self.date)
        for i in range(1, self.emi_count + 1):
            self.env['employee.loan.line'].create({
                'loan_id': self.id,
                'serial_number': i,
                'emi_amount': self.emi_amount,
                'emi_date': emi_date,
            })
            emi_date += timedelta(days=30)

        self.message_post(
            body="The EMI list has been generated successfully.",
            subject="EMI List Generated",
            message_type="notification",
            subtype_id=self.env.ref('mail.mt_comment').id
        )

    def send_email_to_employee(self):
        # Retrieve the employee's email address
        employee_email = self.name.work_email
        if not employee_email:
            raise ValueError("Employee does not have an email address.")

        # Create the Excel file for the EMI lines
        output = BytesIO()
        workbook = xlsxwriter.Workbook(output)
        worksheet = workbook.add_worksheet('EMI Schedule')

        # Write headers in the Excel file
        worksheet.write(0, 0, 'Serial Number')
        worksheet.write(0, 1, 'EMI Amount')
        worksheet.write(0, 2, 'EMI Date')

        # Write EMI lines to the Excel file
        row = 1
        for emi_line in self.emi_lines:
            worksheet.write(row, 0, emi_line.serial_number)
            worksheet.write(row, 1, emi_line.emi_amount)
            worksheet.write(row, 2, emi_line.emi_date.strftime('%Y-%m-%d'))  # Format date
            row += 1

        # Close the workbook to save the Excel file
        workbook.close()
        output.seek(0)

        # Create an attachment for the Excel file
        attachment = self.env['ir.attachment'].create({
            'name': f'EMI_Schedule_{self.name.name}.xlsx',
            'type': 'binary',
            'datas': base64.b64encode(output.read()),  # Base64 encode the content
            'mimetype': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            'res_model': 'employee.loan',
            'res_id': self.id,
        })

        # Prepare the email content
        subject = "Loan Information and EMI Schedule"
        body = f"""
        <p>Dear {self.name.name},</p>
        <p>Please find attached the EMI schedule for your loan.</p>
        <p><b>Loan Amount:</b> {self.loan_amount}</p>
        <p><b>EMI Count:</b> {self.emi_count}</p>
        <p>Best Regards,<br>Your Company</p>
        """

        # Create the email with attachment
        mail_values = {
            'subject': subject,
            'body_html': body,
            'email_to': employee_email,
            'attachment_ids': [(4, attachment.id)],
        }
        mail = self.env['mail.mail'].create(mail_values)
        mail.send()

        # Post the attachment in the chatter
        self.message_post(
            body="The EMI schedule Excel file has been sent to the employee.",
            subject="EMI Schedule Sent",
            message_type="notification",
            attachment_ids=[attachment.id],
            subtype_id=self.env.ref('mail.mt_comment').id
        )


class EmployeeLoanLine(models.Model):
    _name='employee.loan.line'
    _description='Loan Line'

    loan_id = fields.Many2one('employee.loan', string='Loan Reference', required=True, ondelete='cascade')
    serial_number = fields.Integer(string='Serial Number', required=True)
    emi_amount = fields.Float(string='EMI Amount', required=True)
    emi_date = fields.Date(string='EMI Date', required=True)
