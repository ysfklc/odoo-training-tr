from odoo import models, fields, api

class Identification(models.Model):

    _name = 'identification'
    _description = 'IdentityOfPartner'

    name = fields.Char()
    id_num = fields.Char()
    type = fields.Selection([
        ('passport', "Passport"),
        ('id card', "Id Card"),
        ('driving licence',"Driving Licence")
    ],store=True)

