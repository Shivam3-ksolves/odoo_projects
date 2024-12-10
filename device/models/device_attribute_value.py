from odoo import models, fields

class DeviceAttributeValue(models.Model):
    _name = 'device.attribute.value'
    _description = 'Device Attribute Value'

    name = fields.Char(string="Name", required=True)
    device_attribute_id = fields.Many2one(
        'device.attribute',
        string="Device Attribute",
        required=True
    )
    device_model_id = fields.Many2one(
        'device.model',
        string="Device Model"
    )

    _sql_constraints = [
        ('unique_name_attribute',
         'unique(name, device_attribute_id)',
         'The same name cannot be used for multiple values under the same device attribute.')
    ]
