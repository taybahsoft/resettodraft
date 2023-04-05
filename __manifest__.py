# -*- coding: utf-8 -*-
{
    'name': "resttodraft",
    'version': '16.0.0',
    'summary': """ Reset Entries To Draft and delete name """,
    'description': """
        Reset Entries To Draft and delete name (NUMBER) of entry to make it easy to delete 
    """,
    'author': "3rqooop",
    'company': 'Taybahsoft',
    'support': 'taybahsoft.co@gmail.com',
    'category': 'Accounting',
    'price': 50,
    'currency': 'USD',
    'depends': ['base', 'account'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'images': ['static/description/download.jpg'],
    'license': 'AGPL-3',
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}
