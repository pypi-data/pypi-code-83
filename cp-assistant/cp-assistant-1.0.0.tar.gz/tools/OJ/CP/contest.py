import json
import os
import subprocess
import time

from termcolor import cprint


class CpContest:

    @staticmethod
    def fetch_problem(url=''):
        try:
            cmd = 'oj-api get-problem ' + url
            cmd = list(cmd.split())

            cp = subprocess.run(cmd, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            problem = json.loads(cp.stdout)

            if problem['status'] == 'ok':
                try:
                    alphabet = problem['result']['context']['alphabet']
                except:
                    alphabet = ''
                problem_name = problem['result']['name']
                problem_name = alphabet + '-' + problem_name

                if not os.path.isdir(problem_name):
                    os.mkdir(problem_name)
                try:
                    result = f"  * Fetched '{problem_name}'' Successfully"
                    testcases = problem['result']['tests']

                    base = os.getcwd()
                    path = os.path.join(base, problem_name, "")

                    info = '{"name" : "$NAME" , "url" : "$URL" }'

                    info = info.replace('$NAME', problem_name)
                    info = info.replace('$URL', url)

                    with open(path + '.info', 'w') as f:
                        f.write(info)

                    if not os.path.isdir(path + "testcases"):
                        os.mkdir(path + "testcases")
                    path = os.path.join(path, 'testcases')
                    no = 1
                    for case in testcases:
                        file_name_in = 'Sample-' + str(no).zfill(2) + '.in'
                        file_name_out = 'Sample-' + str(no).zfill(2) + '.out'

                        no += 1
                        with open(os.path.join(path, file_name_in), 'w') as fin:
                            fin.write(case['input'])
                        with open(os.path.join(path, file_name_out), 'w') as f_out:
                            f_out.write(case['output'])
                    cprint(result, 'green')

                except Exception as e:
                    print(e)

            else:
                result = "Wrong url."
                cprint(result, 'result')

        except:
            print('-' * 55)
            cprint("Sorry Can't Fetch.", 'red')

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
            # with open('problem.json','w') as f:
            #     f.write(cp.stdout)

            result = "\tFetched Contest info..."
            if contest['status'] == 'ok':
                cprint(result, 'green')
            else:
                cprint("Sorry contest can't be fetched. Sorry sir. :( ", 'red')
                return

            path = os.getcwd()

            contest_name = contest['result']['name']
            cprint(f' # Contest name : {contest_name}', 'green')

            if not os.path.isdir(contest_name):
                os.mkdir(contest_name)

            print()
            os.chdir(os.path.join(path, contest_name))

            problem = contest['result']['problems']
            with open('t.json', 'w') as f:
                f.write(str(contest))

            for key in problem:
                url = key['url']

                self.fetch_problem(url=url)

            os.chdir(path)

            print()
            cprint(" # Done. :D", 'green')
            cprint(f" # Time taken {time.time() - t:.4f} sec.", 'blue')
            cprint('-' * 55, 'magenta')

        except Exception as e:
            cprint(e, 'red')
