# -*- coding: utf-8 -*-

from odoo import models, fields


class TeacherHr(models.Model):
    _inherit = 'hr.employee'
    _description = 'HR Employee'

    is_teacher = fields.Boolean(string='Is Teacher',default=False)
    teacher_id=fields.Char(string='Teacher ID')
    class_ids = fields.One2many('odoo.class','teacher_id',string='Classes')
