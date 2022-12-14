# -*- coding: utf-8 -*-
from odoo import api, fields, models, exceptions

class EstateProperty(models.Model):
    _inherit = 'estate.property'

    def _prepare_invoice_dict(self):
        journal = self.env['account.move'].with_context(default_move_type='out_invoice')._get_default_journal()
        self.ensure_one()
        invoice_vals = {
            'partner_id': self.buyer_id.id,
            'move_type': 'out_invoice',
            'journal_id': journal.id
        }
        return invoice_vals
    
    def _create_invoices(self, grouped=False, final=True, date=None):
        invoice_vals_list = []

        for order in self:
            invoice_vals = self._prepare_invoice_dict
            invoice_vals_list.append(invoice_vals)
        
        if not invoice_vals_list:
            raise exceptions.UserError("No invoices to issue.")

        moves = self.env['account.move'].sudo().with_context(default_move_type='out_invoice').create(invoice_vals_list)

        return moves

    def property_sold(self):
        self._create_invoices()
        return super().property_sold()