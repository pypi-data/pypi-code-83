import codecs
import re
from pathlib import Path
from typing import Iterator, Optional

import arrow
import yaml
from bs4 import BeautifulSoup

from .helpers import fix_absent_signer_problem, fix_multiple_sections_in_first


def is_problematic(d: dict):
    if d.get("item", None) and d.get("order", None):
        match = re.search(r"\d+", d["item"])
        digit = int(match.group()) if match else 999
        return digit != d["order"]


def find_problems(loc: Path):
    target_file = loc / "units.yaml"
    if not target_file.exists():
        return False
    with open(target_file, "r") as r:
        data = {}
        data["units"] = yaml.load(r, Loader=yaml.FullLoader)
        return is_problematic(data["units"][-1])


def origin_clause_not_null(loc: Path):
    target_file = loc / "details.yaml"
    if not target_file.exists():
        return False
    with open(target_file, "r") as r:
        data = yaml.load(r, Loader=yaml.FullLoader)
        if not data["origin_clause"]:
            return False
        return (data["origin_clause"], data["origin"])


def lapse_clause_not_null(loc: Path):
    target_file = loc / "details.yaml"
    if not target_file.exists():
        return False
    with open(target_file, "r") as r:
        data = yaml.load(r, Loader=yaml.FullLoader)
        if not data["lapse_into_law_clause"]:
            return False
        return (data["lapse_into_law_clause"], data["origin"])


def first_issue_detected(loc: Path):
    with open(loc / "units.yaml", "r") as r:
        data = {}
        data["units"] = yaml.load(r, Loader=yaml.FullLoader)
        if data["units"][0] and data["units"][0].get("content", None):
            return "SEC. 2" in data["units"][0]["content"]


def order_mismatches():
    folder = Path(".") / "ra"
    locations = folder.glob("*")
    return (loc for loc in locations if find_problems(loc))


def first_item_issues():
    return [loc for loc in order_mismatches() if first_issue_detected(loc)]


def get_body(loc: Path) -> str:
    body_location = loc / "body_statute.html"
    f = codecs.open(str(body_location))
    return f.read()


def get_legacy_file(loc: Path) -> Path:
    text = str(loc)
    parts = text.split("/")
    num = parts[-1]
    filename = f"ra{num}.yaml"
    return loc / filename


def get_details(loc: Path) -> Optional[dict]:
    try:
        with open(loc / "details.yaml", "r") as r:
            return yaml.load(r, Loader=yaml.FullLoader)
    except FileNotFoundError:
        return None


def add_old(filename: Path, data: dict) -> dict:
    with open(filename, "r") as r:
        unit_data = yaml.load(r, Loader=yaml.FullLoader)
        data |= unit_data
        data.pop("order")
        return data


def add_units(loc: Path, data: dict) -> Optional[dict]:
    if not data:
        return None
    target = loc / "units.yaml"
    if not target.exists():
        return data
    with open(loc / "units.yaml", "r") as r:
        data["units"] = yaml.load(r, Loader=yaml.FullLoader)
        data = fix_absent_signer_problem(data)
        data = fix_multiple_sections_in_first(data)
        return data


def set_whereas(loc: Path) -> dict:
    target = loc / "extra.html"
    if target.exists():
        f = codecs.open(str(target), "r")
        extra_content = f.read()
        title_case = "Whereas" in extra_content
        all_caps = "WHEREAS" in extra_content
        if title_case or all_caps:
            return {"whereas_clause": extra_content}
    return {"whereas_clause": None}


def load_data(loc: Path) -> Optional[dict]:
    """With the passed directory, get the relevant files.

    The high-level configuration file for the law is `details.yaml`
    See sample `details.yaml` under the folder ../pd/1

    - numeral: '1'
    - category: pd
    - origin: [url]
    - publications: []
    - enacting_clause: 'NOW, THEREFORE, I, FERDINAND E. MARCOS, x x x'
    - signers_of_law: 'Done in the City of Manila, x x x'
    - lapse_into_law_clause: null
    - law_title: Reorganizing The Executive Branch Of The National Government
    - date: September 24, 1972
    - item: Presidential Decree No. 1

    The `extra.html` file in this same directory contains the whereas clauses, if they exist.

    The `units.yaml` file in this same directory contains the sections.
    The source of this data is the e-library.

    A better file is the `pd1.yaml` since this includes nesting.
    The source of this data is Republic Act.

    This function combines the contents of the `details.yaml` file
    with the contents of either the `units.yaml` file or the `pd1.yaml` file.
    The resulting combination is a dictionary of key value pairs.

    Args:
        loc (Path): The source directory of the files mentioned above.

    Returns:
        Optional[dict]: The combined data found in the folder.
    """
    if not (data := get_details(loc)):
        print(f"No details.yaml file: {loc}.")
        return None

    data |= set_whereas(loc)

    legacy_file = get_legacy_file(loc)
    if legacy_file.exists():
        return add_old(legacy_file, data)
    else:
        return add_units(loc, data)


def get_directory(
    location: Path,
    law_category: str,
    serial_num: str,
) -> Optional[Path]:
    """With the location of the files, check if a specific folder exists with the given parameters

    Args:
        location (Path): Where the source material is stored
        law_category (str): Must be either "ra", "eo", "pd", "ca", "bp", "act"
        serial_num (str): A digit-like identifier, e.g. 209, 158-a, etc.

    Returns:
        Path: [description]
    """
    if law_category not in ["ra", "eo", "pd", "ca", "bp", "act"]:
        return None

    directory = location / f"{law_category}" / f"{serial_num}"
    if not directory.exists():
        return None

    return directory


def get_title(category: str, num: str):
    if category == "ra":
        category_text = "Republic Act No."
    elif category == "eo":
        category_text = "Executive Order No."
    elif category == "pd":
        category_text = "Presidential Decree No."
    elif category == "bp":
        category_text = "Batas Pambansa Blg."
    elif category == "ca":
        category_text = "Commonwealth Act No."
    elif category == "act":
        category_text = "Act No."
    return f"{category_text} {num}"


def preprocess(
    location: Path,
    law_category: str,
    serial_num: str,
) -> Optional[dict]:
    """If the location exists and there is data processed from such location,
    determine whether the important fields are present and then process (clean) the
    fields.

    Args:
        location (Path): Where the source material is stored
        law_category (str): Must be either "ra", "eo", "pd", "ca", "bp", "act"
        serial_num (str): A digit-like identifier, e.g. 209, 158-a, etc.

    Returns:
        Optional[dict]: Cleaned data dictionary
    """

    folder = get_directory(location, law_category, serial_num)
    if not folder:
        return None

    source = load_data(folder)
    if not source:
        return None

    for field in ["numeral", "law_title", "date", "units"]:
        if not source.get(field, None):
            return None

    return {
        "title": get_title(law_category, source["numeral"]),
        "full_title": source["law_title"],
        "specified_date": arrow.get(source["date"], "MMMM D, YYYY").date(),
        "publications": source.get("publications", None),
        "enacting_clause": source.get("enacting_clause", None),
        "whereas_clause": source.get("whereas_clause", None),
        "signers_of_law": source.get("signers_of_law", None),
        "lapse_into_law_clause": source.get("lapse_into_law_clause", None),
        "units": source["units"],
    }


def get_statute(parent: Path, child: Path, context: str) -> Optional[dict]:
    """

    Args:
        parent (Path): The parent path
        child (Path): The path to the statute
        context (str): The kind of statute

    Returns:
        Optional[dict]: [description]
    """

    parts = str(child).split("/")
    num = parts[-1]
    if not num.isdigit():
        print(f"Not a digit: {child}")
        return None

    print(f"Processing {child}")
    data = preprocess(parent, context, num)
    if data:
        return data
    else:
        print(f"Missing data: {child}")
        return None


def decode_statutes(parent: Path, context: str):
    """Given a parent directory "location" with a subfolder named "context",
    generate decision-like data from entries of the subfolder, or the grandchildren of the parent directory.

    Args:
        context (str): "ra" is the folder name

    Returns:
        [type]: [description]

    Yields:
        Iterator[dict]: Dictionaries containing data in dictionary format
    """
    folder = parent / "statutes"
    subfolder = folder / context
    for child in subfolder.glob("*"):
        yield get_statute(folder, child, context)


def dump_statute_data(target_directory: Path, data: dict):
    with open(target_directory, "w") as writefile:
        yaml.dump(data=data, stream=writefile, sort_keys=False)
        if target_directory / "data.yaml":
            print(f"Added data to: {target_directory}")


def create_statute_data(source_loc: Path, context: str):
    statutes_data = decode_statutes(source_loc, context)
    for data in statutes_data:
        if not source_loc / context / "data.yaml":
            dump_statute_data(source_loc / context, data)
        else:
            print(f"Existing data file: {source_loc / context}")
