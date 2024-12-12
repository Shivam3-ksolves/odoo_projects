{
    'name': 'Course Management',
    'version': '1.0',
    'summary': 'Manage Students, Courses, and Enrollments',
    'author': 'Your Name',
    'depends': ['base', 'sale','product','web'],
    'data': [
        'security/ir.model.access.csv',
        'security/security_rules.xml',
        'views/student_views.xml',
        'views/course_views.xml',
        # 'views/custom_sale_order_views.xml',
        # 'static/src/js/list_view_extension.xml',
        'data/ir_access_data.xml',
    ],
    "assets": {
        "web.assets_backend": [
            # "course_management/static/src/js/list_view_extension.js",
        ],
},

'installable': True,
    'application': True,
}
