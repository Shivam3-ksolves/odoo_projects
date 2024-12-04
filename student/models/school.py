from odoo import models, fields,api
from odoo.exceptions import ValidationError,UserError

class School(models.Model):
    _name = 'school.school'
    _description = 'School'

    name = fields.Char(string="School Name", required=True)
    student_ids = fields.One2many(
        'school.student',  # Related model
        'school_id',       # Related field in the child model
        string="Students"
    )


class Users(models.Model):
    _inherit = 'res.users'

    student_ids = fields.Many2many(
        'school.student',  # Related model
        string="Students",
        compute="_compute_student_ids"  # Computed field
    )


    def _compute_student_ids(self):
        """
        Compute the list of students related to the teacher (current user).
        """
        for user in self:
            # Fetch all students where this teacher is listed in `teacher_ids`
            user.student_ids = self.env['school.student'].search([
                ('teacher_ids', 'in', user.id)
            ])

class Student(models.Model):
    _name = 'school.student'
    _description = 'Student'

    name = fields.Char(string="Student Name", required=True)
    age = fields.Integer(string="Age")
    school_id = fields.Many2one(
        'school.school',  # Related model
        string="School",
        ondelete='cascade'  # Deletes related students if the school is deleted
    )
    teacher_ids = fields.Many2many(
        'school.teacher',  # Related model
        'student_teacher_rel',  # Name of the relation table
        'student_id',  # Column for this model in the relation table
        'teacher_id',  # Column for the other model in the relation table
        string="Teachers"
    )
    status = fields.Selection([
        ('active', 'Active'),
        ('graduated', 'Graduated'),
        ('inactive', 'Inactive')
    ], default='active', string="Status")

    graduation_date = fields.Date(string="Graduation Date")
    final_grades = fields.Char(string="Final Grades",)
    # _sql_constraints = ([
    #                        (
    #                            'check_final_grades',  # Constraint name
    #                            "CHECK(final_grades IN ('A', 'A+', 'B', 'B+', 'C', 'C+'))",  # SQL check expression
    #                            "Invalid Final Grade! Allowed grades are: A, A+, B, B+, C, C+."  # Error message
    #                        ),
    #                    ])

    @api.constrains('final_grades')
    def _check_final_grade(self):
        """
        Ensure that the `final_grade` contains only allowed values.
        """
        allowed_grades = ['A', 'A+', 'B', 'B+', 'C', 'C+', 'D', 'D+']
        for record in self:
            if record.final_grades and record.final_grades not in allowed_grades:
                raise ValidationError(
                    f"Invalid Final Grade: '{record.final_grades}'. "
                    f"Allowed grades are: {', '.join(allowed_grades)}."
                )

    @api.onchange('final_grades')
    def _onchange_final_grade(self):
        """Validate the final_grade when it is changed."""
        allowed_grades = {'A', 'A+', 'B', 'B+', 'C', 'C+'}
        if self.final_grades and self.final_grades not in allowed_grades:
            # Raise a user-friendly error
            raise UserError(
                "Invalid Final Grade! Allowed grades are: A, A+, B, B+, C, C+."
            )

    # Action button to mark student as graduated
    def action_graduate_student(self):
        for student in self:
            student.status = 'graduated'
            student.graduation_date = fields.Date.today()  # Set the graduation date to today's date
            student.final_grades = self._compute_final_grades()  # Compute the final grades for the student

    # Compute final grades (you can enhance this logic as per your requirement)
    def _compute_final_grades(self):
        # Example logic for final grades; modify it as per your requirement
        return "A"  # For simplicity, assume all graduated students get an "A"

    def generate_csv_report(self):
        return self.env.ref('student.action_student_report').report_action(self)


