# copyright 2004-2021 LOGILAB S.A. (Paris, FRANCE), all rights reserved.
# contact http://www.logilab.fr/ -- mailto:contact@logilab.fr
#
# This file is part of rql.
#
# rql is free software: you can redistribute it and/or modify it under the
# terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 2.1 of the License, or (at your option)
# any later version.
#
# rql is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License along
# with rql. If not, see <http://www.gnu.org/licenses/>.
"""Types declarations for RQL types annotations"""


from typing import TYPE_CHECKING, Dict, List

__docformat__ = "restructuredtext en"

Solution = Dict[str, str]
SolutionsList = List[Solution]

if TYPE_CHECKING:
    import rql
    BaseNode = rql.base.BaseNode
else:
    BaseNode = "rql.base.BaseNode"
