from odoo import fields,models

class Subject(models.Model):
    _name='odoo.subject'
    _description='Odoo Subject'

    name=fields.Char(string ='Subject Name')
    student_ids=fields.Many2many('odoo.student',string='Students')