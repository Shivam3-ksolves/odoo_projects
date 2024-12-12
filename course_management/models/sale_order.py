# -*- coding: utf-8 -*-

from odoo import models,fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'


    custom_sale_order_ids = fields.One2many(
        'custom.sale.order', 'sale_order_line_id', string="Custom Sale Orders"
    )
    def action_open_quotation_wizard(self):

        return {
            'type': 'ir.actions.act_window',
            'name': 'Sale Order Lines Wizard',
            'res_model': 'quotation.order.lines.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_quotation_id': self.id,
            },
        }
