from odoo import models, fields

class DeviceAttribute(models.Model):
    _name = 'device.attribute'
    _description = 'Device Attribute'

    name = fields.Char(required=True, unique=True)
    device_type_id = fields.Many2one('device.type', string="Device Type")
