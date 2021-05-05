# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['manim_livestream', 'manim_livestream.config']

package_data = \
{'': ['*']}

install_requires = \
['manim>=0.6']

extras_require = \
{':python_version >= "3.7" and python_version < "4.0.0"': ['ipython>=7.22.0,<8.0.0'],
 ':sys_platform == "win32"': ['pyreadline>=2.1,<3.0']}

entry_points = \
{'manim.plugins': ['manim_livestream = manim_livestream']}

setup_kwargs = {
    'name': 'manim-livestream',
    'version': '0.0.1',
    'description': 'Package that implements livestreaming configurations for Manim.',
    'long_description': '# Manim Livestream\n\nThis plugin is designed to enable livestreaming support for [Manim](https://www.manim.community/). \n## Installation\n\nWorks like other packages, so pip will do fine\n\n``` {.sourceCode .bash}\npip install manim-livestream\n```\n\n\n## Usage\n\n- Run the following command:\n\n```bash\npython -m manim_livestream\n```\n\nThis loads a python shell along with the usage information:\n\n```bash\nManim is now running in streaming mode. Stream animations by passing\nthem to self.play(), e.g.\n\n>>> c = Circle()\n>>> self.play(ShowCreation(c))\n\nThe current streaming class under the name `manim` inherits from the\noriginal Scene class. To create a streaming class which inherits from\nanother scene class, e.g. MovingCameraScene, create it with the syntax:\n\n>>> self2 = get_streamer(MovingCameraScene)\n\nTo view an image of the current state of the scene or mobject, use:\n\n>>> self.show_frame()        # view image of current scene\n>>> c = Circle()\n>>> c.show()                 # view image of Mobject\n\n>>> \n```\n\n- Config parameters in the command line carry over to manim\'s internal framework.\nFor example:\n\n```bash\npython -m manim_livestream -v WARNING\n\n...INFO...\n\n>>> config.verbosity\n\'WARNING\'\n>>>\n```\n\n- IPython is an option:\n\n```bash\npython -m manim_livestream --use-ipython\n\n...INFO...\n\nPython 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)]\nType \'copyright\', \'credits\' or \'license\' for more information\nIPython 7.23.0 -- An enhanced Interactive Python. Type \'?\' for help.\n\nIn [1]:\n\n```\n\n- Simple ways exist for simpler actions:\n\n```py\nPython 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32\nType "help", "copyright", "credits" or "license" for more information.\n\n>>> from manim_livestream import stream\n>>> from manim import Circle, ShowCreation\n>>> self = stream()\n>>> circ = Circle()\n>>> self.play(ShowCreation(circ))\n```\n\n- You want scenes present in files? Here you go:\n\n```bash\npython -m manim_livestream example_scenes/basic.py\nManim Community v0.6.0\n\n1: OpeningManim\n2: SquareToCircle\n3: UpdatersExample\n4: WarpSquare\n5: WriteStuff\n\nChoose number corresponding to desired scene/arguments.\n(Use comma separated list for multiple entries)\nChoice(s): 2\n\n```\n\nThis particular one will render the scene and send the frames to the streaming protocol.\n\n## Potential problems\n- Last 2 or 3 frames don\'t get sent\n  Close the window and restart it with `open_client()`\n- The entire thing freezes\n  Close the window and restart it with `open_client()`\n- Using any other streaming protocol\n  As of yet, not a great plan. From experimentation rtp seems the most stable. However the\n  streaming port shouldn\'t be too hard to modify.\n  \n\n\n## License and contribution\nThe code is released as Free Software under the [GNU/GPLv3](https://choosealicense.com/licenses/gpl-3.0/) license. \nCopying, adapting and republishing it is not only consent but also encouraged, particularly surrounding the subject of tests for the framework.\n\n',
    'author': 'NeoPlato',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/NeoPlato/manim-manim_livestream',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.6.2,<4.0.0',
}


setup(**setup_kwargs)
