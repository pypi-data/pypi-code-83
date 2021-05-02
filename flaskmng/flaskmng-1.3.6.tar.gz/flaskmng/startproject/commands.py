from os.path import join
from myp import MYPReader
from myp import const as myp_const
from ..utils import (
    command_process_step,
    info_message,
    process_ok,
    process_step,
    create_folder,
    success_message,
    make_compatible,
    hl
)
from .utils import (
    create_static_folders,
    create_init_py,
    create_config_py,
    create_app_py,
    create_gitignore,
    create_env,
)
from ..__main__ import main

@main.command("startproject")
def startproject_command():
    """Create new project"""
    processes = []
    process_ok(processes)

    # Install MYP
    command_process_step(
        "Installing MYP...", "pip install --upgrade myp")
    processes.append("Installed MYP")
    process_ok(processes)

    # Create myp.json
    command_process_step("Initializing MYP...",
                        'myp init --template="flaskmng"')
    processes.append("Initialized MYP")
    process_ok(processes)

    # Create config field
    myp = MYPReader()
    myp_config = myp.get_data("config")
    myp_config["APPS"] = []
    myp_config["PROJECT_NAME"] = make_compatible(myp.get_data("name"))
    myp.set_data("config",myp_config)
    myp.write()

    prj_name = myp_config["PROJECT_NAME"]

    # Installing dependencies
    command_process_step(f"Installing dependencies from {hl(myp_const.filename)}...",
                        'myp get:deps --dev')
    processes.append(f"Installed dependencies from {hl(myp_const.filename)}")
    process_ok(processes)

    # Creating main app folder
    process_step(f"Creating {hl(prj_name)} folder...",
                create_folder(prj_name))
    processes.append(f"Created {hl(prj_name)} folder")
    process_ok(processes)

    # Creating .gitignore
    process_step(f"Creating {hl('.gitignore')}...", create_gitignore)
    processes.append(f"Created {hl('.gitignore')}")
    process_ok(processes)

    # Creating app.py
    process_step(f"Creating {hl('app.py')}...", create_app_py(prj_name))
    processes.append(f"Created {hl('app.py')}")
    process_ok(processes)

    # Creating config.py
    process_step(f"Creating {hl('config.py')}...", create_config_py)
    processes.append(f"Created {hl('config.py')}")
    process_ok(processes)

    # Creating .env
    process_step(f"Creating {hl('.env')}...", create_env)
    processes.append(f"Created {hl('.env')}")
    process_ok(processes)

    # Creating project __init__.py
    process_step(f"Creating {hl(join(prj_name,'__init__.py'))}...",
                create_init_py(prj_name))
    processes.append(f"Created {hl(join(prj_name,'__init__.py'))}")
    process_ok(processes)

    # Creating js, css, image folders
    process_step(f"Creating {hl(join(prj_name,'static'))} folder...",
                create_static_folders(prj_name))
    processes.append(f"Created {hl(join(prj_name,'static'))} folder")
    process_ok(processes)

    # Initializing DB
    command_process_step("Initializing database...", "flask db init")
    processes.append("Initialized database")
    process_ok(processes)

    # Commiting initial migration
    command_process_step("Commiting initial migration...",
                        'flask db migrate -m "initial"')
    processes.append("Commited initial migration")
    process_ok(processes)

    # Upgrading migration
    command_process_step("Upgrading migration...", "flask db upgrade")
    processes.append("Upgraded migration")
    process_ok(processes)

    # Initializing git
    command_process_step("Initializing git...", "git init")
    processes.append("Initialized git")
    process_ok(processes)

    # Output success message
    success_message(f"Successfully created project {hl(prj_name)}")
    info_message(f"Use {hl('myp start')} to run your application")