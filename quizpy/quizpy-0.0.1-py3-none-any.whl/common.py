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

import typing
import base64
import abc
import xml.etree.ElementTree as ET
import os

from dataclasses import dataclass, field

@dataclass
class InlineFile:
    name: str
    file: typing.BinaryIO

    @classmethod
    def load(cls, path: str):
        f = open(path, 'rb')
        return cls(os.path.basename(path), f)

    def to_xml(self) -> ET.Element:
        if self.file.seekable():
            self.file.seek(0)

        node = ET.Element('file')
        node.set('name', self.name)
        node.set('path', '/')
        node.set('encoding', 'base64')

        node.text = base64.standard_b64encode(self.file.read()).decode('utf-8')

        return node

    def link(self):
        return f'@@PLUGINFILE@@/{self.name}'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


@dataclass
class Question(abc.ABC):
    title: str
    text: str
    default_points: float

    format: str = 'html'
    id: int = None
    tags: typing.Iterable[str] = field(default_factory=list)
    penalty: float = 0.0
    hidden: bool = False
    general_feedback: str = ''

    files: typing.List[InlineFile] = field(default_factory=list)

    def generate_common_xml(self, qtype: str) -> ET.Element:
        node = ET.Element('question')
        node.set('type', qtype)

        name = ET.SubElement(node, 'name')
        ET.SubElement(name, 'text').text = self.title

        text = ET.SubElement(node, 'questiontext')
        text.set('format', self.format)
        ET.SubElement(text, 'text').text = self.text

        for inline in self.files:
            text.append(inline.to_xml())

        feedback = ET.SubElement(node, 'generalfeedback')
        feedback.set('type', self.format)
        ET.SubElement(feedback, 'text').text = self.general_feedback

        ET.SubElement(node, 'defaultgrade').text = str(self.default_points)
        ET.SubElement(node, 'penalty').text = str(self.penalty)
        ET.SubElement(node, 'hidden').text = '1' if self.hidden else '0'
        ET.SubElement(node, 'idnumber').text = str(self.id) if self.id is not None else ''
        return node

    @abc.abstractmethod
    def to_xml(self) -> ET.Element:
        pass



@dataclass
class Category:
    name: str
    description: str = ''
    questions: typing.List[Question] = field(default_factory=list)
    format: str = 'html'

    def to_xml(self) -> typing.List[ET.Element]:
        nodes = []

        category = ET.Element('question')  # Dummy question node
        category.set('type', 'category')

        name = ET.SubElement(category, 'category')
        ET.SubElement(name, 'text').text = self.name

        info = ET.SubElement(category, 'info')
        info.set('format', self.format)
        ET.SubElement(info, 'text').text = self.description

        nodes.append(category)

        for q in self.questions:
            nodes.append(q.to_xml())

        return nodes


@dataclass
class Quiz:
    categories: typing.List[Category] = field(default_factory=list)

    def to_xml(self) -> ET.Element:
        root = ET.Element('quiz')

        for c in self.categories:
            root.extend(c.to_xml())

        return root

    def export(self, path):
        with open(path, 'wb') as f:
            tree = ET.ElementTree(self.to_xml())
            tree.write(f, encoding='UTF-8', xml_declaration=True)
