from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    fiche_technique_image = fields.Image(
        string="Fiche Technique Image",
        help="Upload an image for the fiche technique."
    )
