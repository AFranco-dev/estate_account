# -*- coding: utf-8 -*-
from odoo import api, fields, models, exceptions, Command
from odoo.addons.account.models import account_move

class EstateProperty(models.Model):
    _inherit = 'estate.property'

    def property_sold(self):
        # defining invoice fields
        partner_id = self.buyer_id.id
        move_type = 'out_invoice'
        #first invoice line values
        name_l1 = self.name
        quantity_l1 = 1
        price_unit_l1 = self.selling_price*0.06
        #second invoice line values
        name_l2 = "administrative fees"
        quantity_l2 = 1
        price_unit_l2 = 100.00
        #first invoice line dict
        line_1 = Command.create({
            'name': name_l1,
            'quantity': quantity_l1,
            'price_unit': price_unit_l1,
        })
        #second invoice line dict
        line_2 = Command.create({
            'name': name_l2,
            'quantity': quantity_l2,
            'price_unit': price_unit_l2,
        })
        # creating invoice dictionary
        invoice = {
            'partner_id': partner_id,
            'move_type': move_type,
            'invoice_line_ids': []
        }

        invoice['invoice_line_ids']+=line_1
        invoice['invoice_line_ids']+=line_2

        self.env['account.move'].sudo().with_context(default_move_type='out_invoice').create(invoice)


        return super().property_sold()