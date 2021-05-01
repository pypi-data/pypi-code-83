from termcolor import cprint

help_keys = ['-h', 'help']


def args_help():
    """All the available arguments are listed here"""
    pt = '-' * 18 + "cp command arguments" + '-' * 18
    cprint(pt, 'magenta')
    print()

    cprint('  -> parse : ', 'yellow', end='')
    cprint('To parse problem or contest via competitive companion extension', 'cyan')

    cprint('  -> listen : ', 'yellow', end='')
    cprint('To parse problem or contest via competitive companion extension', 'cyan')

    cprint('  -> test : ', 'yellow', end='')
    cprint('To test code against testcases', 'cyan')

    cprint('  -> add : ', 'yellow', end='')
    cprint('To add testcase', 'cyan')

    cprint('  -> brute : ', 'yellow', end='')
    cprint('To bruteforce solution', 'cyan')

    cprint('  -> gen : ', 'yellow', end='')
    cprint('To generate testcase generator', 'cyan')

    cprint('  -> setup : ', 'yellow', end='')
    cprint('To generate sol.cpp , brute.cpp and testcase generator', 'cyan')

    cprint('  -> -t "filename": ', 'yellow', end='')
    cprint('To generate "filename" from template', 'cyan')

    cprint('  -> login: ', 'yellow', end='')
    cprint('To login into online judge', 'cyan')

    cprint('  -> submit: ', 'yellow', end='')
    cprint('To submit problem', 'cyan')

    cprint('  -> problem : ', 'yellow', end='')
    cprint('To parse problem manually', 'cyan')

    cprint('  -> contest : ', 'yellow', end='')
    cprint('To parse contest manually', 'cyan')

    cprint('  -> open : ', 'yellow', end='')
    cprint('To open current problem in browser', 'cyan')

    cprint('  -> stand : ', 'yellow', end='')
    cprint('To open standing page in browser', 'cyan')

    print()
    cprint('-' * len(pt), 'magenta')
