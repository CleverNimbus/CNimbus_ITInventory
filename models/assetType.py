from odoo import fields, models, api, _


class AssetType(models.Model):
    _name = 'cn.asset_type'
    _order = 'name'
    _description = 'Asset Type'

    name = fields.Char(required=True)
    loan_type = fields.Selection([('temporal', _('Temporal')),
                                  ('permanent', _('Permanent')),
                                  ('punctual', _('Punctual'))], string=_('Loan Type'), default='temporal')

    assets_ids = fields.One2many(comodel_name='cn.asset_base', inverse_name='type_id')
