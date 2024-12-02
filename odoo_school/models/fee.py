from odoo import fields,models


class Fee(models.Model):
    _name='odoo.fee'
    _description='Odoo Fee'

    name=fields.Char(string='Fee Description')
    amount=fields.Float(string='Amount')
    month=fields.Selection([(str(i), str(i)) for i in range(1, 13)], string='Month')
    student_id= fields.Many2one('odoo.student',string='Student')