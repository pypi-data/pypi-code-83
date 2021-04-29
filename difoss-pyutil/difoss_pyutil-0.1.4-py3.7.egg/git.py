#!python3
# -*- coding:utf-8 -*-
# author: difosschan
#
__all__ = (
    'is_git_dir',
    'is_git_file',
    'GitRepository',
)

import os
import sys
import json
from git import Repo
from git.refs.head import Head
from typing import List, Union

def is_git_dir(git_dir):
    """From git's setup.c:is_git_directory()."""
    result = False
    if git_dir:
        headref = os.path.join(git_dir, 'HEAD')

        if (os.path.isdir(git_dir) and
                (os.path.isdir(os.path.join(git_dir, 'objects')) and
                 os.path.isdir(os.path.join(git_dir, 'refs'))) or
                (os.path.isfile(os.path.join(git_dir, 'gitdir')) and
                 os.path.isfile(os.path.join(git_dir, 'commondir')))):

            result = (os.path.isfile(headref) or
                     (os.path.islink(headref) and
                      os.readlink(headref).startswith('refs/')))
        else:
            result = is_git_file(git_dir)

    return result


def is_git_file(f):
    return os.path.isfile(f) and os.path.basename(f) == '.git'


class GitRepository(object):
    """
    git仓库管理
    """
    def __init__(self, local_path, repo_url, **kwargs):
        self.local_path = local_path
        self.repo_url = repo_url
        self.repo: Union[Repo,None] = None
        self.initial(repo_url, **kwargs)

    def initial(self, repo_url, **kwargs):
        """
        初始化git仓库
        :param repo_url:
        :return:
        """
        if not os.path.exists(self.local_path):
            os.makedirs(self.local_path)

        git_local_path = os.path.join(self.local_path, '.git')
        if not is_git_dir(git_local_path):
            self.repo = Repo.clone_from(repo_url, to_path=self.local_path, **kwargs)
        else:
            self.repo = Repo(self.local_path, **kwargs)

    def pull(self):
        """
        从线上拉最新代码
        :return:
        """
        self.repo.git.pull()

    def push(self, refspec, name='origin', **kwargs):
        self.repo.remote(name).push(refspec=refspec, **kwargs)

    def branches(self):
        """
        获取所有分支
        :return:
        """
        l = [str(x).strip('\t *') for x in self.repo.git.branch('-a').split('\n')]
        lenOf = len('remotes/origin/')
        return [ x[lenOf:] if x.startswith('remotes/origin/') else x for x in l if not x.startswith('remotes/origin/HEAD')]
        # return [item.remote_head
        #         for item in self.repo.remote().refs
        #         if item.remote_head not in ('HEAD', )]

    def get_current_branch(self) -> Head:
        return self.repo.active_branch

    def commits(self):
        """
        获取所有提交记录
        :return:
        """
        commit_log = self.repo.git.log(
            '--pretty={"commit":"%h","author":"%an","date":"%cd"}|%s',
            date='format:%Y-%m-%d %H:%M')
        log_list: List[str] = [ x for x in commit_log.split("\n")]
        objects = []
        for log in log_list:
            v = log.split('|', maxsplit=1)
            o = {}
            try:
                o = json.loads(v[0])
                o['summary'] = v[1]
            except:
                o['error'] = True
                o['origin'] = log
            objects.append(o)

        return objects

    def tags(self):
        """
        获取所有tag
        :return:
        """
        return [tag.name for tag in self.repo.tags]

    def change_to_branch(self, branch, **kwargs):
        """
        切换分值
        :param branch:
        :return:
        """
        self.repo.git.checkout(branch, **kwargs)

    def change_to_commit(self, branch, commit):
        """
        切换commit
        :param branch:
        :param commit:
        :return:
        """
        self.change_to_branch(branch=branch)
        self.repo.git.reset('--hard', commit)

    # about config ---------------------------------------------------------------------------
    def get_config_value(self, section, option, default=None, config_level=None):
        """获取 git 配置值"""
        return self.repo.config_reader(config_level).get_value(section, option, default)

    def get_config_values(self, section, option, default=None, config_level=None):
        """获取 git 配置值"""
        return self.repo.config_reader(config_level).get_values(section, option, default)

    def set_config_value(self, section, option, value, config_level="repository"):
        return self.repo.config_writer(config_level).set_value(section, option, value)

    def get_config_sections(self, config_level=None):
        return self.repo.config_reader(config_level).sections()

    def get_config_options(self, section, config_level=None):
        return self.repo.config_reader(config_level).options(section)
    # ----------------------------------------------------------------------------------------
