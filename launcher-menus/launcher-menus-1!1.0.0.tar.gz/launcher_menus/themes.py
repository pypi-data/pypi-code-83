#!/usr/bin/env python3
# -*- coding: utf-8; mode: python; -*-
#
# Copyright 2021 Pradyumna Paranjape
# This file is part of launcher-menus.
#
# launcher-menus is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# launcher-menus is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with launcher-menus.  If not, see <https://www.gnu.org/licenses/>.
#
'''
Launcher Menu Themes

'''

from pathlib import Path
from typing import Dict

import yaml

from .functions import LauncherMenu
from .read_config import user_config

menu = LauncherMenu()
'''
Plain ``menu`` object.

``command`` defaults to the first one found to be installed.
'''

password_prompt = LauncherMenu(filter_background="#000000",
                               filter_foreground="#000000",
                               prompt="Password: ")
'''
Password prompt menu.
'''

emergency_prompt = LauncherMenu(
    normal_background="#af1f00",
    filter_background="#af1f00",
    selected_background="#50e0ff",
    normal_foreground="#50e0ff",
    filter_foreground="#50e0ff",
    selected_foreground="#af1f00",
    title_background="#000000",
    title_foreground="#ffffff",
)
'''
Emergency prompt menu
'''


def custom_themes(custom_config: Path = None) -> Dict[str, LauncherMenu]:
    """
    Read configuration file ``themes.yml`` from
    standard configuration locations and generate custom themes
    """
    config_themes = {}
    for cfg_dir in user_config(custom_config):
        themes = None
        themes_f = cfg_dir.joinpath("themes.yml")
        if themes_f.is_file():
            with open(themes_f, "r") as theme_h:
                themes = yaml.safe_load(theme_h)
        if themes is not None:
            for new_theme, colors in themes.items():
                config_themes[new_theme] = LauncherMenu(**colors)
    return config_themes


for name, config in custom_themes().items():
    locals()[name] = config
'''
Configuration themes
'''
