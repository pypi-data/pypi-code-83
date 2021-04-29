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
import enum

from dataclasses import dataclass, field

from .common import Question
from .multipe_choice import Choice


class UnitGradingType(enum.Enum):
    NO_PENALTY = 0
    FRAC_RESPONSE_GRADE = 1
    FRAC_TOTAL_GRADE = 2


class UnitBehaviour(enum.Enum):
    Optional = 0
    Force = 1
    NoUnits = 3


@dataclass
class NumericalAnswer(Choice):
    tolerance: float = 0.0

    def to_xml(self) -> ET.Element:
        answer = super().to_xml()
        ET.SubElement(answer, 'tolerance').text = str(self.tolerance)
        return answer

    def to_cloze(self) -> str:
        if self.fraction == 100.0:
            s = f"={self.text}:{self.tolerance}#{self.feedback}"
        elif self.fraction == 0.0:
            s = f"{self.text}:{self.tolerance}#{self.feedback}"
        else:
            s = f"%{int(self.fraction)}%{self.text}:{self.tolerance}#{self.feedback}"
        return s


@dataclass
class Numerical(Question):
    accepted_answers: typing.List[NumericalAnswer] = field(default_factory=list)
    units: typing.List[typing.Tuple[str, float]] = field(default_factory=list)
    units_left: bool = False
    unit_grading_type: UnitGradingType = UnitGradingType.NO_PENALTY
    unit_behaviour: UnitBehaviour = UnitBehaviour.NoUnits
    unit_penalty: float = 0.1

    # TODO: Eingabeformat wird im XML komplett vergessen

    def to_xml(self) -> ET.Element:
        node = self.generate_common_xml('numerical')

        for answer in self.accepted_answers:
            node.append(answer.to_xml())

        units = ET.SubElement(node, 'units')
        for unit, multiplier in self.units:
            u = ET.SubElement(units, 'unit')
            ET.SubElement(u, 'multiplier').text = str(multiplier)
            ET.SubElement(u, 'unit_name').text = unit

        ET.SubElement(node, 'unitgradingtype').text = str(self.unit_grading_type.value)
        ET.SubElement(node, 'unitsleft').text = '1' if self.units_left else '0'
        ET.SubElement(node, 'showunits').text = str(self.unit_behaviour.value)
        ET.SubElement(node, 'unitpenalty').text = str(self.unit_penalty)

        return node

    def to_cloze(self, weight: int):
        cloze = f'{weight}:NM:'
        cloze += '~'.join(map(lambda a: a.to_cloze(), self.accepted_answers))

        return f'{{{cloze}}}'

