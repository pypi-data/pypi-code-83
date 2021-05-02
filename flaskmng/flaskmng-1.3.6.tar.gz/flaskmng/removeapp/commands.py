from os.path import join
from myp import MYPReader
from myp import const as myp_const
from typing import List
from ..utils import (
    info_message,
    process_ok,
    process_step,
    success_message,
    hl,
    take_input
)
from .utils import (
    remove_app,
    remove_app_imports
)
from ..__main__ import main

@main.command("removeapp")
def removeapp_command():
    """Remove app in project"""
    myp:MYPReader = MYPReader()
    prj_name:str = myp.get_data("config").get('PROJECT_NAME', '')
    app_list:List[str] = myp.get_data("config").get('APPS', [])
    processes:List[str] = []
    process_ok(processes)

    # Taking app name to remove
    app_name = take_input("Enter name of app to remove:")

    # Removing app folder
    if not prj_name :
        raise Exception(f"You deleted your project name from {myp_const.filename} file. Please add it.")
    if not app_name in app_list:
        raise Exception("Your app name is not in app list")
    process_step(f"Removing {hl(join(prj_name, app_name))} folder...",
                remove_app(join(prj_name, app_name)))
    processes.append(f"Removed {hl(join(prj_name, app_name))} folder")
    process_ok(processes)

    # Removing app name from myp.json
    myp_config = myp.get_config()
    myp_config['APPS'].remove(app_name)
    myp.set_config(myp_config)
    myp.write()

    # Removing app modules from __init__.py
    process_step(f"Removing imports of {hl(app_name)} from {hl(join(prj_name, '__init__.py'))}...",
                remove_app_imports(prj_name, app_name))
    processes.append(f"Removed imports of {hl(app_name)} from {hl(join(prj_name, '__init__.py'))}")
    process_ok(processes)

    # Output success message
    success_message(f"Successfully removed {hl(app_name)}")
    info_message(f"Use {hl('myp start')} to run your application")
