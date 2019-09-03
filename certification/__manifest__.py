# Copyright 2014-2015 Grupo ESOC <www.grupoesoc.es>
# Copyright 2017-Apertoso N.V. (<http://www.apertoso.be>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "Certification",
    "summary": "Defines certifications for different purposes",
    'version': '12.0.1.0.0',
    "category": "Certification Management",
    "website": "https://github.com/ysfklc",
    "author": "Grupo ESOC, Tecnativa, Odoo Community Association (OCA)",
    'data': ['security/certification_security.xml',
             'security/ir.model.access.csv',
             'views/certification_bodies_view.xml',
             'views/certification_view.xml',
             'views/res_partner_view.xml',
             'views/standard_view.xml'
             ],
    'demo': ['data/certification_data.xml'],
    "license": "AGPL-3",
    'application': False,
    'installable': True,
    'auto_install': False,
    'depends': ['base'],
    'development status':"beta",
    'maintainers':['ceeficent']
}
