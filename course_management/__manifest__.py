{
    'name': 'Course Management',
    'version': '1.0',
    'summary': 'Manage Students, Courses, and Enrollments',
    'author': 'Your Name',
    'depends': ['base', 'sale','product'],
    'data': [
        'security/ir.model.access.csv',
        'security/security_rules.xml',
        'views/student_views.xml',
        'views/course_views.xml',
        'data/ir_access_data.xml',
        # 'views/qoutation_wizard.xml'
    ],
    'installable': True,
    'application': True,
}
