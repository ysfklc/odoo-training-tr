# Copyright 2014-2015 Grupo ESOC <www.grupoesoc.es>
# Copyright 2017-Apertoso N.V. (<http://www.apertoso.be>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "Identity Of Partner",
    "summary": "Defines Identity of the Partner",
    'version': '12.0.1.0.0',
    "category": "Identity Management",
    "website": "https://github.com/ysfklc",
    "author": ["Yusuf Ali Kılıç"],
    'data': [
        'views/identification_view.xml',
        'security/identification_security.xml',
        'security/ir.model.access.csv'
    ],
    'demo': ['data/identification_data.xml'],
    "license": "AGPL-3",
    'application': False,
    'installable': True,
    'auto_install': False,
    'depends': ['base'],
    'development status': "beta",
    'maintainers': ['ceeficent']
}

