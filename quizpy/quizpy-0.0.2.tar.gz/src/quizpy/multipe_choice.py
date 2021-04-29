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


@dataclass
class Choice:
    text: str
    fraction: float

    feedback: str = ''
    format: str = 'html'

    def to_xml(self) -> ET.Element:
        answer = ET.Element('answer')
        answer.set('fraction', str(self.fraction))
        answer.set('format', self.format)

        ET.SubElement(answer, 'text').text = self.text
        fb = ET.SubElement(answer, 'feedback')
        fb.set('format', self.format)
        ET.SubElement(fb, 'text').text = self.feedback

        return answer

    def to_cloze(self) -> str:
        if self.fraction == 100.0:
            s = f"={self.text}#{self.feedback}"
        elif self.fraction == 0.0:
            s = f"{self.text}#{self.feedback}"
        else:
            s = f"%{int(self.fraction)}%{self.text}#{self.feedback}"
        return s


@dataclass
class MultipleChoice(Question):
    shuffle: bool = True
    single: bool = False
    numbering: str = 'abc'
    choices: typing.List[Choice] = field(default_factory=list)

    correct_feedback: str = 'Die Antwort ist richtig.'
    partial_feedback: str = 'Die Antwort ist teilweise richtig.'
    incorrect_feedback: str = 'Die Antwort ist falsch.'

    def add_choice(self, text: str, fraction: float, feedback: str = '', format: str = 'html'):
        c = Choice(text, fraction,feedback,format)
        self.choices.append(c)
        return c

    def to_xml(self):
        node = self.generate_common_xml('multichoice')
        node.set('type', 'multichoice')

        ET.SubElement(node, 'shuffleanswers').text = 'true' if self.shuffle else 'false'

        ET.SubElement(node, 'single').text = 'true' if self.single else 'false'
        ET.SubElement(node, 'answernumbering').text = self.numbering

        correct_feedback = ET.SubElement(node, 'correctfeedback')
        correct_feedback.set('format', self.format)
        ET.SubElement(correct_feedback, 'text').text = self.correct_feedback

        partial_feedback = ET.SubElement(node, 'partiallycorrectfeedback')
        partial_feedback.set('format', self.format)
        ET.SubElement(partial_feedback, 'text').text = self.partial_feedback

        wrong_feedback = ET.SubElement(node, 'incorrectfeedback')
        wrong_feedback.set('format', self.format)
        ET.SubElement(wrong_feedback, 'text').text = self.incorrect_feedback

        for c in self.choices:
            node.append(c.to_xml())

        return node

    def to_cloze(self, weight: int, display_type: str = "dropdown", alignment: str = 'horizontal', shuffle: bool = False) -> str:

        if display_type not in {'dropdown', 'radio', 'checkbox'}:
            raise ValueError("display_type must be either 'dropdown', 'radio' or 'checkbox'!")

        if alignment not in {'horizontal', 'vertical'}:
            raise ValueError("alignment must be either 'horizontal', 'vertical'!")

        if display_type == 'dropdown':
            cloze_type = 'MC'
        elif display_type == 'radio':
            if alignment == 'horizontal':
                cloze_type = 'MCH'
            else:
                cloze_type = 'MCV'
        else:
            if alignment == 'horizontal':
                cloze_type = 'MRH'
            else:
                cloze_type = 'MR'

        if shuffle:
            cloze_type += 'S'

        cloze = f'{weight}:{cloze_type}:'
        cloze += '~'.join(map(lambda s: s.to_cloze(), self.choices))

        return f"{{{cloze}}}"


@dataclass
class MultiTrueFalse(Question):
    scoring_method: str = 'subpoints'
    shuffle: bool = True
    options: typing.List = field(default_factory=lambda: ['Wahr', 'Falsch'])
    statements: typing.List[typing.Tuple[str, str, str]] = field(default_factory=list)

    def add_statement(self, text: str, value: str, feedback: str = ''):
        self.statements.append((text, value, feedback))

    def to_xml(self) -> ET.Element:
        node = self.generate_common_xml('mtf')

        scoring = ET.SubElement(node, 'scoringmethod')
        ET.SubElement(scoring, 'text').text = self.scoring_method

        ET.SubElement(node, 'shuffleanswers').text = 'true' if self.shuffle else 'false'

        num_rows = len(self.statements)
        num_cols = len(self.options)

        ET.SubElement(node, 'numberofrows').text = str(num_rows)
        ET.SubElement(node, 'numberofcolumns').text = str(num_cols)

        for i, (text, _, feedback) in enumerate(self.statements, start=1):
            row = ET.SubElement(node, 'row')
            row.set('number', str(i))

            opt = ET.SubElement(row, 'optiontext')
            opt.set('format', self.format)
            ET.SubElement(opt, 'text').text = text

            fb = ET.SubElement(row, 'feedbacktext')
            fb.set('format', self.format)
            ET.SubElement(fb, 'text').text = feedback

        for i, opt in enumerate(self.options, start=1):
            col = ET.SubElement(node, 'column')
            col.set('number', str(i))

            resp = ET.SubElement(col, 'responsetext')
            resp.set('format', self.format)
            ET.SubElement(resp, 'text').text = opt

        for i, (_, correct, _) in enumerate(self.statements, start=1):
            for j, opt in enumerate(self.options, start=1):
                weight = ET.SubElement(node, 'weight')
                weight.set('rownumber', str(i))
                weight.set('columnnumber', str(j))

                ET.SubElement(weight, 'value').text = '1.000' if opt == correct else '0.000'

        return node


@dataclass
class Matching(Question):
    shuffle: bool = True
    pairs: typing.List[typing.Tuple[str, str]] = field(default_factory=list)

    def to_xml(self) -> ET.Element:
        node = self.generate_common_xml('matching')

        for text, answer in self.pairs:
            subquestion = ET.SubElement(node, 'subquestion')
            subquestion.set('format', self.format)

            ET.SubElement(subquestion, 'text').text = text
            aw = ET.SubElement(subquestion, 'answer')
            ET.SubElement(aw, 'text').text = answer

        return node

