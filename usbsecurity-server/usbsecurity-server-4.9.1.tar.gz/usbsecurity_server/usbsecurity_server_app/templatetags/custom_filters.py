#  This module belongs to the usbsecurity-server project.
#  Copyright (c) 2021 Alexis Torres Valdes
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#  Contact: alexis89.dev@gmail.com

import uuid
import os

from django import template

from usbsecurity_server.usbsecurity_server import settings

register = template.Library()


@register.simple_tag(name='cache_bust')
def cache_bust():
    statics_version = getattr(settings, 'STATICS_VERSION', None)

    if not statics_version:
        project_version = os.environ.get('PROJECT_VERSION')
        version = project_version if project_version else 1
    else:
        version = uuid.uuid1() if statics_version < 0 else statics_version

    return 'v={version}'.format(version=version)
