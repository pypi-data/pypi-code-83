from xml.etree import ElementTree as ET
from .quiz import Quiz


class ShortAnswerQuiz(Quiz):
    def __init__(self):
        super().__init__()
        self._type = "shortanswer"

    def createQuestion(self, quiz, type, name):
        question, qargs = super().createQuestion(quiz, type, name)
        answer = ET.SubElement(
            question, "answer", fraction="100", format="moodle_auto_format")
        ET.SubElement(answer, "text").text = qargs['answer']
        print(qargs)

        return question, qargs
