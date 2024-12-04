from odoo import fields,models



class Student (models.Model):
    _name='odoo.student'
    _description='Odoo Student Model'

    name = fields.Char(string='Name')
    age = fields.Integer(string = 'Age')
    roll_number = fields.Integer(string='Roll Number')
    class_id= fields.Many2one('odoo.class',string='Class')
    fee_ids= fields.One2many('odoo.fee','student_id')
    subject_ids=fields.Many2many('odoo.subject',string='Subjects')
    exam_ids=fields.One2many('odoo.exams','student_id',string='Exams')