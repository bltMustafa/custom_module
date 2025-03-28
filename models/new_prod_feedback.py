from odoo import fields, models, api, _


class ProductFeedback(models.Model):
    _name = "new_prod.feedback"
    _description = "Product Feedback"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name')
    rating = fields.Float(string='Rating')
    product_id = fields.Many2one('product.template', string='Product')
    comment = fields.Text(string='Comment')
    date = fields.Datetime(string='Date')
