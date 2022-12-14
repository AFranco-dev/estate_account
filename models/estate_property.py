# -*- coding: utf-8 -*-
from odoo import api, fields, models, exceptions

class EstateProperty(models.Model):
    _inherit = 'estate.property'

    def property_sold(self):
        for rec in self:
            # defining invoice fields
            partner_id = rec.buyer_id.id
            move_type = 'out_invoice'
            print(rec.env['account.move'].context)
            journal_id = self.env['account.move'].with_context(move_type='out_invoice')._search_default_journal().id

            # creating invoice dictionary
            invoice = {
                'partner_id': partner_id,
                'move_type': move_type,
                'journal_id': journal_id,
            }

            self.env['account.move'].sudo().with_context(default_move_type='out_invoice').create(invoice)


        return super().property_sold()