# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': "IAP / Mail",
    'summary': """Bridge between IAP and mail""",
    'description': """Bridge between IAP and mail""",
    'category': 'Hidden/Tools',
    'depends': [
        'iap',
        'mail',
    ],
    'auto_install': True,
    'data': [
        'views/iap_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'iap_mail/static/src/js/**/*',
        ],
    },
    'author': 'Odoo S.A.',
    'license': 'LGPL-3',
}
