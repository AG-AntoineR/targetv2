# -*- coding: utf-8 -*-
# Copyright (C) 2021 - Auguria (<https://www.auguria.fr>).
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
{
    'name': 'Auguria remove power by odoo',
    'version': '1.0',
    'author': 'Auguria',
    'website': 'https://www.auguria.fr',
    'summary': "Auguria",
    'description': """remove power by odoo on footer of emails and on website""",
    'sequence': 0,
    'certificate': '',
    'license': 'LGPL-3',
    'depends': ['base','mail','website'],
    'data': [
        'views/mail_notification_edit_views.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}
