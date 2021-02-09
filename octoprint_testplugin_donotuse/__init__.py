# coding=utf-8
from __future__ import absolute_import

__author__ = "Shawn Bruce <kantlivelong@gmail.com>"
__license__ = "GNU Affero General Public License http://www.gnu.org/licenses/agpl.html"
__copyright__ = "Copyright (C) 2017 Shawn Bruce - Released under terms of the AGPLv3 License"

import octoprint.plugin
from octoprint.server import user_permission
from octoprint.events import Events
import time
import subprocess
import threading
import os
from flask import make_response, jsonify

class TestPlugin_DoNotUse(octoprint.plugin.StartupPlugin,
                 octoprint.plugin.TemplatePlugin,
                 octoprint.plugin.AssetPlugin,
                 octoprint.plugin.SettingsPlugin,
                 octoprint.plugin.SimpleApiPlugin,
                 octoprint.plugin.EventHandlerPlugin):

    def get_update_information(self):
        return dict(
            testplugin_donotuse=dict(
                displayName="OctoPrint-TestPlugin-DoNotUse",
                displayVersion=self._plugin_version,

                # version check: github repository
                type="github_release",
                user="kantlivelong",
                repo="OctoPrint-TestPlugin-DoNotUse",
                current=self._plugin_version,

                # update method: pip w/ dependency links
                pip="https://github.com/kantlivelong/OctoPrint-TestPlugin-DoNotUse/archive/{target_version}.zip"
            )
        )

__plugin_name__ = "OctoPrint-TestPlugin-DoNotUse"
__plugin_pythoncompat__ = ">=2.7,<4"

def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = TestPlugin_DoNotUse()

    global __plugin_hooks__
    __plugin_hooks__ = {
        "octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
    }
