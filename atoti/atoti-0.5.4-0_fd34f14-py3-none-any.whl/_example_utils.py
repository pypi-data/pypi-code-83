from __future__ import annotations

from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Any, Optional, cast

import pandas as pd
from deepdiff import DeepDiff

from ._sessions import Sessions
from .config import SessionConfiguration, _parse_yaml_file_to_config
from .session import Session


def diff_yaml_config_with_python_config(
    yaml_config: str, python_config: SessionConfiguration
) -> Optional[DeepDiff]:
    with NamedTemporaryFile(delete=False, mode="w", prefix="atoti-") as file:
        try:
            file.write(yaml_config)
            file.close()
            parsed_yaml_config = _parse_yaml_file_to_config(Path(file.name))
        finally:
            Path(file.name).unlink()

    # Return None when the diff is empty so that interactive examples can omit the output line when the configs are equal.
    return DeepDiff(parsed_yaml_config, python_config) or None


def get_cleared_example_session_and_delete_other_ones(sessions: Sessions) -> Session:
    example_session_name = "Example"

    session_names_to_delete = [
        session_name
        for session_name in sessions
        if session_name != example_session_name
        # To be extra safe, also delete non regular sessions squatting the example session name.
        or (not isinstance(sessions[session_name], Session))
    ]

    for session_name in session_names_to_delete:
        del sessions[session_name]

    # Because of how session_names_to_delete is defined, example_session is either None or an instance of Session.
    example_session = cast(Optional[Session], sessions.get(example_session_name))

    if example_session:
        example_session._clear()
    else:
        example_session = sessions.create_session(example_session_name)

    return example_session


def monkey_patch_dataframe_repr_to_trim_trailing_whitespaces():
    """Used so that dataframes outputted in interactive examples match the expected output where trailing whitespaces have been trimmed by the IDE."""
    original_repr = pd.DataFrame.__repr__

    def patched_repr(*args: Any, **kwargs: Any) -> str:
        string = original_repr(*args, **kwargs)
        return "\n".join(line.rstrip() for line in string.splitlines())

    pd.DataFrame.__repr__ = patched_repr
