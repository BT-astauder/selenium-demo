# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (c) 2017 brain-tec AG (http://www.braintec-group.com)
#    All Right Reserved
#
#    See LICENSE file for full licensing details.
##############################################################################
{
    'name': "Configure and Test",
    'author': "brain-tec AG",
    'license': 'LGPL-3',
    'version': '1.0',
    'summary': "Configure and Test",
    'category': 'Base',
    'website': 'http://www.braintec-group.com',
    'images': [
    ],
    'depends': [
        'auth_crypt',
        'base',
        'base_import',
        'base_setup',
        'base_technical_features',
        'bt_helper',
        'configure_odoo',
        'grid',
        'report',
        'server_environment',
        'server_environment_files',
        'web',
        'web_calendar',
        'web_diagram',
        'web_editor',
        'web_enterprise',
        'web_gantt',
        'web_kanban',
        'web_kanban_gauge',
        'web_mobile',
        'web_planner',
        'web_settings_dashboard',
        'web_tour'],
    'data': ['config_settings/_load_configuration_settings.yml',
             'config_settings/res.company.csv',
             ],
    'qweb': [
    ],
    'test': [
    ],
    'js': [
    ],
    'external_dependencies': {
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}
