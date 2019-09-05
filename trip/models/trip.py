from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Trip(models.Model):
    _name = 'trip'
    _description = 'Trip'

    name = fields.Char()
    description = fields.Char()
    day_count = fields.Integer()
    date = fields.Date(string="Trip Date")
    entity_id = fields.Many2many("res.partner", "trip_partner_rel", "trip_id", "partner_id")
    price = fields.Float()
    expiry_days = fields.Integer('Expiry Days', readonly=True,
                                 compute='_compute_expiry_days')
    expiry_status = fields.Selection([
        ('expired', "Expired"),
        ('available', "Available")],
        readonly=True, compute='_compute_expiry_days', store=True)
    is_trip_body = fields.Boolean(string='It is an entity', default='True',
                                  help='Check this box if the contact is a trip entity')

    quota = fields.Integer()



    @api.constrains('expiry_status')
    def _check_status(self):
            if self.expiry_status == "expired":
                raise ValidationError('This trip date has expired!!')

    @api.depends('date')
    def _compute_expiry_days(self):
        if self.date:
            self.expiry_days = (self.date - fields.Date.today()).days
            if self.expiry_days > 1:
                self.expiry_status = 'available'
            else:
                self.expiry_status = 'expired'


