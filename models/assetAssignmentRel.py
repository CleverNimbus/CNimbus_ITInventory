from odoo import fields, models, api, _


class AssetAssignmentRel(models.Model):
    _name = 'cn.asset_assignment_rel'
    _description = 'Assets Assignment relationship'

    asset_id = fields.Many2one('cn.asset_base')
    assignment_id = fields.Many2one('cn.asset_assignment')

    isActive = fields.Boolean('Is Active')
