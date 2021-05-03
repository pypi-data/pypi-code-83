import os

from termcolor import colored as clr, cprint

from settings.compiler import editor
from system.platform import get_platform


class CpAddTest:
    """
     This class handles adding testcases
    """
    open_editor = False

    @property
    def take_input(self):
        content = ''
        while True:
            try:
                line = input()
            except EOFError:
                break
            content += line + '\n'

        return content

    @staticmethod
    def test_print(name, value):
        pt = '-' * 22 + name + '-' * 22
        cprint(pt, 'magenta')
        value = value.split(sep='\n')
        for x in value:
            x = '  ' + x
            print(x)

    def add_case(self, name='Custom-'):
        """  function for adding testcases """
        try:
            pt = '-' * 20 + '-' * 10 + '-' * 20
            cprint(pt, 'magenta')
            pt = (' ' * 17 + "...Adding Testcase..." + '\n')
            print(clr(pt, 'blue'))

            folder_name = 'testcases'
            if os.path.isdir(folder_name):
                pass
            elif os.path.isdir('test'):
                folder_name = 'test'
            else:
                os.mkdir(folder_name)

            path_name = os.path.join(os.getcwd(), folder_name)
            lt = os.listdir(path_name)
            ase = len(lt)
            no = int(ase / 2) + 1
            if not self.open_editor:
                if get_platform() == 'Windows':
                    way_to_stop = 'Press Ctrl+z and then press enter'
                else:
                    way_to_stop = 'Press Ctrl+d'
                cprint(f'Enter the input({way_to_stop}):', 'yellow')
                x = self.take_input

                cprint(f'Enter the output({way_to_stop}):', 'yellow')
                y = self.take_input
            else:
                x = ''
                y = ''

            filename_in = name + str(no).zfill(2) + '.in'
            filename_out = name + str(no).zfill(2) + '.out'
            print()
            if not self.open_editor:
                self.test_print(filename_in, x)
                self.test_print(filename_out, y)

                cprint('-' * 55, 'magenta')

                cprint("Do you want to add this testcase(y/n) :", 'cyan', end='')
                confirm = input().lower()

                positive = ['y', 'yes']
                if confirm not in positive:
                    cprint("Cancelled.", 'red')
                    return

            no += 1
            filename_in_path = os.path.join(path_name, filename_in)
            filename_out_path = os.path.join(path_name, filename_out)
            with open(filename_in_path, 'w') as fin:
                fin.write(x)
            with open(filename_out_path, 'w') as f_out:
                f_out.write(y)

            cprint('Testcase added Successfully. :D', 'green', attrs=['bold'])

            pt = '-' * 20 + '-' * 10 + '-' * 20
            cprint(pt, 'magenta')
            if self.open_editor and editor != '$NONE':
                os.system(editor + ' ' + filename_out_path)
                os.system(editor + ' ' + filename_in_path)
        except:
            cprint("Can't add testcase. :( ", 'red', attrs=['bold'])
