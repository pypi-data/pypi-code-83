# -*- coding: utf-8 -*-
import subprocess


def uiautomator_run():
    r_push = subprocess.check_output(
        ['/usr/local/bin/adb',
         'shell',
         'rm',
         '-rf',
         '/storage/emulated/0/appQtp/exec_info/*'])

    print(r_push)


def list_packages():
    return subprocess.check_output(
        ['/usr/local/bin/adb', 'shell', 'pm', 'list', 'packages', '-3'])


def uninstall_pkg(pkg_name):
    return subprocess.check_output(['/usr/local/bin/adb', 'uninstall', pkg_name])


def install_pkg(apk_file):
    return subprocess.check_output(['/usr/local/bin/adb', 'install', '-r', apk_file])
