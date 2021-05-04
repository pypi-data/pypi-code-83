import csv
import logging
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING, List, Optional

from google.auth.transport.requests import Request
from google.oauth2 import service_account
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

if TYPE_CHECKING:
    from collections.abc import Iterator
    from io import IOBase

logger = logging.getLogger(__name__)


TOKEN_FILE = os.environ.get(
    "GS_TO_CSV_TOKEN_FILE_PATH", Path.home().joinpath(".gs-to-csv-token.json")
)
ALLOWED_SHEET_TYPE = ["GRID"]


@dataclass
class Sheet:

    api: object = None
    spreadsheet_id: str = None
    title: str = None
    column_count: int = None
    first_line_column_count: int = None
    row_count: int = None
    buffer_lines: int = None
    retrieved_lines_count: int = 1
    current_lines: "Iterator" = None

    def __iter__(self):
        return self

    def __next__(self):
        row = []
        if self.current_lines is None:
            self.get_next_rows()

        while len(row) == 0:
            try:
                row = next(self.current_lines)
                if row and self.first_line_column_count is None:
                    self.first_line_column_count = len(row)
            except StopIteration:
                self.get_next_rows()
        # ensure number of column still the same
        return (row + [""] * (self.first_line_column_count - len(row)))[
            : self.first_line_column_count
        ]

    def get_next_rows(self):
        if self.retrieved_lines_count > self.row_count:
            raise StopIteration()
        else:
            self.current_lines = iter(
                self.get_rows(self.retrieved_lines_count, self.buffer_lines)
            )
            self.retrieved_lines_count += self.buffer_lines

    def get_rows(self, row_start: int, row_count):
        return (
            self.api.values()
            .get(
                spreadsheetId=self.spreadsheet_id,
                range=f"{self.title}!{row_start}:{row_start + row_count - 1}",
            )
            .execute()
            .get("values", [])
        )


class GoogleSpreadSheetsToCSV:

    directory: "Path" = None
    spreadsheet_id: str = None
    sheets_selector: str = None
    service_account: Optional = None
    force: bool = None
    buffer_lines: int = None
    service = None
    api = None

    def __init__(
        self,
        outdir: "Path",
        spreadsheet_id: str,
        sheets_selector: str,
        service_account: Optional["IOBase"] = None,
        force: bool = False,
        buffer_lines: int = 500,
    ):
        self.directory = outdir
        self.spreadsheet_id = spreadsheet_id
        self.sheets_selector = sheets_selector
        self.service_account = service_account
        self.force = force
        self.buffer_lines = buffer_lines
        self.authenticate()

    def authenticate(self):
        # If modifying these scopes, delete the file token.json.
        SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

        creds = None

        if self.service_account:
            creds = service_account.Credentials.from_service_account_file(
                self.service_account, scopes=SCOPES
            )
        else:
            # The file token.json stores the user's access and refresh tokens, and is
            # created automatically when the authorization flow completes for the first
            # time.
            if TOKEN_FILE.is_file():
                creds = Credentials.from_authorized_user_file(str(TOKEN_FILE), SCOPES)
            # If there are no (valid) credentials available, let the user log in.
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        Path(__file__).parent.joinpath("google_app_oauth_id.json"),
                        SCOPES,
                    )
                    creds = flow.run_local_server(port=0)
                # Save the credentials for the next run
                with open(str(TOKEN_FILE), "w") as token:
                    token.write(creds.to_json())

        self.service = build("sheets", "v4", credentials=creds)
        self.api = self.service.spreadsheets()

    def get_exported_sheets(self):
        exported_sheet = []
        spreadsheet = self.api.get(spreadsheetId=self.spreadsheet_id).execute()
        logger.info("Reading %s spreadsheet", spreadsheet["properties"]["title"])
        regex = re.compile(self.sheets_selector)
        for sheet in spreadsheet["sheets"]:
            if (
                not regex.match(sheet["properties"].get("title", ""))
                or sheet["properties"].get("sheetType", "") not in ALLOWED_SHEET_TYPE
            ):
                continue
            exported_sheet.append(
                Sheet(
                    api=self.api,
                    spreadsheet_id=self.spreadsheet_id,
                    title=sheet["properties"]["title"],
                    column_count=sheet["properties"]["gridProperties"]["columnCount"],
                    row_count=sheet["properties"]["gridProperties"]["rowCount"],
                    buffer_lines=self.buffer_lines,
                )
            )
        return exported_sheet

    def export(self) -> List[str]:
        exported_files = []
        for sheet in self.get_exported_sheets():
            outpath = self.directory.joinpath(sheet.title + ".csv")
            if outpath.exists() and not self.force:
                raise FileExistsError(
                    f"File {str(outpath)} already present, use `--force` to overwrite."
                )
            with open(outpath, "w", newline="") as csvfile:
                writter = csv.writer(
                    csvfile, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
                )
                for row in sheet:
                    writter.writerow(row)
            exported_files.append(str(outpath))

        return exported_files
