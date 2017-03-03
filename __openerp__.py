# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

######################################################################

{
    'name': 'Evaluaciones 2DAM',
    'version': '1.0',
    'author': 'Daniel Castro Moreno',
    'category': 'Gestion',
    'summary': 'Gestión de evaluaciones 2DAM',
    'description': """
Módulo para el control de evaluaciones de los alumnos por módulos
======================
Con este módulo podremos introducir los resultados en las distintas evaluaciones de los alumnos
del curso 2 DAM del IES Francisco Ayala en el módulo de Sistemas de Gestión Empresarial.

Necesario el módulo de ventas.
    """,
    'license' : 'AGPL-3',
    'depends': ['sale'],
    'update_xml': [
        'template_view.xml',
    ],
    'installable': True,
    'active': False,
}