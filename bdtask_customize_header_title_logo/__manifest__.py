# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Custom Favicon and Title',
    'version': '16.0.0',
    'sequence': 1,
    'summary': """
        Custom Favicon and Title
    """,
    'description': "Choose your own Title to display on the browser header.",
    'author': 'bdtask',
    'maintainer': 'bdtask',
    'price': '0.0',
    'currency': 'USD',
    'website': 'https://www.bdtask.com/',
    'license': 'LGPL-3',
    'images': [
        'static/description/icon.png'
    ],
    'depends': [
        'web'
    ],
    'data': [
        'data/demo_data.xml',
        'views/favicon.xml',
    ],
    'assets': {
        'web.assets_backend_prod_only': [
            'bdtask_customize_header_title_logo/static/src/js/favicon.js',
        ],
    },
    'demo': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb': [
        
    ],
}
