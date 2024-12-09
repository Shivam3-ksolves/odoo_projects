from odoo import models, fields

class DeviceBrand(models.Model):
    _name = 'device.brand'
    _description = 'Device Brand'

    name = fields.Char(required=True, unique=True)
    device_model_ids = fields.One2many('device.model', 'device_brand_id', string="Device Models")
