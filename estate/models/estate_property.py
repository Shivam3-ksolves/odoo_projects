from odoo import models, fields

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property"

    name = fields.Char(string="Property Name", required=True)
    description = fields.Text(string="Description")
    price = fields.Float(string="Price", required=True)
    bedrooms = fields.Integer(string="Bedrooms", required=True)
    living_area = fields.Float(string="Living Area (sqm)", required=True)
