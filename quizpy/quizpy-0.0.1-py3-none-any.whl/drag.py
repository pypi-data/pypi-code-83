#    Quizpy - Creating Moodle exams in Python
#    Copyright (C) 2021  Sebastian Bräuer
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import xml.etree.ElementTree as ET
import typing

from dataclasses import dataclass, field
from .common import Question, InlineFile

# TODO Question Type ddwtos

@dataclass
class DragOption:
    text: str
    group: int = 1
    infinite: bool = False


@dataclass
class DropZone:
    location: typing.Tuple[int, int]
    choice: DragOption
    text: str = ""


@dataclass
class DDImage(Question):

    base_image: InlineFile = None  # Unfortunately,  this must be set with a default
    options: typing.List[DragOption] = field(default_factory=list)
    drops: typing.List[DropZone] = field(default_factory=list)
    shuffle: bool = False

    def to_xml(self) -> ET.Element:

        if self.base_image is None:
            raise ValueError("You need to set a base image!")

        node = self.generate_common_xml('ddimageortext')

        if self.shuffle:
            ET.SubElement(node, "shuffleanswers")

        node.append(self.base_image.to_xml())

        for i, opt in enumerate(self.options, start=1):
            drag = ET.SubElement(node, 'drag')
            ET.SubElement(drag, 'text').text = opt.text
            ET.SubElement(drag, 'draggroup').text = str(opt.group)
            ET.SubElement(drag, 'no').text = str(i)

            if opt.infinite:
                ET.SubElement(drag, 'infinite')

        for i, d in enumerate(self.drops, start=1):
            x, y = d.location
            drop = ET.SubElement(node, 'drop')
            ET.SubElement(drop, 'text')  # Empty sub-element
            ET.SubElement(drop, 'xleft').text = str(x)
            ET.SubElement(drop, 'ytop').text = str(y)
            ET.SubElement(drop, 'no').text = str(i)

            try:
                ET.SubElement(drop, 'choice').text = str(self.options.index(d.choice) + 1)
            except ValueError:
                raise ValueError("Choice for dropzone not found in drag options!")

        return node
