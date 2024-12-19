from odoo import api, fields, models

class MobileSaleOrderLine(models.Model):
    _name = 'mobile.sale.order.line'
    _description = 'Mobile Sale Order Line'

    order_id = fields.Many2one('mobile.sale.order', string="Order", required=True, ondelete='cascade')
    product_id = fields.Many2one('product.product', string="Product", required=True)
    quantity = fields.Integer(string="Quantity", default=1)
    price_unit = fields.Float(string="Unit Price", default=0.0)
    tax_id = fields.Many2one('account.tax', string="Tax")
    tax_amount = fields.Float(string="Tax Amount", compute='_compute_tax_amount', readonly=True, store=True)
    subtotal = fields.Float(string="Subtotal", compute='_compute_subtotal', readonly=True, store=True)
    currency_id = fields.Many2one(
        related='order_id.currency_id',
        string="Currency",
        store=True,
        readonly=True
    )
    @api.depends('quantity', 'price_unit', 'tax_id')
    def _compute_tax_amount(self):
        for line in self:
            if line.tax_id:
                taxes = line.tax_id.compute_all(line.price_unit * line.quantity, currency=None)
                line.tax_amount = taxes['total_included'] - taxes['total_excluded']
            else:
                line.tax_amount = 0.0

    @api.depends('quantity', 'price_unit', 'tax_amount')
    def _compute_subtotal(self):
        for line in self:
            line.subtotal = (line.quantity * line.price_unit)
