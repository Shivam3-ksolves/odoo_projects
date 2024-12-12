# -*- coding: utf-8 -*-
from odoo import models, fields, api


class CustomSaleOrder(models.Model):
    _name = 'custom.sale.order'
    _description = 'Custom Sale Order'

    product_id = fields.Many2one('product.product', string="Product", required=True)
    name = fields.Char(string="Description", required=True)
    quantity = fields.Float(string="Quantity", required=True, default=1.0)
    price_unit = fields.Float(string="Unit Price", required=True)
    subtotal = fields.Float(string="Subtotal", compute="_compute_subtotal", store=True)
    tax_id = fields.Many2many('account.tax', string="Taxes")
    discount = fields.Float(string="Discount (%)", default=0.0)
    sale_order_line_id = fields.Many2one('sale.order', string="Sale Order Line")

    @api.depends('quantity', 'price_unit', 'discount')
    def _compute_subtotal(self):
        for record in self:
            price = record.price_unit * record.quantity
            discount_amount = price * (record.discount / 100.0)
            record.subtotal = price - discount_amount
