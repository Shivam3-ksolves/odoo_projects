from odoo import models, fields, api

# for line in self.quotation_id.order_line:
class Student(models.Model):
    _name = 'student.management'
    _description = 'Student Management'

    # Define the fields for the student model
    name = fields.Char(string="Student Name", required=True)  # Student's name
    age = fields.Integer(string="Age")  # Student's age
    course_ids = fields.Many2many('course.management', string="Enrolled Courses")  # Courses the student is enrolled in

    def enroll_in_course(self, course_id):
        """
        Enroll the student in a specific course.
        - Uses `write()` ORM method to update the Many2many field `course_ids`.
        - (4, course_id): Adds the course to the relationship without removing others.
        """
        course = self.env['course.management'].browse(course_id)  # Fetch the course record by ID
        if course:
            self.write({'course_ids': [(4, course.id)]})  # Add the course to the Many2many field
            return True
        return False

    def fetch_courses(self):
        """
        Fetch all courses a student is enrolled in.
        - Uses `read()` ORM method to retrieve specific fields from related course records.
        """
        return self.course_ids.read(['name', 'code'])  # Returns the name and code of all enrolled courses

    def remove_enrollment(self, course_id):
        """
        Remove the student from a specific course.
        - Uses `write()` ORM method with (3, course_id) to remove the course from the Many2many field.
        """
        self.write({'course_ids': [(3, course_id)]})  # Remove the specified course from the Many2many field

    def duplicate_student(self):
        """
        Duplicate the student record.
        - Uses the `copy()` ORM method to create a duplicate of the current record.
        """
        return self.copy()  # Creates a new student record with the same data as the current one
