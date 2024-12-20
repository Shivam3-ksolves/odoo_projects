{
    'name': 'Device Management',
    'version': '1.0',
    'author': 'Your Name',
    'category': 'Inventory',
    'summary': 'Manage devices, attributes, and assignments',
    'depends': ['base', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/actions.xml',
        'views/device_views.xml',
        'views/device_attribute_assignment_views.xml',
        'views/device_assignment_views.xml',
        'views/device_attribute_views.xml',
        'views/device_brand_views.xml',
        'views/device_model_views.xml',
        'views/device_type_views.xml',
        'views/employee_inherit_views.xml',
        'views/device_sequence.xml',
        'views/menus.xml',

    ],
    'installable': True,
    'application': True,
}
