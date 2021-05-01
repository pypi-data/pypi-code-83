import json
import base64


class MetaDataParser:
    @staticmethod
    def encode(d: dict) -> str:
        return base64.b64encode(json.dumps(d).encode()).decode()

    @staticmethod
    def decode(s: str) -> dict:
        return json.loads(base64.b64decode(s.encode()).decode())


class SubmissionValue:
    def __init__(self, type: str) -> None:
        self.type = type


class SubmissionValuePlainTextInput(SubmissionValue):
    def __init__(self, value: str) -> None:
        super().__init__(type="plain_text_input")
        self.value = value


class SubmissionValueCheckBoxes(SubmissionValue):
    def __init__(self, selected_options: list) -> None:
        super().__init__(type="checkboxes")
        self.selected_options = selected_options
        self.values = {}
        for option in self.selected_options:
            self.values[option["value"]] = option

    def isSelected(self, value: str) -> bool:
        if value in self.values:
            return True
        else:
            return False


class SubmissionParser:
    def __init__(self, payload) -> None:
        self.payload = payload

    def getValue(self, action_id, block_id=None):
        blocks = self.payload["view"]["state"]["values"]
        for block in blocks:
            if block_id == None or block == block_id:
                for action in blocks[block]:
                    if action == action_id:
                        if blocks[block][action]["type"] == "plain_text_input":
                            return SubmissionValuePlainTextInput(
                                blocks[block][action]["value"]
                            )
                        elif blocks[block][action]["type"] == "checkboxes":
                            selected = {}
                            selected["type"] = "checkboxes"
                            return SubmissionValueCheckBoxes(
                                blocks[block][action]["selected_options"]
                            )
