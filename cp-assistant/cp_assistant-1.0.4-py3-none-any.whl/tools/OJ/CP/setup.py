import json
import os
import subprocess

from termcolor import cprint

from data.get_template import get_template
from settings.compiler import editor

editor_file_path = []
editor_file_name = []


class CpSetup:

    @staticmethod
    def sub_process(cmd):
        try:
            x = subprocess.Popen(cmd, stdout=subprocess.PIPE)
            result = (x.communicate()[0]).decode('utf-8')
        except:
            result = ''
        return result

    def gen_py(self):
        pass
        try:
            case_folder = ''
            if os.path.isdir('testcases'):
                case_folder = 'testcases'
            elif os.path.isdir('test'):
                case_folder = 'test'
            else:
                cprint(" testcases folder not available, Can't generate gen.py file. :(", 'red')
                return
            cmd = ['python3', '-m', 'tcgen', '--path', case_folder]
            result = self.sub_process(cmd)

            if result == '':
                cprint(" Can't generated gen file automatically. Sorry sir. :( ", 'red')
                return
            with open('gen.py', 'w') as f:
                f.write(result)
            cprint(' gen.py generated successfully, sir. :D', 'green')
        except Exception as e:
            print(e)
            cprint(" Sorry, Sir can't generate automatically gen file. ")

    @staticmethod
    def template(file_path='', file_name='sol.cpp', parsingMode=False, open_editor=False):
        try:
            from settings.compiler import template_path, coder_name
            from system.get_time import digital_time

            ext = file_name.rsplit(sep='.', maxsplit=1)
            if len(ext) == 1:
                ext = 'cpp'
                file_name = file_name + '.cpp'
            else:
                ext = ext[1]

            if ext == 'cpp':
                path = template_path['c++']
            elif ext == 'py':
                path = template_path['python']
            else:
                cprint(' File format not supported. Currently only support c++ and python.', 'red')
                path = ''
            try:
                f_name = file_name
                info_path = '.info'
                if file_path != '':
                    file_name = os.path.join(file_path, file_name)
                    info_path = os.path.join(file_path, info_path)

                if os.path.isfile(file_name):
                    if parsingMode:
                        return
                    cprint(f" {f_name} already exist, do you want to replace it?(Y/N) :", 'cyan', end='')
                    want = input()
                    want = want.lower()
                    if want != 'y' and want != 'yes':
                        cprint(f" {f_name} creation cancelled.", 'red')
                        return

                info_ase = False
                if os.path.isfile(info_path):
                    info_ase = True

                if path == '$DEFAULT':
                    if ext == 'py':
                        if info_ase:
                            code = get_template('py_template_info.txt')
                        else:
                            code = get_template('py_template.txt')
                    else:
                        if info_ase:
                            code = get_template('cpp_template_info.txt')
                        else:
                            code = get_template('cpp_template.txt')
                else:
                    with open(path, 'r') as f:
                        code = f.read()

                problem_name = '-X-'
                problem_url = '-X-'

                problem_time_limit = 'NULL'
                problem_memory_limit = 'NULL'
                try:
                    if info_ase:
                        with open(info_path, 'r') as f:
                            info = f.read()
                        info = json.loads(info)
                        problem_name = info['name']
                        problem_url = info['url']
                        problem_time_limit = info['timeLimit']
                        problem_memory_limit = info['memoryLimit']
                except:
                    pass

                code = code.replace('$%CODER%$', coder_name)
                code = code.replace('$%DATE_TIME%$', digital_time())
                code = code.replace('$%PROBLEM_NAME%$', problem_name)
                code = code.replace('$%PROBLEM_URL%$', problem_url)
                code = code.replace('$%TIMELIMIT%$', problem_time_limit)
                code = code.replace('$%MEMORYLIMIT%$', problem_memory_limit)

                with open(file_name, 'w') as f:
                    f.write(code)

                if open_editor and editor != '$NONE':
                    try:
                        base = os.getcwd()
                        filename_portion = file_name.rsplit(sep='/', maxsplit=1)
                        editor_file_path.append(filename_portion[0])
                        editor_file_name.append(filename_portion[1])
                    except Exception as e:
                        cprint(e, 'red')

                if not parsingMode:
                    cprint(f' {f_name} created successfully, sir. :D', 'green')
            except Exception as e:
                cprint(e, 'red')
                cprint("template path doesn't exist. Sorry sir.", 'red')
                cprint("check -config to change your template path :D .", 'yellow')
                return
        except Exception as e:
            cprint(e, 'red')
            cprint("Can't generate  template.", 'red')
            return

    @staticmethod
    def brute(file_name='brute.cpp'):
        try:
            if os.path.isfile(file_name):
                cprint(f" {file_name} already exist, do you want to replace it?(Y/N) :", 'cyan', end='')
                want = input()
                want = want.lower()
                if want != 'y' and want != 'yes':
                    cprint(f" {file_name} creation cancelled.", 'red')
                    return
            with open(file_name, 'w') as f:
                f.write('/* Bruteforce */\n')
            cprint(f' {file_name} created successfully, sir. :D', 'green')
        except:
            cprint(f" Can't create {file_name}", 'red')

    def setup(self, t_name='sol.cpp', brute_name='brute.cpp'):
        if not os.path.isfile(t_name):
            self.template()
        else:
            cprint(f" {t_name} exists.", 'green')
        if not os.path.isfile(brute_name):
            self.brute()
        else:
            cprint(f" {brute_name} exists.", 'green')
        self.gen_py()
        pass
