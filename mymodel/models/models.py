from odoo import models, fields

class MyModel(models.Model):
    _name = 'my.model'
    _description = 'My Model for Multiple Views'
    _rec_name = 'description'

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
    start_date = fields.Datetime(string="Start Date")
    end_date = fields.Datetime(string="End Date")
    value = fields.Float(string="Value")
    status = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
    ], string="Status", default='draft')
