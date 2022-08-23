{
    'name': 'Unique Password',
    'version': '15.0.1.0.0',
    'category': 'Extra Tools',
    'summary': """Checking the uniqueness of the user's password""",
    'license': 'LGPL-3',
    'author': 'Anton Zaporozhets',
    'depends': [
        'base',
        'school_lesson_6_5',
    ],
    'data': [
        'security/ir.model.access.csv',
    ],
    'price': 10.0,
    'currency': 'EUR',
    'live_test_url': 'https://demo.odoo.com/odoo-school',
    'support': 'ant.zaporozhets@gmail.com',
    'images': ['static/description/banner.png', 'static/description/icon.png'],
    'application': False,
    'installable': True,
    'auto_install': False,
}
