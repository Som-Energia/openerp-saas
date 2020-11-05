import pytest
from code import *

def test_func_fast():
    pass

def test_getValsInvoice_ok():
    im = InvoiceMaker()

    vals = im.getValsInvoice('B83677229')

    assert vals == {'account_id': 492,
        'address_contact_id': 10,
        'address_invoice_id': 12,
        'date_invoice': '2020-11-05',
        'fiscal_position': False,
        'journal_id': 13,
        'partner_bank': False,
        'partner_id': 3,
        'payment_term': False,
        'payment_type': 3,
        'type': 'out_invoice'}
