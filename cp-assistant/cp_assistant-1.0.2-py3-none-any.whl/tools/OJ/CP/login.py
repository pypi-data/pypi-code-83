import getpass
import json
import os

from termcolor import cprint

from settings.compiler import DEBUG


class CpLogin:

    @staticmethod
    def get_login_link():
        judges = [
            'Codeforces',
            'Atcoder',
            'HackerRank',
            'Others'
        ]
        links = {
            'Codeforces': 'https://codeforces.com/',
            'Atcoder': 'https://atcoder.jp/',
            'HackerRank': 'https://www.hackerrank.com/',
            'Toph': 'https://toph.co/',
        }

        print()
        for no, name in enumerate(judges):
            name = f' {no + 1} ) {name} '
            cprint(name, 'yellow')

        print()
        cprint(" Select the index : ", 'cyan', end='')
        index = int(input())
        if index < len(judges):
            value = judges[index - 1]

            print()
            cprint(f"\t\tJudge  : {value}", 'yellow')
            get_link = links.get(value, 'None')
        else:
            get_link = 'None'

        if get_link == 'None':
            print()
            cprint(' Enter judge link : ', 'cyan', end='')
            get_link = input()
            print()
            print()
            cprint(f"\tJudge link: {get_link}", 'yellow')

        return get_link

    def login(self):
        try:
            cprint(' ' * 17 + '...Log In Service...' + ' ' * 17, 'blue')

            oj = self.get_login_link()

            print()

            cli = False

            cli_available = [
                'codeforces.com',
                'atcoder.jp'
            ]

            for judge in cli_available:
                if judge in oj:
                    cprint(' Login using,', 'yellow')

                    print()
                    cprint('  1) Command line interface.', 'blue')
                    cprint('  2) Using browser (Need Webdriver installed in the system).', 'blue')
                    print()

                    cprint(' Enter the index no : ', 'cyan', end='')
                    index = int(input())

                    print()

                    if index == 1:
                        cli = True

            if cli:
                cprint(' Enter your username : ', 'cyan', end='')
                username = input()
                password = getpass.getpass(prompt=' Enter your password : ')
                cmd = "USERNAME=$USERNAME PASSWORD=$PASS oj-api login-service " + oj + '> .status'
                cmd = cmd.replace("$USERNAME", username)
                cmd = cmd.replace("$PASS", password)

            else:
                cmd = 'oj login ' + oj

            print()
            xt = '-' * 15 + 'Oj-Tools-Interface' + '-' * 15
            cprint(xt, 'magenta')
            print()
            os.system(cmd)
            print()
            cprint('-' * len(xt), 'magenta')
            print()

            if cli:
                with open('.status', 'r') as f:
                    cp = f.read()
                cp = json.loads(cp)
                if cp["result"]['loggedIn']:
                    cprint(" (^-^) Logged in successfully....", 'green')
                else:
                    cprint(" (-_-) Login failed. May be wrong wrong username or password.", 'red')
                os.remove('.status')

        except Exception as e:
            if DEBUG:
                cprint('Error : ' + str(e), 'red')
            cprint(" (^_^) Login failed. May be wrong wrong username or password.", 'red')
            pass
