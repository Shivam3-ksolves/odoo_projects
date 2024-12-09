from odoo import models, fields

class DeviceAttributeValue(models.Model):
    _name = 'device.attribute.value'
    _description = 'Device Attribute Value'

    name = fields.Char(required=True, unique=True)
    device_attribute_id = fields.Many2one('device.attribute', string="Device Attribute", required=True)
    device_model_id = fields.Many2one('device.model', string="Device Model")
