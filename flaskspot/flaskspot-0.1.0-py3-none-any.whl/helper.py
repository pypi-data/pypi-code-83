windows_success_msg = """
Inside that project directory, you can run serval commands:

    python manage.py --help
        Check all commands

You can begin by typing:

    cd {project_name}
    setup your virtual environment
    pip install -r requirements.txt
    python manage.py runserver

"""


common_success_msg = """
Inside that project directory, you can run serval commands:

    make help
        Shows all make commands
    
    make install
        Installs dependency from requirements.txt
    
    make run
        Runs flask application

You can begin by typing:

    cd {project_name}
    setup your virtual environment
    make install
    make run

"""