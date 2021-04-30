import atexit
import base64
import glob
import logging
import mimetypes
import time
from enum import Enum
from pathlib import Path
from typing import Dict, List, Optional, Union, Tuple, Any, Generator

from robot.api.deco import library, keyword  # type: ignore
from robot.libraries.BuiltIn import BuiltIn, RobotNotRunningError  # type: ignore
from RPA.core.types import is_list_like  # type: ignore

from .types import Elements, Result, Options
from .dialog import Dialog, TimeoutException


def to_options(
    opts: Options, default: Optional[str] = None
) -> Tuple[List[str], Optional[str]]:
    """Convert keyword argument for multiple options into
    a list of strings.

    Also handles default option validation.
    """
    if isinstance(opts, str):
        opts = [opt.strip() for opt in opts.split(",")]
    elif is_list_like(opts):
        opts = [str(opt) for opt in opts]
    else:
        raise ValueError(f"Unsupported options type: {opts}")

    if not opts:
        return [], None

    if default is None:
        default = opts[0]

    if default not in opts:
        raise ValueError(f"Default '{default}' is not in available options")

    return opts, default


def optional_str(val: Any) -> Union[str, None]:
    """Convert value to string, but keep NoneType"""
    return str(val) if val is not None else val


def optional_int(val: Any) -> Union[int, None]:
    """Convert value to int, but keep NoneType"""
    return int(val) if val is not None else val


def int_or_auto(val: Any) -> Union[int, str]:
    """Convert value to int or 'AUTO' literal"""
    if isinstance(val, int):
        return val

    try:
        return int(val)
    except ValueError:
        pass

    height = str(val).strip().upper()
    if height == "AUTO":
        return height

    raise ValueError("Value not integer or AUTO")


class Size(Enum):
    """Element size options"""

    Small = "small"
    Medium = "medium"
    Large = "large"


class Icon(Enum):
    """Icon variants"""

    Success = "success"
    Warning = "warning"
    Failure = "failure"


@library(scope="GLOBAL", doc_format="REST", auto_keywords=False)
class Dialogs:
    """The `Dialogs` library provides a way to ask for user input during executions
    through HTML forms. Form elements can be built with library keywords or they can
    be defined in a static JSON file.

    **How the library works**

    The main keyword of the library is ``Request Response`` which works as follows:

    1. It starts an HTTP server in the background
    2. The HTML form is generated either according to a JSON file or the
       keywords called during the task
    3. It opens a browser and shows the created form (The browser is opened with
       the ``Open Available Browser`` keyword from the ``RPA.Browser.Selenium`` library)
    4. Once the form is filled and submitted by the user, the server will process
       the response and extract the field values, which in turn are returned by the keyword
    5. In the end, the browser is closed and the HTTP server is stopped

    ``Request Response`` can be invoked in two ways:

    1. Without any parameters. This means that form shown is the one created
       by other library keywords. If no form elements have been added with
       keywords then the form will contain just one submit button. Form building
       must be started with the keyword ``Create Form``.
    2. Giving a path to a JSON file (using the parameter **formspec**) which
       specifies the elements that form should include.

    The keyword has optional parameters to specify form window **width** and **height**.
    The default size is 600px wide and 1000px high.

    The ``Request Response`` logging is set as protected so that information is not
    visible in the Robot Framework log. The output of the keyword will be visible if
    ``Request Response`` is called within **User Keyword**, which returns the response,
    unless that is also protected with ``RPA.RobotLogListener`` library keyword
    ``Register Protected Keywords`` (see more at the library documentation).

    **Supported element types**

    As a bare minimum, the form is displayed with a submit button when the
    ``Request Response`` keyword is called.

    The supported input elements and their corresponding HTML tags are:

    - form (``<form>``)
    - title (``<h3>``)
    - text (``<p>``)
    - radiobutton  (``<input type='radio'>``)
    - checkbox (``<input type='checkbox'>``)
    - dropdown (``<select>``)
    - textarea (``<textarea>``)
    - textinput (``<input type='text'>``)
    - password (``<input type='password'>``)
    - fileinput (``<input type='file'>``)
    - hiddeninput (``<input type='hidden'>``)
    - submit (``<input type='submit'>``)

    **Examples**

    **Robot Framework**

    Examples of creating forms through keywords and a JSON file:

    .. code-block:: robotframework

        *** Settings ***
        Library    RPA.Dialogs

        *** Keywords ***
        Ask Question From User By Form Built With Keywords
            Create Form     questions
            Add Text Input  label=What is your name?  name=username
            &{response}=    Request Response
            Log             Username is "${response}[username]"

        Ask Question From User By Form Specified With JSON
            &{response}=    Request Response  /path/to/myform.json
            Log             Username is "${response}[username]"

    **Python**

    The library can also be used inside Python:

    .. code-block:: python

        from RPA.Dialogs import Dialogs

        def ask_question_from_user(question, attribute):
            d = Dialogs()
            d.create_form('questions')
            d.add_text_input(label=question, name=attribute)
            response = d.request_response()
            return response

        response = ask_question_from_user('What is your name ?', 'username')
        print(f"Username is '{response['username']}'")
    """  # noqa: E501

    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)
        self.elements: Elements = []
        self.dialogs: List[Dialog] = []

        try:
            # Prevent logging from keywords that return results
            keywords = [
                "Show dialog",
                "Wait dialog",
                "Wait all dialogs",
                "Wait dialogs as completed",
            ]
            BuiltIn().import_library(
                "RPA.core.logger.RobotLogListener", "WITH NAME", "RPA.RobotLogListener"
            )
            listener = BuiltIn().get_library_instance("RPA.RobotLogListener")
            listener.register_protected_keywords(keywords)
        except RobotNotRunningError:
            pass

        # Suppress useless error messages from pywebview
        logging.getLogger("pywebview").setLevel(logging.CRITICAL)

    def add_element(self, element: Dict[str, Any]) -> None:
        if element["type"].startswith("input-"):
            name = element["name"]
            names = [
                el["name"] for el in self.elements if el["type"].startswith("input-")
            ]

            if name in names:
                raise ValueError(f"Input with name '{name}' already exists")

            if name == "submit":
                raise ValueError("Input name 'submit' is not allowed")

        self.elements.append(element)

    @keyword("Clear elements")
    def clear_elements(self) -> None:
        self.elements = []

    @keyword("Add title")
    def add_title(
        self,
        title: str,
        size: Size = Size.Medium,
    ) -> None:
        """Add a title text element into the form.

        :param title: text for the element

        Example:

        .. code-block:: robotframework

            Create Form
            Add Title       User Confirmation Form

        """
        if not isinstance(size, Size):
            size = Size(size)

        element = {
            "type": "title",
            "value": str(title),
            "size": size.value,
        }

        self.add_element(element)

    @keyword("Add text")
    def add_text(
        self,
        text: str,
        size: Size = Size.Medium,
    ) -> None:
        """Add text paragraph element

        :param value: text for the element

        Example.

        .. code-block:: robotframework

            Create Form
            Add Text       ${form_guidance_text}

        """
        if not isinstance(size, Size):
            size = Size(size)

        element = {
            "type": "text",
            "value": str(text),
            "size": size.value,
        }

        self.add_element(element)

    @keyword("Add link")
    def add_link(
        self,
        url: str,
        label: Optional[str] = None,
    ) -> None:
        element = {
            "type": "link",
            "value": str(url),
            "label": optional_str(label),
        }

        self.add_element(element)

    @keyword("Add image")
    def add_image(
        self,
        url_or_path: str,
        width: Optional[int] = None,
        height: Optional[int] = None,
    ) -> None:
        if Path(url_or_path).is_file():
            mime, _ = mimetypes.guess_type(url_or_path)
            with open(url_or_path, "rb") as fd:
                data = base64.b64encode(fd.read()).decode()
                value = f"data:{mime};base64,{data}"
        else:
            # Assume image is a remote URL
            value = url_or_path

        element = {
            "type": "image",
            "value": str(value),
            "width": optional_int(width),
            "height": optional_int(height),
        }

        self.add_element(element)

    @keyword("Add file")
    def add_file(
        self,
        path: str,
        label: Optional[str] = None,
    ) -> None:
        resolved = Path(path).resolve()
        self.logger.info("Adding file: %s", resolved)

        if not resolved.exists():
            self.logger.warning("File does not exist: %s", resolved)

        element = {
            "type": "file",
            "value": str(resolved),
            "label": optional_str(label),
        }

        self.add_element(element)

    @keyword("Add files")
    def add_files(
        self,
        pattern: str,
    ) -> None:
        matches = glob.glob(pattern, recursive=True)
        for match in sorted(matches):
            self.add_file(match)

    @keyword("Add icon")
    def add_icon(self, variant: Icon, size: int = 48) -> None:
        if not isinstance(variant, Icon):
            variant = Icon(variant)

        element = {
            "type": "icon",
            "variant": variant.value,
            "size": int(size),
        }

        self.add_element(element)

    @keyword("Add text input", tags=["input"])
    def add_text_input(
        self,
        name: str,
        label: Optional[str] = None,
        placeholder: Optional[str] = None,
        rows: Optional[int] = None,
    ) -> None:
        """Add text input element

        :param label: input element label
        :param name: input element name attribute
        :param value: input element value attribute

        Example:

        .. code-block:: robotframework

            Create Form
            Add Text Input   what is your firstname ?  fname   value=Mika

        """
        element = {
            "type": "input-text",
            "name": str(name),
            "label": optional_str(label),
            "placeholder": optional_str(placeholder),
            "rows": optional_int(rows),
        }

        self.add_element(element)

    @keyword("Add password input", tags=["input"])
    def add_password_input(
        self,
        name: str,
        label: Optional[str] = None,
        placeholder: Optional[str] = None,
    ) -> None:
        """Add password input element

        :param label: input element label
        :param name: input element name attribute

        Example:

        """
        element = {
            "type": "input-password",
            "name": str(name),
            "label": optional_str(label),
            "placeholder": optional_str(placeholder),
        }

        self.add_element(element)

    @keyword("Add hidden input", tags=["input"])
    def add_hidden_input(
        self,
        name: str,
        value: str,
    ) -> None:
        """Add hidden input element

        :param name: input element name attribute
        :param value: input element value attribute

        Example:

        .. code-block:: robotframework

            Create Form
            ${uuid}   Evaluate  str(uuid.uuid4())
            Add Hidden Input    form-id   ${uuid}

        """
        element = {
            "type": "input-hidden",
            "name": str(name),
            "value": str(value),
        }

        self.add_element(element)

    @keyword("Add file input", tags=["input"])
    def add_file_input(
        self,
        name: str,
        label: Optional[str] = None,
        source: Optional[str] = None,
        destination: Optional[str] = None,
        file_type: Optional[str] = None,
        multiple: bool = False,
    ) -> None:
        """Add file input element

        :param label: input element label
        :param element_id: hidden element id attribute
        :param name: input element name attribute
        :param filetypes: accepted filetypes for the file upload
        :param target_directory: where to save uploaded files to

        **About file types**

        The ``Add File Input`` keyword has parameter ``filetypes``.
        Parameter sets filter for file types that can be uploaded via element.
        Parameter can be set to ``filetypes=${EMPTY}`` to accept all files.
        Multiple types are separated with comma ``filetypes=image/jpeg,image/png``.

        Some common filetypes:

        - image/* (all image types)
        - audio/* (all audio types)
        - video/* (all video types)
        - application/pdf (PDFs)
        - application/vnd.ms-excel (.xls, .xlsx)

        The list of all possible
        `MIME-types <http://www.iana.org/assignments/media-types/media-types.xhtml>`_.


        # file type string 'description (*.file_extension1;*.file_extension2)'

        Example:

        .. code-block:: robotframework

            Create Form
            Add File Input  label=Attachment
            ...             element_id=attachment
            ...             name=attachment
            ...             filetypes=${EMPTY}         # Accept all files
            ...             target_directory=${CURDIR}${/}output

            Add File Input  label=Contract
            ...             element_id=contract
            ...             name=contract
            ...             filetypes=application/pdf  # Accept only PDFs
            ...             target_directory=${CURDIR}${/}output

        """
        element = {
            "type": "input-file",
            "name": str(name),
            "label": optional_str(label),
            "source": optional_str(source),
            "destination": optional_str(destination),
            "file_type": optional_str(file_type),
            "multiple": bool(multiple),
        }

        self.add_element(element)

    @keyword("Add drop-down", tags=["input"])
    def add_drop_down(
        self,
        name: str,
        options: Options,
        default: Optional[str] = None,
        label: Optional[str] = None,
    ) -> None:
        """Add dropdown element

        :param label: dropdown element label
        :param element_id: dropdown element id attribute
        :param options: values for the dropdown
        :param default: dropdown selected value, defaults to None

        Example:

        .. code-block:: robotframework

            Create Form
            Add Dropdown  label=Select task type
            ...           element_id=tasktype
            ...           options=buy,sell,rent
            ...           default=buy

        """
        options, default = to_options(options, default)

        element = {
            "type": "input-dropdown",
            "name": str(name),
            "options": options,
            "default": default,
            "label": optional_str(label),
        }

        self.add_element(element)

    @keyword("Add radio buttons", tags=["input"])
    def add_radio_buttons(
        self,
        name: str,
        options: Options,
        default: Optional[str] = None,
        label: Optional[str] = None,
    ) -> None:
        """Add radio button element

        :param element_id: radio button element identifier
        :param options: values for the radio button
        :param default: radio button selected value, defaults to None

        Example:

        .. code-block:: robotframework

            Create Form
            Add Radio Button   element_id=drone  buttons=Jim,Robert  default=Robert

        """
        options, default = to_options(options, default)

        element = {
            "type": "input-radio",
            "name": str(name),
            "options": options,
            "default": default,
            "label": optional_str(label),
        }

        self.add_element(element)

    @keyword("Add checkbox", tags=["input"])
    def add_checkbox(
        self,
        name: str,
        label: str,
        default: bool = False,
    ) -> None:
        """Add checkbox element

        :param label: check box element label
        :param element_id: check box element identifier
        :param default: check box selected value, defaults to None

        Example:

        .. code-block:: robotframework

            Create Form
            Add Checkbox    label=Select your colors
            ...             element_id=colors
            ...             options=green,red,blue,yellow
            ...             default=blue

        """
        element = {
            "type": "input-checkbox",
            "name": str(name),
            "label": str(label),
            "default": bool(default),
        }

        self.add_element(element)

    @keyword("Add submit buttons", tags=["input"])
    def add_submit_buttons(
        self,
        buttons: Options,
        default: Optional[str] = None,
    ) -> None:
        """Add submit element

        :param name: element name attribute
        :param buttons: list of buttons

        Example:

        .. code-block:: robotframework

            Create Form
            Add Submit    name=direction-to-go  buttons=left,right

        """
        buttons, _ = to_options(buttons, default)

        element = {
            "type": "submit",
            "buttons": buttons,
            "default": default,
        }

        self.add_element(element)

    @keyword("Show dialog", tags=["dialog"])
    def show_dialog(self, timeout: int = 180, **options: Any) -> Result:
        dialog = self.create_dialog(**options)
        return self.wait_dialog(dialog, timeout)

    @keyword("Create dialog", tags=["dialog"])
    def create_dialog(
        self,
        title: str = "Title",
        height: Union[int, str] = "AUTO",
        width: int = 480,
        on_top: bool = False,
        clear: bool = True,
        debug: bool = False,
    ) -> Dialog:
        """Start server and show form. Waits for user response.

        :param formspec: form json specification file, defaults to None
        :param window_width: window width in pixels, defaults to 600
        :param window_height: window height in pixels, defaults to 1000
        :param timeout: optional time to wait for response, in seconds
        :return: form response

        Example:

        .. code-block:: robotframework

            Create Form    ${CURDIR}/${/}myform.json
            &{response}    Open dialog

        """
        height = int_or_auto(height)
        dialog = Dialog(
            self.elements,
            title=title,
            height=height,
            width=width,
            on_top=on_top,
            debug=debug,
        )

        dialog.start()
        self.dialogs.append(dialog)
        atexit.register(dialog.stop)

        if clear:
            self.clear_elements()

        return dialog

    @keyword("Wait dialog", tags=["dialog"])
    def wait_dialog(self, dialog: Dialog, timeout: int = 300) -> Result:
        """Wait for a given dialog to be handled by the user."""
        dialog.wait(timeout)
        return dialog.result()

    @keyword("Wait all dialogs", tags=["dialog"])
    def wait_all_dialogs(self, timeout: int = 300) -> List[Result]:
        """Wait for all opened dialogs to be handled by the user."""
        dialogs = list(self.wait_dialogs_as_completed(*self.dialogs, timeout=timeout))
        dialogs.sort(key=lambda d: d.timestamp)
        return [d.result() for d in dialogs]

    @keyword("Close dialog", tags=["dialog"])
    def close_dialog(self, dialog: Dialog) -> None:
        """Close a dialog that has been created with the keyword
        ``Create dialog``.
        """
        dialog.stop()

    @keyword("Close all dialogs", tags=["dialog"])
    def close_all_dialogs(self) -> None:
        """Close all dialogs opened by this library"""
        for dialog in self.dialogs:
            dialog.stop()

    def wait_dialogs_as_completed(
        self, *dialogs: Dialog, timeout: int = 300
    ) -> Generator[Dialog, None, None]:
        """Wait for multiple dialogs to finish and return results
        as they finish.
        """
        if not dialogs:
            return

        index = list(range(len(dialogs)))

        end = time.time() + timeout
        while time.time() <= end:
            if not index:
                return

            for idx in list(index):
                dialog = dialogs[idx]
                if dialog.poll():
                    self.logger.info(
                        "Dialog completed (%s/%s)",
                        len(dialogs) - len(index) + 1,
                        len(dialogs),
                    )
                    yield dialog
                    index.remove(idx)

            time.sleep(0.1)

        raise TimeoutException
