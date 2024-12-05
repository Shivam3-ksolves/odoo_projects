from odoo import models, api, _, fields
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    merged_status = fields.Selection([
        ('not_merged', 'Not Merged'),
        ('merged', 'Merged')
    ], string='Merge Status', default='not_merged')

    @api.model
    def action_merge_orders(self, order_ids):
        if len(order_ids) < 2:
            raise UserError(_("Please select at least two sale orders to merge."))

        orders = self.browse(order_ids)

        # Validate that all orders belong to the same customer
        customers = orders.mapped('partner_id')
        if len(customers) > 1:
            raise UserError(_("You can only merge orders for the same customer."))

        # Create a new sale order for the merged lines
        merged_order = self.create({
            'partner_id': orders[0].partner_id.id,  # Set the partner_id as the same for all orders
            'merged_status': 'merged',
            'origin': 'Merged Order',  # You can set any other fields you want
        })

        # Merge order lines into the new order
        for order in orders:
            for line in order.order_line:
                # Find matching lines in the new merged order (if any)
                matching_lines = merged_order.order_line.filtered(lambda l:
                    l.product_id == line.product_id and
                    l.price_unit == line.price_unit and
                    l.discount == line.discount and
                    l.product_uom == line.product_uom
                )

                # If multiple matching lines are found, iterate over them
                if matching_lines:
                    for matching_line in matching_lines:
                        matching_line.product_uom_qty += line.product_uom_qty
                else:
                    # If no matching line, create a new order line in the merged order
                    line.copy({'order_id': merged_order.id})

            # Optionally, set the merged status for the original orders
            order.merged_status = 'merged'

            # Cancel orders that are in "sent" or "sale" state
            if order.state in ['sale', 'sent']:
                order.action_cancel()

            # Optionally, create an activity/note for the merged orders
            order.message_post(body=_("This order has been merged into another order."))

        # Confirm the merged order to make it visible in the frontend
        merged_order.action_confirm()

        return {
            'type': 'ir.actions.client',
            'tag': 'reload',  # Reload the current view
            'params': {
                'title': _('Success'),
                'message': _('Sale orders merged into a new order successfully.'),
                'type': 'success',
                'sticky': False,
            },
        }
