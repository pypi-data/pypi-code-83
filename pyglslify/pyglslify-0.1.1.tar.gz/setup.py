# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['pyglslify']
setup_kwargs = {
    'name': 'pyglslify',
    'version': '0.1.1',
    'description': 'Thin wrapper for the glslify nodejs tool, use stack.gl shader modules in Python.',
    'long_description': '# pyglslify\n\nA very thin wrapper for the [glslify](https://github.com/glslify/glslify) nodejs tool, to use [stack.gl](http://stack.gl) shader modules in Python during development.\n\n(after development you\'re probably best just compiling the shaders with nodejs `glslify` cli tool to a file and using the result)\n\n## Installation\n\nThe whole point is to be able to download and use GLSL shader modules from the WebGL community, which are distributed via `npm`.\n\nSo first you need to install nodejs/npm: https://www.npmjs.com/get-npm\n\nThen install the `glslify` tool globally and verify it is on your path:\n```\nnpm install -g glslify\nglslify --help\n```\n\nThen add `pyglslify` in your Python project virtualenv:\n```\npip install pyglslify\n```\n\n## Usage\n\nWe\'re still going to use `npm` to install stack.gl shaders. For example:\n\n```\nnpm install glsl-noise\n```\n\nThis will create `package.json` and `package-lock.json` files in your project root, which will track the `npm` dependencies of your project. These should be committed to source control along with the rest of your project. By default the modules will be downloaded to a `node_modules` dir in your project root, that dir should be added to `.gitignore`.\n\nIf you checkout your project repo on a new machine you can just run `npm install` to fetch the modules specified as dependencies in `package.json`.\n\nOn the Python side you can write GLSL shaders which make use of the glslify `require` pragma:\n```glsl\n#pragma glslify: noise = require(\'glsl-noise/simplex/3d\')\n\nprecision mediump float;\nvarying vec3 vpos;\n\nvoid main () {\n    gl_FragColor = vec4(noise(vpos*25.0),1);\n}\n```\n`fshader.glsl`\n\nAnd then in your Python code, when you want to pass the shader to your rendering pipeline, use `pyglslify` to resolve the pragmas:\n```python\nimport moderngl_window as mglw\nfrom pyglslify import glslify\n\n\nclass RenderWindow(mglw.WindowConfig):\n    def __init__(self, **kwargs):\n        super().__init__(**kwargs)\n        vertex_shader = self.load_text("shaders/vshader.glsl")\n        fragment_shader = self.load_text(\n            glslify("shaders/fshader.glsl")\n        )\n        self.pipeline = self.ctx.program(\n            vertex_shader=vertex_shader,\n            fragment_shader=fragment_shader,\n        )\n```\n\nYou can also use glslify [Source Transforms](https://github.com/glslify/glslify#source-transforms).\n\ne.g. `npm install glslify-hex` allows use of CSS-style hex strings for colors in place of `vec3`s.\n\nSee the glslify docs - they recommend specifying these as configuration in your `package.json`.\n\nYou can also apply local transforms to the shader file at runtime from Python, by passing their module names as args like:\n```python\nfrom pyglslify import glslify\n\nfragment_shader = glslify("shaders/fshader.glsl", "glslify-hex", "glslify-import")\n```\n\nHappy shading!\n',
    'author': 'Anentropic',
    'author_email': 'ego@anentropic.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/anentropic/pyglslify',
    'py_modules': modules,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
