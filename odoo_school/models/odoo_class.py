from odoo import models,fields


class Class(models.Model):
    _name='odoo.class'
    _description='Odoo Class'

    name=fields.Char(string='Class Name',required=True)
    student_ids= fields.One2many('odoo.student','class_id',string='Student')
