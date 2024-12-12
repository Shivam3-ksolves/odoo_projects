from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    custom_sale_order_lines = fields.One2many(
        'custom.sale.order.line', 'sale_order_id', string="Custom Sale Order Lines"
    )

    def action_open_custom_sale_order_line_wizard(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Sale Order Lines Wizard',
            'res_model': 'custom.sale.order.line.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'active_id': self.id,
                'default_sale_order_id': self.id,
            },
        }
