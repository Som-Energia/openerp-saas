#!/usr/bin/env python
# -*- coding: utf-8 -*-
from erppeek import Client
import configdb
from datetime import datetime, date


class InvoiceMaker:
    def __init__(self):
        self.O = Client(**configdb.erppeek)

    def getValsInvoice(self, dni):
        partner_id = self.O.ResPartner.search([('vat','=',"ES"+dni)])
        if not partner_id:
            print "La inscripció amb DNI ", dni, " no existeix al ERP, no s'ha fet factura"
            return None

        date_invoice = str(date.today())
        account_id = self.O.AccountAccount.search([('code','=','430000')])
        journal_id = self.O.AccountJournal.search([('code','=','ENERGIA')])
        payment_type_id = self.O.PaymentType.search([('code','=','TRANSFERENCIA_CSB')])
        ai_obj = self.O.AccountInvoice

        vals = {}
        vals.update(ai_obj.onchange_partner_id([], 'out_invoice', partner_id[0]).get('value', {}))
        vals.update({
            'partner_id': partner_id[0],
            'type': 'out_invoice',
            'journal_id': journal_id[0],
            'account_id': account_id[0],
            'payment_type': payment_type_id[0],
            'date_invoice': date_invoice,
        })
        return vals

