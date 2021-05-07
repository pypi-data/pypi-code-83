#!/usr/bin/env python3
# -*- coding: utf-8; mode: python -*-
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
Load configurations
'''

import os
from pathlib import Path
from typing import Dict, List, Union

import yaml


def user_config(custom_root: Union[str, os.PathLike] = None) -> List[Path]:
    """
    Location of default configuration file

    Returns:
        path of default configuration file if found, else ``None``
    """
    # Default
    config_roots = [Path(__file__).parent.joinpath('menu-cfgs')]

    # User
    config_dir_path = None
    home_dir = os.environ.get('HOME')
    config_dir = os.environ.get('XDG_CONFIG_HOME')
    if config_dir is not None:
        config_dir_path = Path(config_dir)
    elif home_dir is not None:
        config_dir_path = Path(home_dir).joinpath('.config')  # usually
    if config_dir_path is not None and config_dir_path.is_dir():
        config_root = config_dir_path.joinpath('launcher_menus')
        if config_root.is_dir():
            config_roots.append(config_root)
    # Local
    local_root = Path(".").joinpath(".launcher_menus")
    if local_root.is_dir():
        config_roots.append(local_root)

    # Custom
    if custom_root is not None:
        custom_root = Path(custom_root)
        if custom_root.is_dir():
            config_roots.append(custom_root)
    return config_roots


def flag_names_from_file(
        custom_config: Path = None) -> Dict[str, Dict[str, str]]:
    '''
    Fish out specific flag names from known config files located in menu-cfg.

    custom_cfg: path to a custom configuration location

    Returns:
        flag_name: command- specific dictionary containing- k: action, v: flag.
        flag_name: empty dictionary if that config file was not found.

    '''
    known_menus: Dict[str, Dict[str, str]] = {}
    for cfg_dir in user_config(custom_config):
        for node in cfg_dir.glob("*"):
            # walk through all available flag_name files
            if node.stem in ("_template", "themes"):
                continue
            if node.is_file():
                if node.suffix.lower() in ('.yml', '.yaml'):
                    # {command}.yaml file
                    with open(node, 'r') as yml_handle:
                        known_menus[node.stem] = yaml.safe_load(yml_handle)
    return known_menus
