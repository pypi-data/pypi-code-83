from termcolor import cprint

from tools.OJ.CP.add_test import CpAddTest
from tools.OJ.CP.bruteforce import CpBruteforce
from tools.OJ.CP.contest import CpContest
from tools.OJ.CP.extension import CpExt
from tools.OJ.CP.help import help_keys, args_help
from tools.OJ.CP.login import CpLogin
from tools.OJ.CP.problem import CpProblem
from tools.OJ.CP.setup import CpSetup
from tools.OJ.CP.submit import CpSubmit
from tools.OJ.CP.test import CpMyTester, CpTest
from tools.OJ.CP.url_manager import CpUrlManager
from tools.run_program import if_run_type

cp_keys = ['-cp', '-Cp']


def cp_manager(msg):
    """
    It takes command and initialize operations according to the command
    :param msg:
    :return:
    """
    status = ''
    msg = msg.lower()
    ar = msg.split(sep=' ')

    if if_run_type(msg):
        pass

    elif 'dev' in ar or 'dev' in ar:
        obj = CpExt()
        obj.link()
    elif 'parse' in ar or 'listen' in ar:
        obj = CpExt()
        if 'link' in ar:
            obj.link()
        elif 'id' in ar:
            obj.id()
        elif 'contest' in ar:
            obj.parse_contest()
        else:
            obj.listen()
        status = '$SHELL'
    elif 'problem' in ar:
        obj = CpProblem()
        obj.fetch_problem()
    elif 'submit' in ar:
        msg = msg.replace('submit', '')
        msg = msg.replace(' ', '')
        obj = CpSubmit()
        obj.find_files(msg)
    elif '-t' in ar or 'template' in ar:
        msg = msg.replace('-t', '')
        msg = msg.replace('template', '')
        msg = msg.split()

        if (len(msg)) == 0:
            msg = 'sol.cpp'
        else:
            msg = msg[0]

        obj = CpSetup()
        obj.template(file_name=msg)

    elif 'contest' in ar:
        obj = CpContest()
        obj.parse_contest()

    elif 'login' in ar:
        obj = CpLogin()
        obj.login()
    elif 'add' in ar:
        obj = CpAddTest()
        if '-e' in ar or '-editor' in ar:
            obj.open_editor = True
        obj.add_case()
    elif 'test-oj' in ar:
        msg = msg.replace('test -oj', '')
        msg = msg.replace(' ', '')
        obj = CpTest()
        obj.find_files(msg)
    elif 'test' in ar:
        msg = msg.replace('test', '')
        msg = msg.replace(' ', '')
        ns = False
        if '-ns' in msg:
            msg = msg.replace('-ns', '')
            ns = True
        obj = CpMyTester(ns)
        # obj.TLE = 1
        show = False
        debug_run = False
        if '-d' in ar:
            msg = msg.replace('-d', '')
            debug_run = True
        if '--show' in ar:
            msg = msg.replace('--show', '')
            show = True
        obj.find_files(msg, show, debug_run)
    elif 'setup' in ar:
        obj = CpSetup()
        obj.setup()
    elif 'brute' in ar:
        obj = CpBruteforce()
        obj.run()
    elif 'gen' in ar:
        obj = CpSetup()
        obj.gen_py()
    elif 'open' in ar:
        all_item = False
        if 'all' in ar:
            all_item = True
        obj = CpUrlManager()
        obj.open(all_item)
    elif 'stand' in ar or 'standing' in ar:
        obj = CpUrlManager()
        obj.stand()
    elif msg in help_keys:
        args_help()
    else:
        cprint('Arguments Error', 'red')
        args_help()

    return status


def if_cp_type(msg):
    """
    check whether given command is a cp type command
    :param msg:
    :return:
    """
    for key in cp_keys:
        if key in msg:
            msg = msg.replace(key, '')
            cp_manager(msg.lower())
            return True
    return False
