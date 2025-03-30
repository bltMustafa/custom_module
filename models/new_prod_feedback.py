from odoo import fields, models, api, _


class ProductFeedback(models.Model):
    _name = "new_prod.feedback"
    _description = "Product Feedback"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Reference", required=True, copy=False, readonly=True, default='New')
    rating = fields.Selection([
        ('1', '★☆☆☆☆'),
        ('2', '★★☆☆☆'),
        ('3', '★★★☆☆'),
        ('4', '★★★★☆'),
        ('5', '★★★★★')
    ], string='Rating', required=True)

    product_id = fields.Many2one('product.template', string='Product')
    comment = fields.Text(string='Comment')
    date = fields.Datetime(string='Date')
    image = fields.Binary(string='Image')
    image_filename = fields.Char(string='Filename')


    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('new_prod.feedback') or 'New'
        return super(ProductFeedback, self).create(vals)


class ProductTemplate(models.Model):
    _inherit = "product.template"

    feedback_ids = fields.One2many('new_prod.feedback', 'product_id', string="Feedbacks")
