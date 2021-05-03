import json
import os
import webbrowser

from termcolor import cprint


class CpUrlManager:

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
            return True
        except:
            cprint('not cf id', 'red')
            return False

    def open_from_cwd(self):
        try:
            id = self.cf_id_from_cwd()

            if not self.check_cf_id(id):
                return False

            url = 'https://codeforces.com/contest/$CONTEST_ID/problem/$ALPHABET'
            id = id.split(sep=' ')
            url = url.replace('$CONTEST_ID', id[0])
            url = url.replace('$ALPHABET', id[1])

            webbrowser.open(url)
            cprint(' Check Browser.', 'yellow')
            return True

        except:
            return False

    def open(self, all=False):
        try:
            with open('.info', 'r') as f:
                info = f.read()
            info = json.loads(info)
            url = info['url']

            if all:
                if 'codeforces.com' in url:
                    lab = url.rsplit('/', maxsplit=1)
                    lab[-1] = ''
                    url = lab[0] + 's'
                elif 'atcoder.jp' in url:
                    lab = url.rsplit('/', maxsplit=1)
                    url = lab[0]

            webbrowser.open(url)
            cprint(' Check Browser.', 'yellow')

        except:
            if not self.open_from_cwd():
                cprint(" Can't find valid url.", 'red')

    def stand_from_cwd(self):
        try:
            id = self.cf_id_from_cwd()

            if not self.check_cf_id(id):
                return False

            stand_url = 'https://codeforces.com/contest/$CONTEST_ID/standings/friends/true'
            id = id.split(sep=' ')
            url = stand_url.replace('$CONTEST_ID', id[0])

            webbrowser.open(url)
            cprint(' Check Browser.', 'yellow')
            return True

        except Exception as e:
            print(e)
            return False

    @staticmethod
    def stand_open(url):

        if 'codeforces.com' in url:
            stand_url = 'https://codeforces.com/contest/$CONTEST_ID/standings/friends/true'
            id = url.split(sep='/')
            stand_url = stand_url.replace('$CONTEST_ID', id[-3])
            webbrowser.open(stand_url)
            cprint(' Check Browser.', 'yellow')

        elif 'atcoder.jp' in url:
            url = url.split(sep='/')
            url[-1] = ''
            url[-2] = 'standings'
            url = '/'.join(url)
            webbrowser.open(url)
            cprint(' Check Browser.', 'yellow')

        else:
            cprint(' Sorry sir, standing option has not implemented for this OJ.', 'red')

    def stand(self):

        try:
            with open('.info', 'r') as f:
                info = f.read()
            info = json.loads(info)
            url = info['url']

            self.stand_open(url)

        except:
            if not self.stand_from_cwd():
                cprint(" Can't find valid url.", 'red')
