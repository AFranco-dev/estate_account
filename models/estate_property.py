# -*- coding: utf-8 -*-
from odoo import api, fields, models, exceptions
from odoo.addons.account.models import account_move

class EstateProperty(models.Model):
    _inherit = 'estate.property'

    def property_sold(self):
        # defining invoice fields
        partner_id = self.buyer_id.id
        move_type = 'out_invoice'
        journal = self.env['account.move'].with_context(default_move_type='out_invoice')._get_default_journal()
        print(journal)
        print(self.env['account.move'].search([('model_type', '=', 'out_invoice')]))
        journal_id = self.env['account.move'].sudo().with_context(move_type='out_invoice').id

        # creating invoice dictionary
        invoice = {
            'partner_id': partner_id,
            'move_type': move_type,
            'journal_id': journal_id,
        }

        self.env['account.move'].sudo().with_context(default_move_type='out_invoice').create(invoice)


        return super().property_sold()