# -*- coding: utf-8 -*-
{
    'name': "Student Management",
    'summary': "Manage student data and reports",
    'description': """
        This module allows you to manage student information, generate reports, and handle graduation processes.
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web'],

    # always loaded
    'data': [
        # Security files
        'security/user_groups.xml',
        'security/ir.model.access.csv',
        'security/record_rules.xml',

        # 'views/menu_views.xml',

        'views/school_views.xml',
        'views/department_views.xml',
        'views/menu_views.xml',
        'views/user_views.xml',
        'views/student_report_template.xml',
        'views/student_report_action.xml'

    ],
    'installable': True,
    'application': True,
    # only loaded in demonstration mode

}

