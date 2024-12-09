from odoo import models, fields

class DeviceType(models.Model):
    _name = 'device.type'
    _description = 'Device Type'

    name = fields.Char(required=True, unique=True)
    code = fields.Char(unique=True)
    sequence = fields.Char(string="Sequence", default=lambda self: self.env['ir.sequence'].next_by_code('device.type.sequence'))
    device_model_ids = fields.One2many('device.model', 'device_type_id', string="Device Models")
    device_attribute_ids = fields.One2many('device.attribute', 'device_type_id', string="Device Attributes")
