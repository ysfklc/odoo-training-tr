from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    trip_ids = fields.Many2many("trip", "trip_partner_rel", "partner_id", "trip_id")


    '''
    is_adult = fields.Boolean(string='It is an adult',default='True',help='Check this box if the contact is an adult ??')
    '''
