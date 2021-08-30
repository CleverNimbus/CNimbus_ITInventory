from odoo import fields, models, api, _


class AssetBase(models.Model):
    _name = 'cn.asset_base'
    _order = 'name'
    _description = 'Asset'

    name = fields.Char(required=True)
    description = fields.Html('Description')
    type_id = fields.Many2one('cn.asset_type')
    assignment_rel_ids = fields.One2many(comodel_name='cn.asset_assignment_rel', inverse_name='asset_id')
    manufacturer_id = fields.Many2one('cn.asset_manufacturer')
    active_assignment_id = fields.Float(
        string='Current Active Assignment',
        compute='_compute_current_assignment',
        store=False,
        compute_sudo=True,
    )

    @api.depends('assignments_ids')
    def _compute_current_assignment(self):
        assignments = self.assignment_rel_ids.search([('isActive', '=', 'True')])
        if assignments[0]:
            self.active_assignment_id = assignments[0].assignment_id
        else:
            self.active_assignment_id = None

    def name_get(self):
        result = []
        for record in self:
            rec_name = "%s (%s) [%s]" % (record.name, record.manufacturer_id.name, record.type_id.name)
            result.append((record.id, rec_name))
        return result


class AssetComputer(models.Model):
    _inherit = 'cn.asset_base'

    code = fields.Char('Computer Code', required=True)


class AssetSmartphone(models.Model):
    _inherit = 'cn.asset_base'

    imei = fields.Char('IMEI', required=True)


class AssetScreen(models.Model):
    _inherit = 'cn.asset_base'

    inches = fields.Float('Screen Inches', digits=(5, 2))


class AssetKeyboard(models.Model):
    _inherit = 'cn.asset_base'


class AssetMouse(models.Model):
    _inherit = 'cn.asset_base'


class AssetHeadset(models.Model):
    _inherit = 'cn.asset_base'


class AssetPendrive(models.Model):
    _inherit = 'cn.asset_base'

    driveSize = fields.Integer('Drive Size GB')
