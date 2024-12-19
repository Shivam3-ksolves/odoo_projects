from odoo import models, fields

class SalesTaskModel(models.Model):
    _name = 'sales_task.sales_task_model'
    _description = 'Sales Task Model'

    name = fields.Char(string="Task Name", required=True)
    count = fields.Integer(string="Count", default=0)

    def action_client_component(self):
        """Trigger a success popup."""
        return {
            'type': 'ir.actions.client',
            'tag': 'sales_task.client_action_component',
            'params': {'message': 'Task updated successfully!'},
        }
