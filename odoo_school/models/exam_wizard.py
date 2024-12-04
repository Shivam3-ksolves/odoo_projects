from odoo import fields,models


class CreateExamWizard(models.TransientModel):
    _name = 'create.exam.wizard'
    _description = 'Wizard to Create Exams'

    exam_name = fields.Char(string='Exam Name', required=True)
    date =fields.Date(string='Exam Date',required=True)
    student_id=fields.Many2one('odoo.student',string='Student',required=True)
    class_id=fields.Many2one('odoo.class',string='Class',required=True)

    def create_exams(self):
        students=self.env['odoo.student'].search([])
        subjects=self.env['odoo.subject'].search([])
        exam_obj=self.env['odoo.exams']

        for student in students:
            for subject in subjects:
                exam_obj.create({
                    'name':self.exam_name,
                    'student_id':student.id,
                    'subject_id':subject.id,
                    'date':self.date,
                    'total_marks':100,
                    'class_id':self.class_id.id
                })

        return {'type': 'ir.actions.client', 'tag': 'reload'}
