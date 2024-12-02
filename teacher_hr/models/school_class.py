from odoo import models,fields


class SchoolClass(models.Model):
    _inherit='odoo.class'

    teacher_id=fields.Many2one('hr.employee',string='Teacher')
