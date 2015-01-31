# coding=utf-8
from __future__ import absolute_import

__author__ = "Gijs van Roij <gijs@gijsvanroij.nl>"
__license__ = "GNU Affero General Public License http://www.gnu.org/licenses/agpl.html"
__copyright__ = "Copyright (C) 2015 Gijs van Roij - Released under terms of the AGPLv3 License"

import octoprint.plugin

class NavBarPlugin(octoprint.plugin.TemplatePlugin, octoprint.plugin.AssetPlugin):
            
    ##~~ AssetPlugin API
    
    def get_assets(self):
        return {

            "css": ["css/octohedron.css"],
            "less": ["less/octohedron.less"]
        } 
        
__plugin_name__ = "Octohedron Ui Concept"
__plugin_implementations__ = [NavBarPlugin()]
