from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    x_jewelry_name = fields.Char(string='Jewelry Name')
    x_date_of_birth = fields.Date(string='Date of Birth')
    x_personne_name = fields.Char(string='Personne Name')
    x_assistant = fields.Char(string='Assistant')
    x_mailing_city = fields.Char(string='Mailing City')
    x_email_secondary = fields.Char(string='Email Secondary')
    x_territories = fields.Char(string='Territories')
    x_code_app = fields.Char(string='Code App')
    x_email_social_login_app = fields.Char(string='Email Social Login App')
