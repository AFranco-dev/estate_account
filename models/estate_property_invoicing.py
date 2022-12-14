# -*- coding: utf-8 -*-
from odoo import api, fields, models

class EstatePropertyInvoicing(models.Model):
    _name = 'estate.property.invoicing'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Estate Property Invoicing'