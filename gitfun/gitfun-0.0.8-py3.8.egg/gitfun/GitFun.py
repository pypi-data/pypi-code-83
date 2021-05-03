import subprocess



def init_push(url:str) -> str:
    """

    :param url:str, required
    The url is passed to add a remote repo link for the git
    :return:
    str  subprocess.run("git push --set-upstream origin master ")
    which pushes all the changes to repo
    """


    commit_message = "initial Commit"
    subprocess.run("git init")
    subprocess.run("git remote add origin %s") % (url)
    subprocess.run("git add .")
    subprocess.run("git commit -m %s")%(commit_message)
    return subprocess.run("git push --set-upstream origin master ")









def remote(url:str) -> str:
    subprocess.run("git add remote origin",url)
    return "remote add"
