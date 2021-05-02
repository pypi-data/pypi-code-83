# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sonora']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.7.4,<4.0.0',
 'async-timeout>=3.0.1,<4.0.0',
 'grpcio>=1.37.1,<2.0.0',
 'urllib3>=1.26.4,<2.0.0']

setup_kwargs = {
    'name': 'sonora',
    'version': '0.2.1',
    'description': 'A WSGI and ASGI compatible grpc-web implementation.',
    'long_description': '[![CircleCI](https://circleci.com/gh/public/sonora.svg?style=svg)](https://circleci.com/gh/public/sonora)\n\n# Sonora\n\nSonora is a Python-first implementation of gRPC-Web built on top of standard Python APIs like [WSGI](https://wsgi.readthedocs.io/en/latest/what.html) and [ASGI](https://asgi.readthedocs.io/en/latest/) for easy integration.\n\n## Why?\n\nRegular gRPC has a lot going for it but is awkward to use in some environments. gRPC-Web makes it easy to get gRPC working in\nenvironments that need HTTP/1.1 but the Google gRPC and gRPC-Web implementations don\'t like to coexist with your normal Python\nframeworks like Django or Flask. Sonora doesn\'t care what ioloop you use, this means you can run it along side any other Python\nweb framework in the same application!\n\nThis makes it easy to\n\n- Add gRPC to an existing code base.\n- Run gRPC behind AWS and other HTTP/1.1 load balancers.\n- Integrate with other ASGI frameworks like [Channels](https://channels.readthedocs.io/en/stable/), [Starlette](https://www.starlette.io/), [Quart](https://pgjones.gitlab.io/quart/) etc.\n- Integrate with other WSGI frameworks like [Flask](https://flask.palletsprojects.com/en/1.1.x/), [Django](https://www.djangoproject.com/) etc.\n\nSonora aims to be compatible with and tested against Google\'s [grpc-web](https://github.com/grpc/grpc-web) implementation in both text mode and binary mode.\n\nThe name Sonora was inspired by the [Sonoran gopher snake](https://en.wikipedia.org/wiki/Pituophis_catenifer_affinis).\n\n![Snek](https://i.imgur.com/eqhQnlY.jpg)\n\n## How?\n\nSonora is designed to require minimal changes to an existing Python application.\n\n### Server\n\n#### WSGI\n\nNormally a WSGI application ([such as your favourite Django app](https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/)) will have a file somewhere named `wsgi.py`\nthat gets your application setup and ready for your web server of choice. It will look something like this.\n\n```python\nfrom django.core.wsgi import get_wsgi_application\napplication = get_wsgi_application()\n```\n\nTo add Sonora\'s gRPC-Web capabilities to an application like the above all you need to do to enable it is this.\n\n```python\nfrom django.core.wsgi import get_wsgi_application\nfrom sonora.wsgi import grpcWSGI\nimport helloworld_pb2_grpc\n\n# Setup your frameworks default WSGI app.\n\napplication = get_wsgi_application()\n\n# Install the Sonora grpcWSGI middleware so we can handle requests to gRPC\'s paths.\n\napplication = grpcWSGI(application)\n\n# Attach your gRPC server implementation.\n\nhelloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), application)\n```\n\nAnd now you have a combined HTTP/1.1 Django + gRPC application all under a single port.\n\n#### ASGI\n\nFor ASGI things are mostly the same, the example shown here integrates with [Quart](https://github.com/pgjones/quart) but it\'s more or less the same for other frameworks.\n\n```python\nfrom sonora.asgi import grpcASGI\nfrom quart import Quart\nimport helloworld_pb2_grpc\n\n# Setup your frameworks default ASGI app.\n\napplication = Quart(__name__)\n\n# Install the Sonora grpcASGI middleware so we can handle requests to gRPC\'s paths.\n\napplication = grpcASGI(application)\n\n# Attach your gRPC server implementation.\n\nhelloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), application)\n```\n\nAnd now you have a combined HTTP/1.1 Quart + gRPC application all under a single port.\n\n### Clients\n\nSonora provides both regular sync and aiohttp based async clients.\n\n#### Requests (Sync)\n\nInstead of using gRPCs native `grpc.insecure_channel` API we have `sonora.client.insecure_web_channel` instead which provides a [requests](https://github.com/kennethreitz/requests) powered client channel to a gRPC-Web server. e.g.\n\n```python\n    import sonora.client\n\n    with sonora.client.insecure_web_channel(\n        f"http://localhost:8080"\n    ) as channel:\n        stub = helloworld_pb2_grpc.GreeterStub(channel)\n        print(stub.SayHello("world"))\n```\n\n#### Aiohttp (Async)\n\nInstead of `grpc.aio.insecure_channel` we have `sonora.aio.insecure_web_channel` which provides an [aiohttp](https://docs.aiohttp.org/) based asyncio compatible client for gRPC-Web. e.g.\n\n```python\n    import sonora.aio\n\n    async with sonora.aio.insecure_web_channel(\n        f"http://localhost:8080"\n    ) as channel:\n        stub = helloworld_pb2_grpc.GreeterStub(channel)\n        print(await stub.SayHello("world"))\n\n        stub = helloworld_pb2_grpc.GreeterStub(channel)\n        async for response in stub.SayHelloSlowly("world"):\n            print(response)\n```\n\nThis also supports the new streaming response API introduced by [gRFC L58](https://github.com/grpc/proposal/pull/155)\n\n```python\n    import sonora.aio\n\n    async with sonora.aio.insecure_web_channel(\n        f"http://localhost:8080"\n    ) as channel:\n        stub = helloworld_pb2_grpc.GreeterStub(channel)\n        async with stub.SayHelloSlowly("world") as response:\n            print(await response.read())\n```\n',
    'author': 'Alex Stapleton',
    'author_email': 'alexs@prol.etari.at',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/public/sonora',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
