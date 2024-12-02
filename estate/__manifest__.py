{
    'name': 'Estate',
    'version': '1.0',
    'summary': 'Estate Management Module for Odoo 17',
    'category': 'Real Estate',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',  # This must come after models are loaded.
        'views/estate_property_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
