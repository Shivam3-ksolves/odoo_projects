from odoo import models, fields,api

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
    ], default='draft')
    _sql_constraints = [
        ('unique_device_assignment_name', 'unique(name)', 'The device assignment name must be unique!')
    ]
    @api.model
    def create(self, values):
        # Set default state to 'new' when a record is created
        if 'state' not in values:
            values['state'] = 'new'
        return super(DeviceAssignment, self).create(values)

    def write(self, values):
        # Change state to 'draft' when a record is edited or updated
        if 'state' not in values:
            values['state'] = 'draft'
        return super(DeviceAssignment, self).write(values)

    def action_set_new(self):
        self.write({'state': 'new'})

    def action_set_draft(self):
        self.write({'state': 'draft'})

    def action_set_approved(self):
        self.write({'state': 'approved'})

    def action_set_returned(self):
        self.write({'state': 'returned'})

    def action_set_rejected(self):
        self.write({'state': 'rejected'})

