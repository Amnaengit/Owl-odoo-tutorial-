from odoo import http


class ResPartner(http.Controller):
    @http.route('/owl_odoo/rpc_service', type='json', auth='user')
    def get_customers(self):

        return http.request.env['res.partner'].search_read([], ['name', 'email'],)

    @http.route('/owl_odoo/dashboard_service', type='json', auth='user')
    def dashboard_service(self):
        partner = http.request.env['res.partner']
        return {
            "partner": partner.search_count([]),
            "customer": partner.search_count([('is_company', '=', True)]),
            "individual": partner.search_count([('is_company', '=', False)]),
            "location": len(partner.read_group([], ['state_id'], ['state_id'])),

        }