# contact_qr_ocr/__manifest__.py
{
    'name': 'Common customizations',
    'version': '17.0.1.0.0',
    'summary': 'Common customizations for a NSOFT',
    'category': 'Productivity',
    'description': '',
    'author': 'Oleksii Panpukha',
    'license': 'Other proprietary',
    'website': 'https://github.com/3xecut0r',
    'depends': ['contacts', 'crm'],
    'data': [
        'views/res_partner.xml',
        'views/crm.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}
