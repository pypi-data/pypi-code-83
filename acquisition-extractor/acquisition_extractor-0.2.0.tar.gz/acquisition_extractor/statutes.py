import codecs
import re
from pathlib import Path
from typing import Iterator, Match, Optional

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


def uniform_section_label(raw: str):
    """Replace the SECTION | SEC. | Sec. format with the word Section, if applicable."""
    regex = r"""
        ^\s*
        S
        (
            ECTION|
            EC|
            ec
        )
        [\s.,]+
    """
    pattern = re.compile(regex, re.X)
    if pattern.search(raw):
        text = pattern.sub("Section ", raw)
        text = text.strip("., ")
        return text
    return raw


def process_units(nodes: list[dict]) -> None:
    """Recursive function to ensure that the nested units comply with the database constraints.
    Each item should be limited to 500 characters. Each caption should be limited to 500 characters.
    For items which contain a variant of the "section" label, e.g. "SEC. 1", apply uniform label,
    i.e. "Section 1".

    Args:
        nodes (list[dict]): [description]
    """
    for node in nodes:
        if node.get("item", None):
            node["item"] = uniform_section_label(node["item"])
            if len(node["item"]) > 500:
                node["item"] = node["item"][:500]

        if caption := node.get("caption", None):
            if len(node["caption"]) > 500:
                node["caption"] = caption[:500]

        if node.get("units", None):
            process_units(node["units"])


def get_legacy_file(loc: Path, context: str) -> Path:
    text = str(loc)
    parts = text.split("/")
    num = parts[-1]
    filename = f"{context}{num}.yaml"
    return loc / filename


def get_details(loc: Path) -> Optional[dict]:
    try:
        details = loc / "details.yaml"
        if not details.exists():
            return None
        with open(details, "r") as r:
            return yaml.load(r, Loader=yaml.FullLoader) | set_whereas(loc)

    except FileNotFoundError:
        return None


def add_old(filename: Path, data: dict) -> dict:
    with open(filename, "r") as r:
        result = yaml.load(r, Loader=yaml.FullLoader)
        data["units"] = result["units"]
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


def load_statute(loc: Path) -> Optional[dict]:
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

    legacy_file = get_legacy_file(loc, data["category"])
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
        law_category (str): Must be either "ra", "eo", "pd", "ca", "bp", "act", "const"
        serial_num (str): A digit-like identifier, e.g. 209, 158-a, etc.

    Returns:
        Path: [description]
    """
    if law_category not in ["ra", "eo", "pd", "ca", "bp", "act", "const"]:
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
    elif category == "const":
        category_text = num
        num = "Constitution"
    return f"{category_text} {num}"


def data_from_folder(
    location: Path,
    law_category: str,
    serial_num: str,
) -> Optional[dict]:
    """If the location exists and there is data processed from such location,
    determine whether the important fields are present and then process (clean) the
    fields.

    Args:
        location (Path): Where the source material is stored
        law_category (str): Must be either "ra", "eo", "pd", "ca", "bp", "act", "const"
        serial_num (str): A digit-like identifier, e.g. 209, 158-a, etc.

    Returns:
        Optional[dict]: Cleaned data dictionary
    """

    if not (folder := get_directory(location, law_category, serial_num)):
        return None

    if not (source := load_statute(folder)):
        return None

    if source.get("units", None):
        process_units(source["units"])

    return map_to_model(law_category, source)


def map_to_model(law_category: str, source: dict) -> Optional[dict]:
    """The dictionary found in source needs to be mapped to the schema of the database.

    Args:
        law_category (str): Must be either "ra", "eo", "pd", "ca", "bp", "act", "const"
        source (dict): Pre-processed content

    Returns:
        Optional[dict]: Segregated data that matches the database schema for Statutes
    """
    for field in ["numeral", "law_title", "date", "units"]:
        if not source.get(field, None):
            return None

    # The database limit should be less than 1000 characters
    if len(source["law_title"]) > 1000:
        source["law_title"] = source["law_title"][:1000]

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
    # Is the folder digit-like, e.g. 209 or 209-A
    if not re.search(r"(^\d+-[A-C]$)|(^\d+$)", child.name):
        print(f"Not digit-like: {child}")
        return None

    print(f"Processing: {child}")
    data = data_from_folder(parent, context, child.name)
    if data:
        return data
    else:
        print(f"Missing data: {child}")
        return None
