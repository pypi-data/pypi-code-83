import os
from shutil import copy
import subprocess


def generate_pymol(xyz_directory):
    print("If you do not want to generate a pymol session, enter 'exit'")
    filenames_to_pymol = input("File Names: ").split()
    if filenames_to_pymol[0].lower() == "exit":
        return

    print("File Names Received")
    print("Files to print below")
    for file in filenames_to_pymol:
        print(file)

    print(filenames_to_pymol)
    print()
    print("Please create a New Folder to copy structures into")
    current_directory = os.getcwd()
    added_xyz_folder_path = input("Enter New Folder Name: ")
    xyz_folder_path = os.path.join(current_directory,added_xyz_folder_path)

    os.mkdir(xyz_folder_path)
    print("Folder Created")
    # user_input_directory = "/Users/matthewnwerem/Chapman University/OMO Research Group - Project Conf. Analysis - Nwerem - proj_conf_analysis/Code Versions/Conformational_Analysis/pentane_file_test"
    user_input_directory = xyz_directory
    xyz_files_dir = os.listdir(user_input_directory)

    xyz_files = []
    for file in xyz_files_dir:
        if file.endswith(".xyz"):
            xyz_files.append(file)

    print("Printing all possible XYZ Files in question to be able to see in PyMol ")
    print(xyz_files)

    #  if there is a file in filenames_to_Pymol, that matches a file in xyz_files_dir, then
    for current_file in filenames_to_pymol:
        for current_file2 in xyz_files:
            if current_file == current_file2:
                #  copy file to the new directory path
                file_name = current_file2
                print("Copying " + file_name + " ...")
                print(xyz_folder_path)
                current_file_path = os.path.join(user_input_directory, file_name)
                copy(current_file_path, xyz_folder_path)

    os.chdir(xyz_folder_path)
    print("Directory Changed")
    subprocess.Popen("mGenerate_PyMOL_Session.sh", cwd=None, shell= True)


# testing function
#/Users/matthewnwerem/Chapman University/OMO Research Group - Project Conf. Analysis - Nwerem - proj_conf_analysis/Code Versions/Conformational_Analysis/pentane_file_test
# generate_pymol("/Users/matthewnwerem/Chapman University/OMO Research Group - Project Conf. Analysis - Nwerem - proj_conf_analysis/Code Versions/Conformational_Analysis/pentane_file_test")