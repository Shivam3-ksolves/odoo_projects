
{
    'name': "NewsApp",
    'version': '1.0',
    'depends': ['base'],  # Dependencies

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'category': 'Uncategorized',
    'data': [
        'security/ir.model.access.csv',
        'views/news_views.xml',
    ],
    'installable':True,
    'application': True
}
