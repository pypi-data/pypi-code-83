import json
import os

from termcolor import cprint


class CpSubmit:
    from settings.compiler import cf_tool_mode

    @staticmethod
    def cf_url(url):
        codeforces = 'codeforces.com'
        if codeforces in url:
            return True
        else:
            return False

    @staticmethod
    def cf_submit(submission_id, file_name):

        pt = '-' * 22 + 'Cf tool' + '-' * 22
        cprint(pt, 'magenta')

        cmd = 'cf submit ' + submission_id + ' ' + file_name
        done = os.system(cmd)

        cprint(len(pt) * '-', 'magenta')

        return True if done == 0 else False

    def cf_submit_manager(self, url, file_name=''):
        url = url.split(sep='/')
        submission_id = url[-3] + ' ' + url[-1]

        return self.cf_submit(submission_id, file_name)

    @staticmethod
    def cf_id_from_cwd():
        try:
            curr_path = os.getcwd()
            problem_id = curr_path.split(sep='/')
            problem_id = problem_id[-2] + ' ' + problem_id[-1]
            return problem_id
        except:
            return ''

    @staticmethod
    def check_cf_id(id):
        try:
            id = id.split(' ')
            if len(id) != 2:
                return False
            x = int(id[0])
            y = id[1]
            return True
        except:
            cprint('not cf id', 'red')
            return False

    def cf_submit_from_cwd(self, file_name=''):

        try:
            if not self.cf_tool_mode:
                return False

            submission_id = self.cf_id_from_cwd()

            if self.check_cf_id(submission_id):
                self.cf_submit(submission_id, file_name)
                return True

            return False

        except:
            return False

    def submit_it(self, file_name):
        try:
            with open('.info', 'r') as f:
                info = f.read()
            info = json.loads(info)
            problem_name = info['name']
            url = info['url']
        except:
            if self.cf_submit_from_cwd():
                return
            cprint("Enter the problem url : ", 'cyan', end='')
            url = input()
            problem_name = url
        pt = '-' * 20 + 'Problem Description' + '-' * 20
        cprint(pt, 'magenta')
        cprint(' ' * 4 + 'Problem : ', 'yellow', end='')
        cprint(problem_name, 'green')
        cprint(' ' * 4 + 'Problem url: ', 'yellow', end='')
        cprint(url, 'green')
        cprint(' ' * 4 + 'File name: ', 'yellow', end='')
        cprint(file_name, 'green')
        cprint('-' * len(pt), 'magenta')
        cprint('Enter (y/n) to confirm : ', 'yellow', attrs=['bold'], end='')
        x = input()
        if x.lower() == 'y' or x.lower == 'yes':
            cprint('Submitting...', 'green')
            submitted = False
            if self.cf_tool_mode == True and self.cf_url(url):
                submitted = self.cf_submit_manager(url, file_name)

            if not submitted:
                cmd = 'oj submit --wait=0 --yes $URL $FILENAME'
                cmd = cmd.replace('$URL', url)
                cmd = cmd.replace('$FILENAME', file_name)
                os.system(cmd)
        else:
            cprint('Submitting Cancelled.', 'red')

    def find_files(self, file_name=''):
        cprint(' ' * 17 + '...Submitting Problem...' + '\n', 'blue')
        file_list = []
        # print(f'FIle name is {file_name}')
        supported_ext = ['cpp', 'py']
        for file in os.listdir(os.getcwd()):
            try:
                ext = file.rsplit(sep='.', maxsplit=1)
                for i in supported_ext:
                    if ext[1] == i:
                        if file_name in file:
                            file_list.append(file)
            except:
                pass

        sz = len(file_list)
        if sz == 1:
            self.submit_it(file_list[0])
        elif sz > 1:
            no = 1
            cprint("All the available files are given below.\n", 'yellow')
            for file in file_list:
                pt = (' ' * 4 + str(no) + ') ' + file)
                cprint(pt, 'blue')
                no += 1
            cprint(' ' * 4 + '0) Cancel operation', 'red')
            print()
            while True:
                cprint("Select the file number : ", 'cyan', end='')
                index = int(input())
                if index == 0:
                    cprint("Submitting operation cancelled.", 'red')
                    break
                elif index < no:
                    self.submit_it(file_list[index - 1])
                    break
                else:
                    cprint("You have entered the wrong index.Please try again.", 'red')
        else:
            cprint("NO FILE FOUND :(", 'red')
