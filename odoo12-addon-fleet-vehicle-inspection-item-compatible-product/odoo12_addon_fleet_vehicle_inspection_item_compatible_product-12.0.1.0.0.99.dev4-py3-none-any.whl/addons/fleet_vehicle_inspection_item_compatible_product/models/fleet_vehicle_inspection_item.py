# Copyright 2021 - TODAY, Marcel Savegnago <marcel.savegnago@escodoo.com.br>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class FleetVehicleInspectionItem(models.Model):

    _inherit = 'fleet.vehicle.inspection.item'

    compatible_product_ids = fields.Many2many(
        "product.product",
        "fleet_vehicle_inspection_item_compatible_product_rel",
        "vehicle_inspection_item_id",
        "product_id",
        "Products",
        domain=[("is_fleet_vehicle_product", "=", True)],
        context={"default_is_fleet_vehicle_product": True},
        help="Compatible Products/Services",
    )
