from odoo import fields,models

class Exams(models.Model):
    _name='odoo.exams'
    _description='Odoo Exams'

    name=fields.Char(string='Exam Name')
    student_id=fields.Many2one('odoo.student', string='Student', required=True)
    subject_id=fields.Many2one('odoo.subject', string='Subject', required=True)
    class_id=fields.Many2one('odoo.class', string='Class', required=True)
    date=fields.Date(string='Exam Date')
    marks_obtained = fields.Float(string='Marks Obtained')
    total_marks = fields.Float(string='Total Marks', default=100.0)
