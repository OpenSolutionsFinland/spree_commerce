from osv import osv, fields
from openerp.tools.translate import _

class spree_product(osv.osv):
    _name="product.product"
    _inherit="product.product"
    
    _columns = {
        'waiting_spree_import': fields.boolean('Waiting spree import', required=False),
    }
    
    _defaults = {
        'waiting_spree_import': True,
    }

spree_product()


class spree_stock_picking(osv.osv):
    _name="stock.picking.out"
    _inherit="stock.picking.out"
    
    _columns = {
        'shipment_reported_spree': fields.boolean('Shipment reported to Spree', required=False),
    }
    
    _defaults = {
        'shipment_reported_spree': False,
    }
    
spree_stock_picking()