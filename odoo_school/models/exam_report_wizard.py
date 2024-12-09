from odoo import models, fields, api

class ExamReportWizard(models.TransientModel):
    _name = 'exam.report.wizard'
    _description = 'Exam Report Wizard'

    student_id = fields.Many2one('odoo.student', string='Student', required=True)

    def generate_report(self):
        # Fetching data and triggering the report
        return self.env.ref('odoo_school.exam_report_pdf').report_action(self)
