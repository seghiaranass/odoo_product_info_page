from odoo import http
from odoo.http import request

class ProductInfoController(http.Controller):

    @http.route('/product/<int:product_id>', type='http', auth='public', website=True)
    def product_page(self, product_id):
        product = request.env['product.template'].sudo().browse(product_id)
        if not product.exists():
            return request.render('website.404')
        

        return request.render('odoo_product_info_page.product_page_template', {
            'product': product
        })
