from system.platform import get_platform
from tools.OJ.CP.setup import CpSetup

import os
import subprocess
import json
from termcolor import cprint
import time
import threading
import socket
from settings.compiler import competitive_companion_port, parse_problem_with_template
from settings.compiler import editor

editor_file_path = []
editor_file_name = []


class CpExt:
    HOST = '127.0.0.1'
    PORT = competitive_companion_port
    PARSED_URL = []
    NOT_FINISHED = True

    @staticmethod
    def template(file_path, file_name='sol.cpp', open_editor=False):
        try:

            obj_template = CpSetup()
            obj_template.template(file_path, file_name, parsingMode=True, open_editor=open_editor)
            return
        except:
            return

    @staticmethod
    def rectify(s):
        try:
            i = s.find('{')
            s = s[i:]
            return s
        except:
            return ''

    def create(self, problem, cnt=0, link=False):
        try:
            problem = self.rectify(problem)
            dic = json.loads(problem)
            if dic['url'] in self.PARSED_URL:
                return
            self.PARSED_URL.append(dic['url'])
            if link:
                dic = dic['result']

            problem_name = dic['name']
            try:
                contest_name = dic['group']
            except:
                contest_name = 'NULL'
            url = dic['url']
            problem_time_limit = 'NULL'
            problem_memory_limit = 'NULL'
            try:
                problem_time_limit = str(dic['timeLimit']) + ' ms'
                problem_memory_limit = str(dic['memoryLimit']) + ' MB'
            except Exception as e:
                cprint(e, 'red')
                pass
            base = os.getcwd()
            base_name = os.path.basename(base)

            contest_path = os.path.join(base, contest_name)

            if contest_name != 'NULL':
                contest_path = self.get_contest_path(base, contest_name)

            if contest_name != 'NULL':
                try:
                    if cnt == 0:
                        if not os.path.isdir(contest_name):
                            os.mkdir(contest_name)
                            cprint(f" Folder {contest_name} is created.", 'blue')
                            info = '{"contest_name" : "$CONTEST" , "url" : "$URL"}'
                            info = info.replace('$CONTEST', contest_name)
                            info = info.replace('$URL', url)
                            with open(os.path.join(contest_path, '.info'), 'w') as f:
                                f.write(info)
                        cprint(f" All the problems will be parsed into '{contest_name}' folder.\n", 'magenta')
                except Exception as e:
                    print(e)
                os.chdir(contest_path)

            if not os.path.isdir(problem_name):
                os.mkdir(problem_name)

            info = '{"name" : "$NAME" , "url" : "$URL","timeLimit" : "$timeLimit" , "memoryLimit":"$memoryLimit"}'

            info = info.replace('$NAME', problem_name)
            info = info.replace('$URL', url)
            info = info.replace('$memoryLimit', problem_memory_limit)
            info = info.replace('$timeLimit', problem_time_limit)

            path = os.path.join(os.getcwd(), problem_name, "")

            with open(path + '.info', 'w') as f:
                f.write(info)

            if parse_problem_with_template:
                open_editor = False
                if cnt == 0:
                    open_editor = True
                self.template(path, open_editor=open_editor)

            testcases = dic['tests']

            no = 1
            if not os.path.isdir(path + "testcases"):
                os.mkdir(path + "testcases")
            path = os.path.join(path, 'testcases')

            for case in testcases:
                file_name_in = 'Sample-' + str(no).zfill(2) + '.in'
                file_name_out = 'Sample-' + str(no).zfill(2) + '.out'

                no += 1
                with open(os.path.join(path, file_name_in), 'w') as fin:
                    fin.write(case['input'])
                with open(os.path.join(path, file_name_out), 'w') as f_out:
                    f_out.write(case['output'])

            cprint(f'  {problem_name} fetched successfully.', 'green')
            os.chdir(contest_path)

        except Exception as e:
            cprint(e, 'red')

    def time_out(self, target_time):
        time.sleep(target_time)
        self.NOT_FINISHED = False

    def listen(self):

        cprint(' ' * 17 + '...Parsing Problem...' + ' ' * 17, 'blue')
        print()
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.HOST, self.PORT))
            cprint(" Listening (Click competitive companion extension)....", 'yellow')
            print()
            timeout = 1000
            cnt = 0
            ok = True
            while ok and self.NOT_FINISHED:
                try:
                    s.listen()
                    s.settimeout(timeout)
                    timeout = 2
                    conn, addr = s.accept()
                    with conn:
                        problem_json = ''
                        continue_loop = True
                        while continue_loop and self.NOT_FINISHED:
                            data = conn.recv(1024)
                            result = (data.decode('utf-8'))

                            if not data:
                                if problem_json == '':
                                    break
                                t = threading.Thread(target=self.create, args=(problem_json, cnt))
                                t.start()
                                cnt += 1
                                continue_loop = False
                                ok = False
                            else:
                                problem_json += result
                                pass

                except Exception as e:
                    # print(e)
                    ok = False

        print()
        t.join()
        cprint(f' # Total {cnt} problems is fetched.', 'blue')

        if cnt > 0 and editor != '$NONE':
            cli_editors = ['nvim', 'vim', 'nano']
            if editor not in cli_editors:
                os.system(editor + ' .')
            base = os.getcwd()
            for file_path, file_name in zip(editor_file_path, editor_file_name):
                os.chdir(file_path)
                os.system(editor + ' ' + file_name)
            os.chdir(base)

    def link(self):

        t = None
        cprint(' ' * 17 + '...Parsing Problem...' + ' ' * 17, 'blue')
        print()
        cprint(" Enter the link of the problem : ", 'cyan', end='')
        url = input()
        print()
        cnt = 0
        ok = True

        while ok:
            try:
                cmd = 'oj-api get-problem --compatibility ' + url
                cmd = list(cmd.split())

                problem_json = subprocess.run(cmd, universal_newlines=True, stdout=subprocess.PIPE,
                                              stderr=subprocess.PIPE)

                t = threading.Thread(target=self.create, args=(problem_json.stdout, cnt, True))
                t.start()
                ok = False
                cnt += 1
            except:
                ok = False

        print()
        t.join()
        print()
        cprint(f' # Total {cnt} problems is fetched.', 'blue')

    def id(self):

        t = None
        cprint(' ' * 17 + '...Parsing Problem...' + ' ' * 17, 'blue')
        print()
        cprint(" Enter the codeforces contest id : ", 'cyan', end='')
        contest_id = input()
        cprint(" Enter the codeforces problems id : ", 'cyan', end='')
        problems = input()
        problems = problems.split(sep=' ')
        url = 'https://codeforces.com/contest/$CONTEST_ID/problem/$PROBLEM_ID'
        url = url.replace('$CONTEST_ID', contest_id)
        rem = url
        print()
        cnt = 0

        for prob in problems:
            try:
                url = rem.replace('$PROBLEM_ID', prob)
                cmd = 'oj-api get-problem --compatibility ' + url
                cmd = list(cmd.split())

                problem_json = subprocess.run(cmd, universal_newlines=True, stdout=subprocess.PIPE,
                                              stderr=subprocess.PIPE)
                t = threading.Thread(target=self.create, args=(problem_json.stdout, cnt, True))
                t.start()
                cnt += 1
            except:
                cprint(" Invalid id : " + prob, 'red')

        print()
        t.join()
        print()
        cprint(f' # Total {cnt} problems is fetched.', 'blue')

    def parse_contest(self, url=''):
        try:

            cprint(' ' * 17 + '...Parsing Contest...' + ' ' * 17, 'blue')
            if url == '':
                cprint('Enter the url : ', 'cyan', end='')
                url = input()
            cprint('-' * 55, 'magenta')
            # os.system(cmd)
            t = time.time()
            cmd = 'oj-api get-contest ' + url
            cmd = list(cmd.split())

            cp = subprocess.run(cmd, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            contest = json.loads(cp.stdout)

            result = "\tFetched Contest info..."
            if contest['status'] == 'ok':
                cprint(result, 'green')
            else:
                cprint("Sorry contest can't be fetched. Sorry sir. :( ", 'red')
                return
            problems = contest['result']['problems']

            cnt = 0

            for prob in problems:
                try:

                    url = prob['url']
                    cmd = 'oj-api get-problem --compatibility ' + url
                    cmd = list(cmd.split())

                    problem_json = subprocess.run(cmd, universal_newlines=True, stdout=subprocess.PIPE,
                                                  stderr=subprocess.PIPE)
                    t = threading.Thread(target=self.create, args=(problem_json.stdout, cnt, True))
                    t.start()
                    cnt += 1
                except:
                    cprint(" Invalid id : " + prob, 'red')

            print()
            t.join()
            print()
            cprint(f' # Total {cnt} problems is fetched.', 'blue')

        except Exception as e:
            cprint(e, 'red')

    @staticmethod
    def get_contest_path(base, contest_name):
        if get_platform() == 'Windows':
            sep = '\\'
        else:
            sep = '/'
        cnt = len(base.split(sep=sep))
        if cnt <= 2:
            return base
        base = base.rsplit(sep=sep, maxsplit=cnt - 2)
        contest_path = 'None'
        for b in base:
            if b == contest_name:
                break
            if not contest_path:
                contest_path = b
            else:
                contest_path = os.path.join(contest_path, b)

        contest_path = os.path.join(contest_path, contest_name)
        return contest_path
