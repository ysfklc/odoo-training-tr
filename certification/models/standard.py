from odoo import models, fields


class Standard(models.Model):
    _name = 'standard'
    _description = 'Standard'

    name = fields.Char()
    description = fields.Text(string='Validation Details')
