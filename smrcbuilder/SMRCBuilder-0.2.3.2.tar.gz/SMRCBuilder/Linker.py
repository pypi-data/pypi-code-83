from SMRCBuilder import Exceptions
import csv
import os
from time import sleep
import zipfile
import subprocess

def sendprompt(name, repo, folder, directory):
    check = input(f"The Interface '{name}' Already Exists. Do You Want To Overwrite It? (Y/N): ")
    if check == "Y":
        with open("install.bat",'w') as w:
            w.write(f'rmdir /Q /S "{directory}/{name}"')
            w.close()
        os.startfile("install.bat")
        sleep(5)

        if repo != None:
            os.system(f'git clone {repo} "{directory}/{name}"')

        elif folder != None:
            with zipfile.ZipFile(f"{name}.zip", 'r') as r:
                r.extractall(str(os.path.dirname(name)))

            try:
                os.rename(folder, name)
            except PermissionError:
                print(f"The Program Was Prevented From Changing {folder} to {name}")

    elif check == "N":
        return
        
    else:
        print("Incorrect Answer Passed. Skipped")

class setup:
    """
    Setup Your Linker File Here
    """
    def __init__(self, name, version, repository, folder, author):
        self.name = name
        self.version = version
        self.author = author
        self.repository = repository
        self.folder = folder
        
    def online(self):
        """
        Creates Your Linker File With A GitHub Repository
        """
        if self.repository == None:
            raise Exceptions.ArgError("Repository Can't Be None")
                
        fh = open(f"{self.name}.linker",'w')
        try:
            fh.write(f"Name,{self.name}\n")
            fh.write(f"Version,{self.version}\n")
            fh.write(f"Repository,{self.repository}\n")
            fh.write(f"Author,{self.author}")
            fh.close()
        except:
            raise Exceptions.LinkerBuildError("Error Building Linker File")
        print(f"Linker '{self.name}' Created")

    def local(self):
        """
        If You Don't Have A GitHub Repo, You Can Use A Zip File. 
        
        However, You May Not Be Able To Install Updates With This Method.
        """
        if self.folder == None:
            raise Exceptions.ArgError("Folder Can't Be None")

        def zipdir(path, ziph):
            for root, dirs, files in os.walk(path):
                for file in files:
                    ziph.write(os.path.join(root, file))
            ziph.write("temp.linkinfo")

        try:
            temp = [f"{self.folder}/.linker", "temp.linkinfo"]
            for i in temp:
                fh = open(i,'w')
                fh.write(f"Name,{self.name}\n")
                fh.write(f"Version,{self.version}\n")
                fh.write(f"Folder,{self.folder}\n")
                fh.write(f"Author,{self.author}")
                fh.close()
        
        except FileNotFoundError:
            raise Exceptions.LinkerBuildError("Error Building Linker File, Does Folder Exist?")

        zipf = zipfile.ZipFile(f'{self.name}.zip', 'w', zipfile.ZIP_DEFLATED)
        zipdir(self.folder, zipf)
        zipf.close()
        print(f"Linker {self.name} created")

class Linker:
    def __init__(self, name, directory, prompt=True):
        """
        Manage Installations And Linker Files
        """
        self.name = name
        self.directory = directory
        self.prompt = prompt

        try:
            with open(f"{self.name}.linker", 'r') as r:
                info = []
                reader = csv.reader(r)
                for line in reader:
                    info.append(line[1])

        except FileNotFoundError:
            with zipfile.ZipFile(f"{self.name}.zip",'r') as r:
                r.extract("temp.linkinfo")

            with open("temp.linkinfo", 'r') as r:
                info = []
                reader = csv.reader(r)
                for line in reader:
                    info.append(line[1])

        self.actname = info[0]
    
    def online(self):
        """
        Downloads And Installs The Repository Using The Linker File
        """
        fh = open(f"{self.name}.linker",'r')
        reader = csv.reader(fh)
        info = []
        try:
            for line in reader:
                info.append(line[1])
        except:
            raise Exceptions.LinkerReadError("Error Reading Linker File. Is It Properly Formatted?")

        if os.path.exists(info[0]):
            if self.prompt == True:
                sendprompt(info[0], info[2], None, self.directory)
        
        else:
            os.system(f'git clone {info[2]} "{self.directory}/{info[0]}"')

        print(f"'{info[0]}' Created")
    
    def local(self):
        """
        Extracts And Installs The Program Using The Zip File
        """
        if self.name.endswith(".zip"):
            self.name = self.name.split(".")[0]
        try:
            with zipfile.ZipFile(f"{self.name}.zip", 'r') as r:
                try:
                    os.system("del temp.linkinfo")
                except:
                    pass
                r.extract("temp.linkinfo")
                r.close()
            fh = open("temp.linkinfo",'r')
            reader = csv.reader(fh)
            info = []
            for line in reader:
                info.append(line[1])

            if os.path.exists(info[0]):
                if self.prompt == True:
                    sendprompt(info[0], None, info[2], self.directory)
            else:
                with zipfile.ZipFile(f"{self.name}.zip", 'r') as r:
                    r.extractall(str(os.path.dirname(self.name)))
                    try:
                        os.rename(info[2], info[0])
                        self.name = info[0]
                    except PermissionError:
                        print("Builder Was Prevented From Renaming Folder")

            print("Interface Created")

        except FileNotFoundError:
            raise Exceptions.LinkerReadError("Could Not Find Linker File")

    def uninstall(self):
        """
        Removes The Installed Interface
        """
        if self.prompt == True:
            check = input(f"Are You Sure You Want To Uninstall {self.name}? (Y/N): ")

            if check == "Y":
                os.system(f"rmdir /Q /S {self.name}")
                print(f"Successfully Uninstalled {self.name}")
            
            elif check == "N":
                return
            
            else:
                print("Incorrect Answer Passed: Skipped Uninstallation")
                
        else:os.system(f"rmdir /Q /S {self.name}")

    def start(self, filename):
        """
        Starts The Program
        """
        os.startfile(f"{self.directory}/{self.name}/{filename}")

    def version(self):
        """
        Returns The Version Of The Linker File
        """
        try:
            with open(f"{self.name}.linker",'r') as r:
                info = []
                reader = csv.reader(r)
                for line in reader:
                    info.append(line[1])
                
            return info[1]
        
        except FileNotFoundError:
            with zipfile.ZipFile(f"{self.name}.zip", 'r') as r:
                r.extract("temp.linkinfo")
                r.close()
            
            with open("temp.linkinfo",'r') as r:
                info = []
                reader = csv.reader(r)
                
                for line in reader:
                    info.append(line[1])
            
            return info[1]