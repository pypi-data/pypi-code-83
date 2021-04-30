import os
import hashlib
from setuptools import setup, find_packages


def calculate_checksum(filenames):
    hash = hashlib.md5()
    for fn in filenames:
        if os.path.isfile(fn):
            hash.update(open(fn, "rb").read())
    return hash.digest()
def md5_for_files(folder):
    files = os.listdir(folder)
    filenames=[]
    for each in files:
        if each.endswith('.py') or each.endswith('.sh'):
            filenames.append(each)
    print(filenames)
    result=calculate_checksum(filenames)

    print(result)
    
    with open(folder+'/'+'chk_sum.md5',"wb") as outfile:
        outfile.write(result)

    with open(folder+'/'+'chk_sum.md5',"rb") as inputfile:
        readBack=inputfile.read()
        print(readBack)
    
md5_for_files('./spotii/launcher')
    
# __packages__ = find_packages(
#     where = 'spotii_project',
# #    include = ['define*',],
# #    exclude = ['additional',]
#     )
#__packages__ = ['spotii'] + __packages__
__packages__=['spotii','spotii.guifolder','spotii.communication','spotii.on_off','spotii.test_handler']
#__packages__=['spotii']
print(__packages__)


# _ROOT = os.path.abspath(os.path.dirname(__file__))
# def get_data(path):
#     return os.path.join(_ROOT, 'data', path)

#print get_data('resource1/foo.txt')
setup(
    name = "spotii",
    version = "0.0.11",
    description = "a demo",
    author = 'gxf',
    author_email = 'feng.gao@laipac.com',
    url = 'https://github.com/gxfca/gitTest',
    packages = __packages__,
#    package_dir ={'spoitii':'spotii'},
    package_data={
        'spotii':['guifolder/png/slot/*',
                  'guifolder/png/slot/detecting/*',
                  'guifolder/png/slot/invalid/*',
                  'guifolder/png/slot/negative/*',
                  'guifolder/png/slot/positive/*',
                  'guifolder/png/slot/warning/*',
                  'guifolder/png/title/*',
                  'launcher/*',
                  ],
                  },
    entry_points={
    'console_scripts': [
        'spotii=spotii.__main__:spot_main',
    ],
    },
    )
