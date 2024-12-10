from odoo import fields,models,api
from datetime import datetime, timedelta

class EMIWizard(models.Model):
    _name = 'emi.wizard'
    _description = 'EMI Filter Wizard'

    month = fields.Selection(
        [(str(i), datetime(2000, i, 1).strftime('%B')) for i in range(1, 13)],
        string='Month',
        required=True
    )
    loan_line_ids = fields.One2many(
        comodel_name='employee.loan.line',
        inverse_name='emi_wizard_id',
        string="Loan Lines",
    )

    @api.onchange('month')
    def _onchange_month(self):
        """This method is triggered when the month field changes."""
        if not self.month:
            return

        # Get the selected month
        selected_month = int(self.month)
        current_year = datetime.today().year

        start_date = datetime(current_year, selected_month, 1)

        # Check if the selected month is December (12), then set the next month to January of the next year
        if selected_month == 12:
            end_date = datetime(current_year + 1, 1, 1)  # January of next year
        else:
            end_date = datetime(current_year, selected_month + 1, 1)

        # Get the unpaid EMI lines for the selected month
        emi_lines = self.env['employee.loan.line'].search([
            ('emi_date', '>=', start_date),
            ('emi_date', '<', end_date),
            ('paid', '=', False)
        ])

        # If unpaid EMI lines exist, return the action to show them, otherwise show an empty list
        # If unpaid EMI lines exist, return the action to show them, otherwise show an empty list
        if emi_lines:
            # Use [(6, 0, ids)] to link the loan lines to the wizard's One2many field
            self.loan_line_ids = [(6, 0, emi_lines.ids)]
        else:
            self.loan_line_ids = [(5, 0, 0)]  # Clear the lines if no unpaid EMI lines

    def write(self, vals):
        """
        Override write to ensure that changes to loan_line_ids are saved to the
        employee.loan.line model.
        """
        res = super(EMIWizard, self).write(vals)

        # Ensure changes are written to employee.loan.line model for 'paid' field
        if 'loan_line_ids' in vals:
            for line in self.loan_line_ids:
                if line.paid:
                    line.write({'paid': line.paid})  # Explicitly save changes to employee.loan.line

        return res


    def action_show_emis(self):
        # Get the selected month
        selected_month = int(self.month)
        current_year = datetime.today().year

        start_date = datetime(current_year, selected_month, 1)

        # Check if the selected month is December (12), then set the next month to January of the next year
        if selected_month == 12:
            end_date = datetime(current_year + 1, 1, 1)  # January of next year
        else:
            end_date = datetime(current_year, selected_month + 1, 1)

        # Debugging: Print date range
        print(f"Filtering EMI Lines between {start_date} and {end_date}")

        # Get the unpaid EMI lines for the selected month
        emi_lines = self.env['employee.loan.line'].search([
            ('emi_date', '>=', start_date),
            ('emi_date', '<', end_date),
            ('paid', '=', False)
        ])

        # Debugging: Print how many records found
        print(f"Found {len(emi_lines)} unpaid EMI lines.")

        # If unpaid EMI lines exist, return the action to show them, otherwise show an empty list
        if emi_lines:
            return {
                'name': 'Unpaid EMI Lines',
                'type': 'ir.actions.act_window',
                'res_model': 'employee.loan.line',
                'view_mode': 'tree',
                'view_id': self.env.ref('teacher_hr.view_employee_loan_line_tree').id,  # Ensure this points to the correct tree view
                'domain': [('id', 'in', emi_lines.ids)],
                'target': 'current',
            }
        else:
            return {
                'name': 'No Unpaid EMIs',
                'type': 'ir.actions.act_window',
                'res_model': 'employee.loan.line',
                'view_mode': 'tree',
                'domain': [],
                'target': 'current',
            }

