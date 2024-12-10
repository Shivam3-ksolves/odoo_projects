from odoo import models, fields

class DeviceType(models.Model):
    _name = 'device.type'
    _description = 'Device Type'

    name = fields.Char(required=True, unique=True, string="Device Type Name")
    code = fields.Char(unique=True, string="Device Type Code")
    sequence = fields.Char(
        string="Sequence",
        default=lambda self: self.env['ir.sequence'].next_by_code('device.type.sequence'),
        readonly=True
    )
    device_model_ids = fields.One2many(
        'device.model',
        'device_type_id',
        string="Device Models"
    )
    device_attribute_ids = fields.One2many(
        'device.attribute',
        'device_type_id',
        string="Device Attributes"
    )

    _sql_constraints = [
        ('unique_name', 'unique(name)', 'Device Type name must be unique.'),
        ('unique_code', 'unique(code)', 'Device Type code must be unique.')
    ]
