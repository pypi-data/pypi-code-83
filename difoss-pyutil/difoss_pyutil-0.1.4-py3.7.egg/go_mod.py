#!python3
# -*- coding:utf-8 -*-
# author: difosschan
#
import re
from typing import List, Union

all = (
    'get_requires',
    'get_replaces',
    'get_module',
    'get_go_version',
    'join_require',
    'join_replace',
    'join_go_mod',
)

# Reference: https://golang.org/ref/mod#go-list-m
#
# type Module struct {
#     Path      string       // module path
#     Version   string       // module version
#     Versions  []string     // available module versions (with -versions)
#     Replace   *Module      // replaced by this module
#     Time      *time.Time   // time version was created
#     Update    *Module      // available update, if any (with -u)
#     Main      bool         // is this the main module?
#     Indirect  bool         // is this module only an indirect dependency of main module?
#     Dir       string       // directory holding files for this module, if any
#     GoMod     string       // path to go.mod file for this module, if any
#     GoVersion string       // go version used in module
#     Error     *ModuleError // error loading module
# }
#  ... ...
# type Module struct {
#         Path string
#         Version string
# }
#
# type GoMod struct {
#         Module  Module
#         Go      string
#         Require []Require
#         Exclude []Module
#         Replace []Replace
# }
#
# type Require struct {
#         Path string
#         Version string
#         Indirect bool
# }
#
# type Replace struct {
#         Old Module
#         New Module
# }

def pick_up_from_go_mod(content: str, keyword: str, pattern: re.Pattern, allow_bracket: bool = True) -> List[dict]:

    module_lines = []

    if allow_bracket:
        PATTERN_IN_BRACKETS = re.compile(r'%s\s*\((.*?)\)' % (keyword), re.DOTALL)
        requires_in_bracket = PATTERN_IN_BRACKETS.findall(content)
        for rib in requires_in_bracket:
            spList = rib.split('\n')
            for line in spList:
                line = line.strip('\t \n')
                if line:
                    module_lines.append(line)

    PATTERN_SINGLE_LINE = re.compile(r'%s\s+([^(]+)' % (keyword))
    content_lines = content.split('\n')
    for line in content_lines:
        line = line.strip('\t \n')
        if line:
            m = PATTERN_SINGLE_LINE.match(line)
            if m:
                group = m.groups()
                if group:
                    module_lines.append(group[0])

    modules = []
    for info in module_lines:
        m = pattern.match(info)
        if m:
            modules.append(m.groupdict())

    return modules


def get_requires(content: str) -> List[dict]:
    return pick_up_from_go_mod(
        content, 'require',
        re.compile(r'(?P<repository>\S+)\s+'
                   r'(?P<whole_version>\S*(?P<version>v[^-/\s]+)\S*)'
                   r'\s*(?P<indirect>//.*)?'
                   ))


def get_replaces(content: str) -> List[dict]:
    return pick_up_from_go_mod(
        content, 'replace',
        re.compile(r'(?P<repository>\S+)(\s+(?P<version>v\S+))?'
                   r'\s*=>\s*'
                   r'(?P<new_repository>\S+)(\s+(?P<new_version>v\S+))?'
                   ))


def get_module(content: str) -> str:
    module = pick_up_from_go_mod(
        content, 'module',
        re.compile(r'(?P<repository>\S+)'), False)
    if not module:
        return ''

    return module[0].get('repository', '')


def get_go_version(content: str) -> str:
    go_version = pick_up_from_go_mod(
        content, 'go',
        re.compile(r'(?P<version>\d+\.\d+)', False)
    )
    if not go_version:
        return ''
    return go_version[0].get('version', '')


def join_require(require: dict) -> str:
    return ' '.join([x for x in [
        require.get('repository'),
        require.get('whole_version'),
        require.get('indirect'),
    ] if x ] )


def join_replace(replace: dict) -> str:
    return ' '.join([x for x in [
        replace.get('repository'),
        replace.get('version'),
        '=>',
        replace.get('new_repository'),
        replace.get('new_version'),
    ] if x ] )


def join_go_mod(module: str,
                requires: List[dict],
                go_version: Union[str, float, None] = None,
                replaces: List[dict] = None) -> str:

    require_lines = [ join_require(x) for x in requires ]
    replace_lines = [ join_replace(x) for x in replaces ]

    return ('\n' * 2).join([ x for x in  [
        f'module {module}',
        "\n\t".join(['require (', *require_lines]) + '\n)' if replaces else None,
        f'go {go_version}' if go_version else None,
        "\n\t".join(['replace (', *replace_lines]) + '\n)' if replaces else None,
    ] if x ] )
