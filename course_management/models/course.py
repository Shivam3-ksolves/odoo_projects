# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError

class Course(models.Model):
    _name = 'course.management'
    _description = 'Course Management'

    name = fields.Char(string="Course Name", required=True)
    code = fields.Char(string="Course Code", required=True)
    student_ids = fields.Many2many('student.management', string="Students")

    def action_open_quotation_wizard(self):
        """
        Opens the Quotation Order Lines Wizard.
        """
        view_id = self.env.ref('course_management.view_quotation_order_lines_wizard_form').id
        return {
            'type': 'ir.actions.act_window',
            'name': 'Quotation Order Lines Wizard',
            'res_model': 'quotation.order.lines.wizard',
            'view_mode': 'form',
            'view_id': view_id,  # Explicitly reference the wizard view ID
            'target': 'new',  # Open in a modal
            'context': {
                'default_quotation_id': self.env['sale.order'].search([], limit=1).id,  # Adjust as needed
            },
        }

    @api.model
    def create_course(self,vals):
        """
        Create a new course record with the name and code entered by the user.
        """
        # Ensure that name and code are provided by the user
        if not self.name or not self.code:
            raise UserError("Please provide a valid name and code for the course.")

        # Create the new course record
        vals = self.create({
            'name': self.name,
            'code': self.code,
        })

        # Optionally return an action to open the newly created course
        # return {
        #     'type': 'ir.actions.act_window',
        #     'res_model': 'course.management',
        #     'view_mode': 'form',
        #     'res_id': new_course.id,
        #     'target': 'current',
        # }

    def update_course_name(self):
        """
        Update the course name to a default value when triggered by the UI.
        """
        if not self:
            raise UserError("No course selected.")
        self.write({'name': self.name})
        return True

    def search_course(self):
        """
        Search for a specific course by a hardcoded code and return its form view.
        """
        course = self.search([('code', '=', "COURSE-001")], limit=1)
        if not course:
            raise UserError("No course found with the code 'COURSE-001'.")
        return {
            'name': 'Course Found',
            'type': 'ir.actions.act_window',
            'res_model': 'course.management',
            'view_mode': 'form',
            'res_id': course.id,
        }

    def delete_course(self):
        """
        Delete the current course record.
        """
        if not self:
            raise UserError("No course selected to delete.")
        self.unlink()
        return {'type': 'ir.actions.act_window_close'}

    def read_students(self):
        """
        Read and display the names and ages of all enrolled students.
        """
        if not self.student_ids:
            raise UserError("No students are enrolled in this course.")
        student_data = self.student_ids.read(['name', 'age'])
        message = '\n'.join([f"{student['name']} (Age: {student['age']})" for student in student_data])
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Enrolled Students',
                'message': message,
                'type': 'info',
                'sticky': False,
            },
        }
