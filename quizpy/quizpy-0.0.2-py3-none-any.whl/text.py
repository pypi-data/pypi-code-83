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

from .common import Question
from .multipe_choice import Choice


@dataclass
class ShortAnswer(Question):
    case_sensitive: bool = False
    accepted_answers: typing.List[Choice] = field(default_factory=list)

    def to_xml(self) -> ET.Element:
        node = self.generate_common_xml('shortanswer')
        ET.SubElement(node, 'usecase').text = '1' if self.case_sensitive else 0

        for answer in self.accepted_answers:
            node.append(answer.to_xml())

        return node

    def to_cloze(self, weight: int) -> str:
        cloze = f"{weight}:SA:" if not self.case_sensitive else f"{weight}:SAC:"

        cloze += '~'.join(map(lambda s: s.to_cloze(), self.accepted_answers))

        return f"{{{cloze}}}"


class Description(Question):

    def to_xml(self) -> ET.Element:
        node = self.generate_common_xml('description')
        return node


@dataclass
class Essay(Question):
    grading_info: str = ""
    response_format: str = "editor"
    response_required: bool = True
    response_template: str = ""
    attachements_required: bool = False
    max_attachements: int = 0
    max_lines: int = 15

    def to_xml(self) -> ET.Element:
        node = self.generate_common_xml('essay')

        ET.SubElement(node, 'responseformat').text = self.response_format
        ET.SubElement(node, 'responserequired').text = '1' if self.response_required else '0'
        ET.SubElement(node, 'responsefieldlines').text = str(self.max_lines)
        ET.SubElement(node, 'attachements').text = str(self.max_attachements)
        ET.SubElement(node, 'attachementsrequired').text = '1' if self.attachements_required else '0'

        grading_info = ET.SubElement(node, 'graderinfo')
        grading_info.set('format', self.format)
        ET.SubElement(grading_info, 'text').text = self.grading_info

        template = ET.SubElement(node, 'responsetemplate')
        template.set('format', self.format)
        ET.SubElement(template, 'text').text = self.response_template

        return node


class Cloze(Question):
    """The question text will be rendered using the custom Cloze syntax.
    See https://docs.moodle.org/310/en/Embedded_Answers_(Cloze)_question_type.

    You can also use the `to_cloze()` functions of the relevant question classes to generate the syntax for you.
    """

    def to_xml(self) -> ET.Element:
        node = self.generate_common_xml('cloze')
        return node
