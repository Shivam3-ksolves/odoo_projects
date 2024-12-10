from odoo import models, fields, api

class DeviceAttribute(models.Model):
    _name = 'device.attribute'
    _description = 'Device Attribute'

    name = fields.Char(string="Name", required=True, unique=True)
    device_type_id = fields.Many2one(
        'device.type',
        string="Device Type",
        required=True
    )
    required = fields.Boolean(string="Required", default=False)
    device_attribute_value_ids = fields.One2many(
        'device.attribute.value',
        'device_attribute_id',
        string="Device Attribute Values"
    )
    _sql_constraints = [
        ('unique_device_attribute_name', 'unique(name)', 'The device attribute name must be unique!')
    ]
