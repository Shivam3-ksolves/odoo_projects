# -*- coding: utf-8 -*-
from odoo import models, fields, api

class CustomSaleOrderLineWizard(models.TransientModel):
    _name = 'custom.sale.order.line.wizard'
    _description = 'Wizard for Custom Sale Order Lines'

    sale_order_id = fields.Many2one('sale.order', string="Sale Order", required=True)
    order_line_ids = fields.One2many('custom.sale.order.line.temp', 'wizard_id', string="Order Lines")

    @api.onchange('sale_order_id')
    def _onchange_sale_order_id(self):
        if self.sale_order_id:
            lines = []
            for line in self.sale_order_id.custom_sale_order_lines:
                lines.append({
                    'product_id': line.product_id.id,
                    'name': line.name,
                    'quantity': line.quantity,
                    'price_unit': line.price_unit,
                    'discount': line.discount,
                })

            self.update({'order_line_ids': [(5, 0, 0)] + [(0, 0, vals) for vals in lines]})

    def action_save(self):

        existing_lines = self.env['custom.sale.order.line'].search([
            ('sale_order_id', '=', self.sale_order_id.id),
        ])

        for line in self.order_line_ids:

            existing_line = existing_lines.filtered(lambda l: l.product_id == line.product_id)

            if existing_line:

                existing_line.write({
                    'name': line.name,
                    'quantity': line.quantity,
                    'price_unit': line.price_unit,
                    'discount': line.discount,
                })

                existing_lines -= existing_line
            else:

                self.env['custom.sale.order.line'].create({
                    'sale_order_id': self.sale_order_id.id,
                    'product_id': line.product_id.id,
                    'name': line.name,
                    'quantity': line.quantity,
                    'price_unit': line.price_unit,
                    'discount': line.discount,
                })

        existing_lines.unlink()

        return {'type': 'ir.actions.act_window_close'}


class CustomSaleOrderLineTemp(models.TransientModel):
    _name = 'custom.sale.order.line.temp'
    _description = 'Temporary Custom Sale Order Lines'

    wizard_id = fields.Many2one('custom.sale.order.line.wizard', string="Wizard")
    product_id = fields.Many2one('product.product', string="Product", required=True)
    name = fields.Char(string="Description")
    quantity = fields.Float(string="Quantity", default=1.0)
    price_unit = fields.Float(string="Unit Price")
    discount = fields.Float(string="Discount (%)")


