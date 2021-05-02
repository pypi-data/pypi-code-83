import git
import os


def get_real_path(git_path, git_version, base_path):
    return base_path + os.sep + git_path[git_path.index(':') + 1:].replace('.git', '') + os.sep + git_version


def run(git_path, git_version, base_path):
    real_path = get_real_path(git_path, git_version, base_path)
    if not os.path.exists(real_path):
        os.makedirs(real_path)

    try:
        git.Repo(real_path)
    except git.InvalidGitRepositoryError:
        try:
            repo = git.Repo.clone_from(url=git_path, to_path=real_path)
            repo.git.checkout(git_version)
        except Exception:
            return False
    return True
