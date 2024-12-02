from odoo import models, fields, api

class QuotationOrderLinesWizard(models.TransientModel):
    _name = 'quotation.order.lines.wizard'
    _description = 'Wizard for Quotation Order Lines'

    quotation_id = fields.Many2one('sale.order', string="Quotation", required=True)
    order_line_ids = fields.One2many('quotation.order.lines.temp', 'wizard_id', string="Order Lines")

    @api.onchange('quotation_id')
    def _onchange_quotation_id(self):
        """
        Fetch order lines from the selected quotation and populate the wizard.
        """
        # view_id = self.env.ref('your_module.view_quotation_order_lines_wizard_form').id

        if self.quotation_id:
            lines = []
            for line in self.quotation_id.order_line:
                self.write({
                    "order_line_ids": [(0, 0, {
                        'product_id': line.product_id.id,
                        'sale_order_line_id': line.id,  # Ensure this is being set correctly
                        'name': line.name,
                        'quantity': line.product_uom_qty,
                        'price_unit': line.price_unit,
                        'subtotal': line.price_subtotal,
                        'tax_id': [(6, 0, line.tax_id.ids)],
                        'discount': line.discount,
                    })]
                })



    def action_confirm(self):
        """
        Confirm and save the changes made in the wizard back to the sale order.
        """
        for line in self.quotation_id.order_line:
            # Update the corresponding sale order lines
            order_line = self.env['sale.order.line'].browse(line.id)
            order_line.write({
                'product_id': self.order_line_ids.product_id.id,
                'name': self.order_line_ids.name,
                'product_uom_qty': self.order_line_ids.quantity,
                'price_unit': self.order_line_ids.price_unit,
                'tax_id': [(6, 0, self.order_line_ids.tax_id.ids)],
                'discount': self.order_line_ids.discount,
            })

        return {'type': 'ir.actions.act_window_close'}


class QuotationOrderLinesTemp(models.TransientModel):
    _name = 'quotation.order.lines.temp'
    _description = 'Temporary Quotation Order Lines'

    wizard_id = fields.Many2one('quotation.order.lines.wizard', string="Wizard")
    product_id = fields.Many2one('product.product', string="Product")
    name = fields.Char(string="Description")
    quantity = fields.Float(string="Quantity")
    price_unit = fields.Float(string="Unit Price")
    subtotal = fields.Float(string="Subtotal", compute="_compute_subtotal", store=True)
    tax_id = fields.Many2many('account.tax', string="Taxes")
    discount = fields.Float(string="Discount (%)")
    sale_order_line_id = fields.Many2one('sale.order.line')

    @api.depends('quantity', 'price_unit')
    def _compute_subtotal(self):
        for line in self:
            line.subtotal = line.quantity * line.price_unit

