from odoo import fields, models, api, _


class AssetManufacturer(models.Model):
    _name = 'cn.asset_manufacturer'
    _order = 'name'
    _description = 'Asset Manufacturer'

    name = fields.Char(required=True)
    assets_ids = fields.One2many(comodel_name='cn.asset_base', inverse_name='manufacturer_id')
