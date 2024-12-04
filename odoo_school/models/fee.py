import csv
import io
from odoo import models, fields, api
from odoo.http import request

class Fee(models.Model):
    _name = 'odoo.fee'
    _description = 'Odoo Fee'

    name = fields.Char(string='Fee Description')
    amount = fields.Float(string='Amount')
    month = fields.Selection([
        ('1', 'January'),
        ('2', 'February'),
        ('3', 'March'),
        ('4', 'April'),
        ('5', 'May'),
        ('6', 'June'),
        ('7', 'July'),
        ('8', 'August'),
        ('9', 'September'),
        ('10', 'October'),
        ('11', 'November'),
        ('12', 'December')
    ], string='Month')
    student_id = fields.Many2one('odoo.student', string='Student')

    def generate_csv(self):
        # Create a StringIO buffer to hold the CSV data
        csv_file = io.StringIO()

        # Create a CSV writer object
        writer = csv.writer(csv_file)

        # Write the header row
        writer.writerow(['Fee Description', 'Amount', 'Month', 'Student'])

        # Write data rows for each fee record
        for record in self:  # This will iterate over the recordset if multiple records are selected
            writer.writerow([record.name, record.amount, record.month, record.student_id.name])

        # Move the pointer to the beginning of the file to ensure it is read correctly
        csv_file.seek(0)

        # Return the file as a downloadable attachment
        response = request.make_response(csv_file.getvalue(),
                                        headers=[('Content-Type', 'text/csv'),
                                                 ('Content-Disposition', 'attachment; filename="fees.csv"')])

        return response
