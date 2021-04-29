import json
import base64

class MetaDataParser:
    @staticmethod
    def encode(d: dict) -> str:
        return base64.b64encode(json.dumps(d).encode()).decode()

    @staticmethod
    def decode(s: str) -> dict:
        return json.loads(base64.b64decode(s.encode()).decode())


class SubmissionParser:
    def __init__(self, payload) -> None:
        self.payload = payload

    def getValue(self, action_id, block_id=None):
        if block_id == None:
            blocks = self.payload["view"]["state"]["values"]
            for block in blocks:
                for action in blocks[block]:
                    if action == action_id:
                        return blocks[block][action]["value"]
        else:
            blocks = self.payload["view"]["state"]["values"]
            for block in blocks:
                if block == block_id:
                    for action in blocks[block]:
                        if action == action_id:
                            return blocks[block][action]["value"]