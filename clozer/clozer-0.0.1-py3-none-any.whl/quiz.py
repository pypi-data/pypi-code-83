from xml.etree import ElementTree as ET
import re


class Quiz:
    file = "text.html"
    questionvars = []

    def __init__(self):
        self._name = "Pregunta"
        self._type = "cloze"
        self._count = 256
        self._txt = None

    def getArgs(self):
        self._vars = {}
        return {
            var: getattr(self, var)
            for var in self.questionvars
        }

    def getTXT(self):
        if self._txt is None:
            with open(self.file, 'r') as file:
                self._txt = "".join(file.readlines())
        return self._txt

    def createQuestion(self, quiz, type, name):
        question = ET.SubElement(quiz, "question", type=type)
        ename = ET.SubElement(question, "name")
        ET.SubElement(ename, "text").text = name

        qtext = ET.SubElement(question, "questiontext", format="html")
        qargs = self.getArgs()
        txt = self.getTXT()
        txt = self.preParse(txt)
        txt = txt.format(**qargs)
        txt = "\n<![CDATA[\n{}\n]]>\n".format(txt)
        ET.SubElement(qtext, "text").text = txt
        return question, qargs

    def preParse(self, txt):
        return txt

    def __str__(self):
        quiz = ET.Element("quiz")
        for i in range(self._count):
            name = "{} {}".format(self._name, i)
            self.createQuestion(quiz, self._type, name)
        tree = ET.tostring(quiz, encoding="unicode")
        tree = re.sub('&gt;', '>', tree)
        tree = re.sub('&lt;', '<', tree)
        return str(tree)

    def store(self):
        with open("{}.xml".format(self._name), 'w') as file:
            file.write(str(self))
