from odoo import models, fields


class CRM(models.Model):
    _inherit = 'crm.lead'

    x_annual_revenue = fields.Monetary(string='Annual Revenue', currency_field='x_currency_id')
    x_currency_id = fields.Many2one('res.currency', string='Currency')
    x_exchange_rate = fields.Float(string='Exchange Rate')
    x_forme = fields.Char(string='Forme')
    x_poids = fields.Float(string='Poids')
    x_purete = fields.Char(string='Pureté')
    x_couleur = fields.Char(string='Couleur')
    x_type_de_prospect = fields.Char(string='Type de Prospect')
    x_laboratoire = fields.Char(string='Laboratoire')
    x_ville_principale = fields.Char(string='Ville Principale')
