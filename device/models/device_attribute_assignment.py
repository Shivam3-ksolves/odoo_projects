from odoo import models, fields

class DeviceAttributeAssignment(models.Model):
    _name = 'device.attribute.assignment'
    _description = 'Device Attribute Assignment'

    device_id = fields.Many2one('device.device', string="Device", required=True, unique=True)
    device_attribute_id = fields.Many2one('device.attribute', string="Attribute", required=True)
    device_attribute_value_id = fields.Many2one('device.attribute.value', string="Attribute Value", required=True)
    _sql_constraints = [
        ('unique_device_attribute',
         'unique(device_id, device_attribute_id)',
         'A device cannot have duplicate assignments for the same attribute.')
    ]
