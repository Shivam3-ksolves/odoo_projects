from odoo import models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_open_quotation_wizard(self):
        """
        Opens the Quotation Order Lines Wizard.
        """
        return {
            'type': 'ir.actions.act_window',
            'name': 'Quotation Order Lines Wizard',
            'res_model': 'quotation.order.lines.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_quotation_id': self.id,
            },
        }
