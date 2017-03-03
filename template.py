# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

######################################################################

from openerp.osv import fields, osv, orm
from datetime import time, datetime
from openerp.tools.translate import _


class template_modelo(osv.osv):
    _name = 'template.modelo'
    _description = 'Formulario de evaluaciones'
    _columns = {
        'name': fields.char('Nombre', size=256, required=True),
        'apellidos': fields.char('Nombre', size=256, required=True),
        '1ev': fields.integer('1ª Evaluación', required=False),
        '2ev': fields.integer('2ª Evaluación', required=False),
        'final': fields.integer('Final', required=False),
        'active': fields.boolean('Activo'),
    }
    _defaults = {
        'active': 'true',
    }

template_modelo()
