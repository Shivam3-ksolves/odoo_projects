from odoo import models, fields

class DeviceBrand(models.Model):
    _name = 'device.brand'
    _description = 'Device Brand'

    name = fields.Char(string="Brand Name", required=True)
    device_model_ids = fields.One2many(
        'device.model',
        'device_brand_id',
        string="Device Models"
    )

    _sql_constraints = [
        ('unique_brand_name',
         'unique(name)',
         'The brand name must be unique.')
    ]
