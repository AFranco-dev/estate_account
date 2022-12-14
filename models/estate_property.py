# -*- coding: utf-8 -*-
from odoo import api, fields, models, exceptions
from odoo.tools import date_utils
from odoo.tools import float_utils

class EstateProperty(models.Model):
    _inherit = ['mail.thread', 'mail.activity.mixin', 'estate.property']

    def property_sold(self):
        print("Overriden property sold. AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        return super().property_sold()