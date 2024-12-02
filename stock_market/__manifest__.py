{
    'name': 'Stock Market',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Stock Market Module to manage stocks and trades',
    'author': 'Your Name',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/stock_market_views.xml',
        'data/stock_market_data.xml',
    ],
    'installable': True,
    'application': True,
}
