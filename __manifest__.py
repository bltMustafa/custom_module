{
    'name': 'Product Feedback',
    'category': 'Product Management',
    'summary': 'Product Feedback is ',
    'version': '18.0.1.0.0',
    'license': 'OPL-1',
    'author': 'mstk',
    'depends': [
        'product',
        'purchase',
        'hr_expense',
        'stock',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/new_prod_feedback.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
}
