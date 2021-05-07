from typing import List, Dict
from requests import Session

class Report:
    url: str
    label: str
    system: str = "NOGROUP"
    status_code: str = "OK"
    description: str = "No description given."
    tags: List[str] = []
    severity: int = 5
    ttl: int = 0

    def __init__(self, client: Session):
        self.client = client

    def add_tag(self, tag: str):
        if tag in self.tags:
            return 

        self.tags.append(tag)


    def validate(self) -> None:
        if not self.url:
            raise ValueError("report.url must be set")

        if not self.label:
            raise ValueError("Report label must be set")


    def send(self) -> None:
        self.validate()

        payload: Dict = {
            "label": self.label,
            "system": self.system,
            "statusCode": self.status_code,
            "description": self.description,
            "tags": self.tags,
            "severity": self.severity,
            "ttl": self.ttl
        }

        response = self.client.post(url=self.url, json=payload)
        
        if response.status_code == 200:
            return

        raise ConnectionError("Something is wrong")


def new_report() -> Report:
    sess = Session()
    r = Report(sess)
    return r
