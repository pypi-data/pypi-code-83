import sh
import yaml
import logging
from pathlib import Path
from donno.config import get_attr, CONF_PATH


configs = get_attr()
HOMEPAGE_TEMP = CONF_PATH.parent / 'homepage.html'
NOTE_TEMP = CONF_PATH.parent / 'note.html'
LOCAL_REPO = 'blog_pages'
HOMEPAGE = 'index.html'
NOTE_FILES = Path(configs['repo']).glob('*.md')
TITLE_LINE_NO = 0  # zero based line number
TAG_LINE_NO = 1
NOTEBOOK_LINE_NO = 2
UPD_LINE_NO = 4
logger = logging.getLogger('blog')
logger.setLevel(logging.INFO if configs['logging_level'] == 'info'
                else logging.DEBUG)
ch = logging.StreamHandler()
ch.setFormatter(logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(ch)

NOTE_LIST_PATH = '/tmp/notes.yaml'


def create_web_page_list():
    page_home = Path(configs['app_home']) / LOCAL_REPO
    vcs = Path(configs['app_home']) / LOCAL_REPO / '.git'
    converted = {'note': []}
    if vcs.exists():
        # incremental sync, only notes updated since last blog commit will
        # be converted to blog pages
        # TODO
        pass
    else:
        logger.info('No VCS found in your blog folder.\n'
                    'A complete conversion will be performed')
        page_home.mkdir(exist_ok=True)
        nb = configs['blog.notebook']
        for note in NOTE_FILES:
            with open(note, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            if nb not in lines[NOTEBOOK_LINE_NO]:
                continue
            target = note.stem + '.html'
            note_yml = Path('/tmp') / note.name
            sh.sed(sh.sed(note, e="1 i ---"), e='7 i ---', _out=str(note_yml))
            sh.pandoc(note_yml, standalone=True, mathjax=True, toc=True,
                      template=NOTE_TEMP, output=str(page_home / target))
            converted['note'].append(
                {'title': lines[TITLE_LINE_NO].strip()[7:],
                 'tags': lines[TAG_LINE_NO].strip()[6:]
                 if len(lines[TAG_LINE_NO].strip()) > 7 else '',
                 'path': './' + target,
                 'updated': lines[UPD_LINE_NO].strip()[9:]})

    with open(NOTE_LIST_PATH, 'w', encoding='utf-8') as f:
        notesyml = yaml.dump(converted, default_flow_style=False,
                             allow_unicode=True)
        f.write(f'---\n{notesyml}---')

    sh.pandoc(NOTE_LIST_PATH, standalone=True, mathjax=True,
              template=HOMEPAGE_TEMP, output=str(page_home / HOMEPAGE))
