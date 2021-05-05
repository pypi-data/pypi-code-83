from typing import Any, Callable, Dict, List, Union

from mmcc_framework.activity import ActivityType
from mmcc_framework.callback_adapters import CallbackAdapter
from mmcc_framework.exceptions import DescriptionException
from mmcc_framework.framework import Process


def validate_process(process:  Union[Process, Dict[str, Any]]) -> List[str]:
    """ Performs some checks on the description, both syntactic and semantic.

    If the check is successful this returns an empty list, otherwise the list
    will contain the error messages (one or more than one).

    This checks that:
    - If process is a dictionary
        - it contains the list of activities and the id of the first one
        - each activity has an id and a valid type
        - each activity provides some choices according to its type
        - every id used has a corresponding activity
    - no activity is linked to itself as the next or as a choice
    - no activity contains None or Null in the choices
    - there are not duplicate choices
    - there are no activities with the same id
    - the first activity id has a corresponding activity

    This does not check:
    - the knowledge base, its contents and how it is used
    - the callbacks, their existence and behavior
    """
    if not isinstance(process, Process):
        process = Process.from_dict(process)

    errors = []
    try:
        process.check()
    except (DescriptionException, KeyError) as err:
        errors.append(str(err))
    return errors


def validate_callbacks(
        process:  Union[Process, Dict[str, Any]],
        callback_getter: CallbackAdapter):
    """ Checks that each callback used in the process is available.

    The process must be valid. ActivityType.END activities do not have a callback.

    This does not check:
    - the knowledge base, its contents and how it is used
    - that the callbacks have the correct method signature nor their behavior

    If the check is successful this returns an empty list, otherwise the list
    will contain the error messages (one or more than one).
    """
    if not isinstance(process, Process):
        process = Process.from_dict(process)

    errors = []
    for a in process.activities:
        if a.type == ActivityType.END:
            continue

        if not callback_getter.check(a.callback):
            errors.append(f"The callback is not valid: {a.callback} in activity {a.id}")
            continue

        try:
            callback = callback_getter.get(a.callback)
            if not callable(callback):
                errors.append(f"The callback getter for {a.callback} in activity {a.id} "
                              f"returned something that is not callable: {callback}")
        except BaseException as err:
            errors.append(f"The callback getter for {a.callback} in activity {a.id} "
                          f"raised an error: {str(err)}")
    return errors
