# -*- coding: utf-8 -*-
{
    'name': 'Real Estate Invoicing',
    'version': '1.0.0',
    'category': 'Real Estate',
    'sequence': -999,
    'summary': 'A module for managing your real estate properties invoices',
    'description': "This is the odoo 16 tutorial module",
    'depends': [
        'base',
        'mail',
        'account',
        'real-estate',
    ],
    'data': [
        'security/ir.model.access.csv',
    ],
    'demo': [],
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}