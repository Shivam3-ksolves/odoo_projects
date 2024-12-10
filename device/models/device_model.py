from odoo import models, fields

class DeviceModel(models.Model):
    _name = 'device.model'
    _description = 'Device Model'

    name = fields.Char(string="Model Name", required=True)
    device_type_id = fields.Many2one(
        'device.type',
        string="Device Type",
        required=True
    )
    device_brand_id = fields.Many2one(
        'device.brand',
        string="Device Brand",
        required=True
    )
    device_attribute_value_ids = fields.One2many(
        'device.attribute.value',
        'device_model_id',
        string="Attribute Values"
    )

    _sql_constraints = [
        ('unique_model_name',
         'unique(name)',
         'The model name must be unique.')
    ]
