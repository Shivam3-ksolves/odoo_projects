from odoo import models, fields,api

class Department(models.Model):
    _name = 'school.department'
    _description = 'Department'

    name = fields.Char(string="Department Name", required=True)

class Teacher(models.Model):
    _name = 'school.teacher'
    _description = 'Teacher'

    name = fields.Char(string="Teacher Name", required=True)
    age = fields.Integer(string="Age")
    department_id = fields.Many2one(
        'school.department',  # Related model
        string="Department",
        ondelete='set null',  # Set to NULL if the department is deleted
    )
    student_ids = fields.Many2many(
        'school.student',  # Related model
        'student_teacher_rel',  # Name of the relation table
        'teacher_id',  # Column for this model in the relation table
        'student_id',  # Column for the other model in the relation table
        string="Students"
    )
    student_count = fields.Integer(
        string="Number of Students",
        compute='_compute_student_count',  # Compute function
        store=True  # Store the computed value in the database
    )

    @api.depends('student_ids')
    def _compute_student_count(self):
        for teacher in self:
            teacher.student_count = len(teacher.student_ids)  # Count the number of students
        self._compute_experience()

    # @api.depends('student_count')
    def _compute_experience(self):
       if self.student_count > 2 and not self.name.startswith('Prof.'):
            self.name='Prof. '+self.name


    # @api.onchange('student_ids')
    # def _onchange_student_ids(self):
    #     if self.student_count > 2 and not self.name.startswith('Prof.'):
    #         self.name = 'Prof. '+self.name  # Increase teacher's age by 1 if student count > 10

