"""
The MIT License (MIT)

Copyright (c) 2020-2021 NotShin

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

import asyncio
import aiohttp
import websockets

BASE_URL = 'https://www.guilded.gg/api/'
GATEWAY_URI = 'wss://api.guilded.gg/socket.io/?jwt=undefined&EIO=3&transport=websocket'

def _cancel_tasks(loop):
    tasks = {task for task in asyncio.all_tasks(loop=loop) if not task.done()}

    # all tasks are done
    if not tasks:
        return

    # cancel all tasks
    for task in tasks:
        task.cancel()

    loop.run_until_complete(asyncio.gather(*tasks, return_exceptions=True))

    for task in tasks:
        if task.exception() is not None:
            loop.call_exception_handler({
                'message': 'Unhandled exception during Client.run shutdown.',
                'task': task,
                'exception': task.exception()
            })

def _cleanup_tasks(loop):
    try:
        print("Cleaning up tasks.")
        _cancel_tasks(loop)
    except:
        pass
    finally:
        print("Closing event loop.")
        loop.close()

class Client:
    def __init__(self, *, loop=None, **options):
        self.ws = None
        self.loop = asyncio.get_event_loop() if loop is None else loop

        self.command_prefix = options.get('command_prefix', None)
        self.description = options.get('description', None)

        self.__session = None
        self._connection = None
        self._closed = False

        self.user = None
        self.cookie = None

        self.all_commands = []
        self.tasks = []

    async def login(self, email, password):
        self.__session = aiohttp.ClientSession()

        payload = {
            'email': email,
            'password': password
        }

        ClientResponse = await self.__session.post(BASE_URL + "login", json=payload)

        try:
            if (ClientResponse.status == 200): # OK
                self.user = await ClientResponse.json()
                self.cookie = ClientResponse.headers['Set-Cookie']
                print(f"Successfully logged in as {self.user['user']['name']}")
            elif (ClientResponse.status == 400): # Bad Request
                await self.close()
                print("Email or password is invalid. Please check your credentials and try again.")
        except Exception as e:
            await self.close()
            print(e)

    async def connect(self):
        self._connection = await websockets.connect(GATEWAY_URI, extra_headers=[('cookie', self.cookie)])
        try:
            self.tasks.append(self.websocket_receive())
            self.tasks.append(self.send_heartbeat())
            await asyncio.gather(*self.tasks)
        except asyncio.exceptions.CancelledError:
            pass
        except Exception as e:
            print(e)
            await self.close()

    async def start(self, email, password):
        await self.login(email, password)
        await self.connect()

    def run(self, *args, **kwargs):
        loop = self.loop

        try:
            loop.run_until_complete(self.start(*args, **kwargs))
        except KeyboardInterrupt:
            print('Keyboard input received to terminate client connection.')
            loop.run_until_complete(self.close())
        finally:
            _cleanup_tasks(loop)

    def is_closed(self):
        return self._closed

    # closes all open connections
    async def close(self):
        if self._closed:
            return

        await self.__session.close()
        print('Closing Guilded connection')
        self._closed = True

        if self._connection is not None and self._connection.open:
            print('Closing websocket connection')
            await self._connection.close(code=1000)

    # receives websocket events and sends to interpreter
    async def websocket_receive(self):
        try:
            while not self.is_closed():
                self.ws = await asyncio.wait_for(self._connection.recv(), timeout=60.0)
                print(self.ws)
        except websockets.exceptions.ConnectionClosed:
            pass

    # send heartbeat every 25 seconds
    async def send_heartbeat(self):
        try:
            while not self.is_closed():
                await self._connection.send('2')
                await asyncio.sleep(25)
        except asyncio.exceptions.CancelledError:
            pass
