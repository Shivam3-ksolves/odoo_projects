from odoo import models, fields

class Device(models.Model):
    _name = 'device.device'
    _description = 'Device'

    name = fields.Char(required=True, unique=True)
    shared = fields.Boolean(default=False)
    device_type_id = fields.Many2one('device.type', string="Device Type", required=True)
    device_brand_id = fields.Many2one('device.brand', string="Device Brand")
    device_model_id = fields.Many2one('device.model', string="Device Model")
    attributes = fields.One2many('device.attribute.assignment', 'device_id', string="Attributes")
    _sql_constraints = [
        ('unique_device_name', 'unique(name)', 'The device name must be unique!')
    ]
