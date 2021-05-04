class skyway:
    def __init__(self):
        global f, content, project_name, project_version
        f = open('./skyway/skyway/config.sky', "r")
        project_namefinder = f.readline()
        project_versionfinder = f.readline()
        f.close()
        project_namefinder.find('PROJECT_NAME =')
        project_versionfinder.find('PROJECT_VERSION =')
        project_name = project_namefinder.split(' ')[2]
        project_versionfinder.find('PROJECT_VERSION =')
        project_version = project_versionfinder.split(' ')[2]

    def read(self, targetdir, file):
        self.dir = targetdir
        self.file = file
        file = open(targetdir + file, "r")
        echofinder = file.readlines()
        file.close()
        i = 0
        for i in echofinder:
            echofinder.remove("\n")
            echofinder.remove("\n")

        for i2 in echofinder:
            print(echofinder[echofinder.index(i2)].split('"')[1])


