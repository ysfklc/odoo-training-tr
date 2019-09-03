from odoo import models,fields


class certificationStandard(models.Model):
    _name = 'certification.standard'
    _description = 'Certification Types'
    
    name = fields.Char()
    description = fields.Text()