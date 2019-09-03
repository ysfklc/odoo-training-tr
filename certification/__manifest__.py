# Copyright 2014-2015 Grupo ESOC <www.grupoesoc.es>
# Copyright 2017-Apertoso N.V. (<http://www.apertoso.be>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "Certification",
    "summary": "Defines certitifcation for different purpose",
    "author": "Grupo ESOC, Tecnativa, Odoo Community Association (OCA)",
    'version': '12.0.1.0.0',
    "category": "Certification Management",
    "website": "https://github.com/ysfklc",
    "license": "AGPL-3",
    'application': True,
    'installable': True,
    'auto_install': False,
    "category":"Tools",
    "depends": [
        "base",
    ],
    "data": [
        "security/ir.model.access.csv", 
        "views/certification_view.xml", 
        "views/standard_view.xml"
    ]
}
