# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) Open Solutions Finland 2014.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name" : "Spree Commerce",
    "version" : "1.0",
    "author" : "Open Solutions Finland",
    "description" : """
    Required fields for Spree Commerce endpoint integration
    """,
    "website" : "http://www.opensolutions.fi",
    "depends" : ["base","product","sale", "stock"],
    "category" : "Generic Modules",
    "init_xml" : [],
    "demo_xml" : [],
    "data" : [
              'spree_view.xml',
                    ],
    'test': [
             ],
    'installable': True,
    'active': False,
    'certificate': '',
}
