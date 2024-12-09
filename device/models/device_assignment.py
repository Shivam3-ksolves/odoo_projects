from odoo import models, fields

class DeviceAssignment(models.Model):
    _name = 'device.assignment'
    _description = 'Device Assignment'

    name = fields.Char(required=True, unique=True)
    device_id = fields.Many2one('device.device', string="Device", required=True)
    employee_id = fields.Many2one('hr.employee', string="Employee")
    date_start = fields.Date()
    date_expire = fields.Date()
    state = fields.Selection([
        ('new', 'New'),
        ('draft', 'Draft'),
        ('approved', 'Approved'),
        ('returned', 'Returned'),
        ('rejected', 'Rejected'),
    ], default='new')
