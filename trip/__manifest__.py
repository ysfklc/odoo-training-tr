# Copyright 2014-2015 Grupo ESOC <www.grupoesoc.es>
# Copyright 2017-Apertoso N.V. (<http://www.apertoso.be>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "Trip",
    "summary": "Defines trips for different purposes",
    'version': '12.0.1.0.0',
    "category": "Trip Management",
    "website": "https://github.com/ysfklc",
    "author": ["Yusuf Ali Kılıç", "Fatma Betül Ceylan", "Buğra Kaan Türkmenoğlu"],
    'data': [
        'views/trip_view.xml',
        'views/trip_bodies_view.xml',
        'views/res_partner_view.xml',
        'security/trip_security.xml',
        'security/ir.model.access.csv'
    ],
    'demo': [],
    "license": "AGPL-3",
    'application': False,
    'installable': True,
    'auto_install': False,
    'depends': ['base'],
    'development status': "beta",
    'maintainers': ["Odooveloper"]
}
