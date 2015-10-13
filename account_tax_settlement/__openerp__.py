# -*- coding: utf-8 -*-
{
    'name': 'Tax Settlement',
    'version': '9.0.1.0.0',
    'category': 'Accounting',
    'sequence': 14,
    'summary': '',
    'description': """
Tax Settlement
==============
Add a model to manage tax settlements
    """,
    'author':  'ADHOC SA',
    'website': 'www.adhoc.com.ar',
    'images': [
    ],
    'depends': [
        'account_move_voucher',
    ],
    'data': [
        'views/account_move_line_view.xml',
        'views/account_journal_view.xml',
        'views/account_tax_settlement_detail_view.xml',
        'views/account_tax_settlement_view.xml',
        'views/account_voucher_view.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [
    ],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
