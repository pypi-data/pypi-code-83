'''
Info
========
A basic wrapper for the API SRA(Some Random Api) \n
Copyright - (c) 2021, Nimboss#9651 (ID - 717724055217635398) on Discord, Nimboss2411 on GitHub \n
API Creator - (c) 2018 - 2021, Telk#4038 (ID - 423675224395874314) on Discord, telkenes on GitHub \n
License - MIT

Links
========
URL for API - https://some-random-api.ml \n
Github repository - https://github.com/Nimboss2411/SRApiWrapper \n
Documentation - https://github.com/Nimboss2411/SRApiWrapper/tree/main/Documentation \n
SRApi Discord server - https://discord.gg/E4HT8KTTd5 \n
API Keys - https://some-random-api.ml/docs/Welcome/Keys

Usage
========
Synchronous usage- \n
    For using synchronous API wrapper functions, make a new instance of `class SRAPI`. \n
    `class SRAPI()` params - `api_key` (type - `str` or `NoneType` if key is not needed). \n
Asynchronous usage- \n
    For using asynchronous API wrapper functions with the `async` and `await` syntax, make a new instance of `class AioSRAPI`. \n
    `class AioSRAPI()` params - `api_key` (type - `str` or `NoneType` if key is not needed).

API Keys
========
An API Key is a special alpha-numerical 20-character string that is used to access more features and less ratelimits in the SRAPI. \n
There are 3 tiers of API Keys - Tier 1, Tier 2 and Tier 3 (with Tier 3 being the best). \n
Learn how to get API Keys and read about their ratelimits here: https://some-random-api.ml/docs/Welcome/Keys.
'''

import aiohttp
from io import BytesIO
from random import choice
import requests
from json.decoder import JSONDecodeError
from urllib.parse import quote

class InvalidUrl(Exception): pass
class ApiKeyError(Exception): pass
class HTTPError(Exception): pass

class AioSRAPI:
    '''
    # Asynchronous class wrapper
    `This is the class that contains all the asynchronous functions for Some Random API.`\n
    `The functions of this class require python's async/await syntax.`\n
    `If you don't know what that is you should consider using SRAPI(), the class with non-asynchronous, normal functions.`\n
    Use the `dir()` method on this class to see all its functions in a list (ignore the `__double_underscore_builtins__`)\n
    Parameters -\n
        `api_key` (type str) (default None)
        `warnings` (type bool) (default True) (defining it as False disables warnings about functions you might get through printing)
    Usage-\n
        Make a new instance of this class with the parameters above,
        Use it's functions using `your_class_instance.function_name()`
    The class for using the synchronous API wrapper class is `SRAPI()`.
    '''
    def __init__(self, api_key: str = None, warnings: bool = True):
        self.api_key = api_key
        if not api_key is None:
            self.formatted_api_key = f'&key={api_key}'
        else:
            self.formatted_api_key = ''

    async def errorhandler(self, jsondata, other_args: list = None):
        '''
        # Error handling
        A function for private use, a global error handler to raise the right errors in right situations.\n
        Returns - None.\n
        Raises - Errors depending on the error message recieved from the API.
        '''
        try:
            e = jsondata['error']
        except KeyError:
            return

        if (e == 'avatar is not a valid url') or (e == 'Image given has not completed loading') or (e == 'Internal image has not completed loading'):
            if other_args[1] == 'background_link':
                raise InvalidUrl(f'The {other_args[0]} or {other_args[1]} argument is an invalid, non-image URL. The URL only supports JPG, JPEG, PNG or GIF files. Also use HTTPS links only and not HTTP.')
            raise InvalidUrl(f'The {other_args[0]} argument is an invalid, non-image URL. The URL only supports JPG, JPEG, PNG or GIF files. Also use HTTPS links only and not HTTP.')

        elif (e == 'Your key isn\'t able to use this endpoint, please consider upgrading your key') or (e == 'Invalid key') or (e == 'Your key has expired'):
            raise ApiKeyError(f'{self.api_key} is not a valid key/is an expired key/is a key of too low tier. Get a valid key at https://some-random-api.ml/docs/Welcome/Keys. Type -vote and follow the instructions.')

        elif (e == 'Too many requests, please try again later.'):
            raise HTTPError('Too many requests are being sent to the API, please try again later. You are being ratelimited. Try sleeping/waiting for sometime.')
        
        else:
            raise HTTPError(f'{jsondata["error"]}')

    async def aio_quote(self, str_to_quote: str, safe: str):
        '''
        A function for private user. Only availible in the AioSRAPI class.\n
        This is just so that `urllib.parse.quote` can be used asynchronously.
        '''
        return quote(str_to_quote, safe = safe)

    async def keycheck(self):
        '''
        # Check your key
        `Checks your API key and returns your key\'s details`\n
        Parameters -\n
            `api_key` (type str) (in class initialization, not a function parameter)
        Returns -\n
            Your key's details (type dict)
            {'id': 'your key\'s id', 'tier': your key\'s tier (type int), 'end': when your key ends (type int) (format - number of milliseconds from `January 1st, 1970 00:00:00 GMT`)}
        Raises -\n
            SRApi.ApiKeyError - If the key you provided is an invalid key, or it is None/unspecified
        '''
        if self.api_key is None:
            raise ApiKeyError('An API key is required for this function. To get an API key visit https://some-random-api.ml/docs/Welcome/Keys.')
        
        if self.warnings is True:
            print('Warning: Do not use this function often as it has a very high ratelimit (you can only use it 10 times per minute)\nThese warnings can be turned off in the class initialisation (warnings = False).')

        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://some-random-api/key/check?key={self.api_key}') as session_keycheck:
                jsondata = await session_keycheck.json()

        try:
            return {
                'id': jsondata['id'],
                'tier': jsondata['tier'],
                'end': jsondata['end']
            }
        except KeyError:
            if jsondata['error'] == 'No user found with that key':
                raise ApiKeyError('The API key you have given is invalid/expired. To get an API key visit https://some-random-api.ml/docs/Welcome/Keys.')
            await self.errorhandler(jsondata)
    
    async def fact(self, type_of_fact: str) -> str:
        '''
        # Random fact
        Parameters - \n
            `type_of_fact` (type str) (case-insensitive)\n
        `type_of_fact` must be one of the elements from this list: `dog, cat, panda, fox, bird (alias - birb), koala, kangaroo, racoon (alias - raccoon), elephant, giraffe, whale`.\n
        Returns -\n
            A random fact about the category you provided (type str).\n
        Raises -\n
            ValueError, if the `type_of_fact` category is not from the list above.
        '''
        if not type_of_fact.lower() in ['dog', 'cat', 'panda', 'fox', 'bird', 'birb', 'koala', 'kangaroo', 'racoon', 'raccoon', 'elephant', 'giraffe', 'whale']:
            raise ValueError('The only type of facts that are provided are dog, cat, panda, fox, bird (alias - birb), koala, kangaroo, racoon (alias - raccoon), elephant, giraffe, whale.')
    
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://some-random-api.ml/facts/{type_of_fact.lower()}?key={self.api_key}') as session_fact:
                jsondata = await session_fact.json()
        return jsondata['fact']

    async def image(self, type_of_image: str) -> str:
        '''
        # Random image link
        Parameters - \n
            `type_of_image` (type str) (case-insensitive)\n
        `type_of_image` must be one of the elements from this list: `dog, cat, panda, red_panda, bird (alias - birb), fox, koala, racoon (alias - raccoon), kangaroo, whale, pikachu`.\n
        Returns -\n
            A link to a random image with the category you provided (type str).\n
        Raises -\n
            ValueError, if the `type_of_image` category is not from the list above.
        '''
        if not type_of_image.lower() in ['dog', 'cat', 'panda', 'red_panda', 'birb', 'bird', 'fox', 'koala', 'racoon', 'raccoon', 'kangaroo', 'whale', 'pikachu']:
            raise ValueError('The only types of images that are provided are dog, cat, panda, red_panda, bird (alias - birb), fox, koala, racoon (alias- raccoon), kangaroo, whale, pikachu.')
        
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://some-random-api.ml/img/{type_of_image.lower()}?key={self.api_key}') as session_pic:
                jsondata = await session_pic.json()
        return jsondata['link']

    async def gif(self, type_of_gif: str) -> str:
        '''
        # Random gif link
        Parameters - \n
            `type_of_gif` (type str) (case-insensitive)\n
        `type_of_gif` must be one of the elements from this list: `wink, pat, hug, face-palm`.\n
        Returns -\n
            A link to a random gif with the category you provided (type str).\n
        Raises -\n
            ValueError, if the `type_of_gif` category is not from the list above.
        '''
        if not type_of_gif.lower() in ['wink', 'pat', 'hug', 'face-palm']:
            raise ValueError('The only types of gifs that are provided are wink, pat, hug, face-palm.')
        
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://some-random-api.ml/animu/{type_of_gif.lower()}?key={self.api_key}') as session_gif:
                jsondata = await session_gif.json()
        return jsondata['link']

    async def animeQuote(self) -> dict:
        '''
        # Random anime quote
        Returns -\n
            A random anime quote with it's details (type dict)
            {'character': 'the character that said the quote', 'anime': 'the anime from where the quote is from', 'quote': 'the quote'}
        '''
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://some-random-api.ml/animu/quote?key={self.api_key}') as session_quote:
                jsondata = await session_quote.json()
        return {
            'character': jsondata['characther'],
            'anime': jsondata['anime'],
            'quote': jsondata['sentence']
        }

    async def stringSimilarity(self, string1: str, string2: str) -> str:
        '''
        # Compares two strings to check similarity%
        Parameters -\n
            string1 (type str)
            string2 (type str)
        Returns -\n
            The strings' similarity% (type int)
        '''
        string1 = await self.aio_quote(string1, safe = '')
        string2 = await self.aio_quote(string2, safe = '')
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://some-random-api.ml/stringsimilarity?string1={string1.replace(" ", "%20")}&string2={string2.replace(" ", "%20")}&key={self.api_key}') as session_similarity:
                jsondata = await session_similarity.json()
        return jsondata['similarity'] * 100

    async def overlay(self, type_of_overlay: str, image_to_overlay: str) -> BytesIO:
        '''
        # Image overlays
        Parameters - \n
            `type_of_overlay` (type str) (case-insensitive), 
            `image_to_overlay` (type str) (case-sensitive)\n
        `type_of_overlay` must be one of the elements from this list: `gay, glass, wasted, triggered, jail, comrade`.\n
        `image_to_overlay` must be a direct URL to an image link. Supported image formats - JPG, JPEG, PNG, GIF.\n
        Returns -\n
            if `type_of_overlay` is `gay` - An image in BytesIO form with a rainbow overlay on it (type BytesIO).
            if `type_of_overlay` is `glass` - An image in BytesIO form with a glass-like white overlay on it (type BytesIO).
            if `type_of_overlay` is `wasted` - An image in BytesIO form with the text "wasted" in red colour on a grey version of your original picture (type BytesIO).
            if `type_of_overlay` is `triggered` - A GIF in BytesIO form which has a red-yellow angry shaking overlay on your original picture with the text "Triggered" at the bottom of the GIF (type BytesIO).
            if `type_of_overlay` is `jail` - An image in BytesIO form with jail-cell bars on top of a grey version of your original picture (type BytesIO).
            if `type_of_overlay` is `comrade` - An image in BytesIO form with a red-like overlay and a yellow communist symbol on it.
        Raises -\n
            ValueError, if the `type_of_fact` category is not from the list specified above.
            SRApi.InvalidURL, if the `image_to_overlay` argument\'s URL is invalid.
        '''
        if not type_of_overlay.lower() in ['gay', 'glass', 'wasted', 'triggered', 'jail', 'comrade']:
            raise ValueError('The only types of overlays that are provided are gay, glass, wasted, triggered, jail, comrade.')

        image_to_overlay = await self.aio_quote(image_to_overlay, safe = '')
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://some-random-api.ml/canvas/{type_of_overlay.lower()}?avatar={image_to_overlay}&key={self.api_key}') as session_image:
                try:
                    jsondata = await session_image.json()
                    await self.errorhandler(jsondata, ['image_to_overlay'])
                except aiohttp.ContentTypeError:
                    return BytesIO(await session_image.read())

    async def lyrics(self, search_query: str) -> dict:
        '''
        # Lyrics to a song
        Parameters - \n
            `search_query` (type str) (case-insensitive)\n
        It is recommended to have the song title in the `search_query` argument and not just the composer of the song.\n
        Returns -\n
            Lyrics to the song you asked for (type str).\n
        Raises -\n
            ValueError, if the lyrics to the song you were looking for couldn\'t be found.
        '''
        search_query = await self.aio_quote(search_query, safe = '')
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://some-random-api.ml/lyrics?title={search_query.lower().replace(" " , "%20")}&key={self.api_key}') as session_lyrics:
                jsondata = await session_lyrics.json()
        try:
            if jsondata['error'] == 'Sorry I couldn\'t find that song\'s lyrics':
                raise ValueError(f'{search_query}\'s lyrics couldn\'t be found.')
            await self.errorhandler(jsondata)
        except KeyError:
            return {'title' : jsondata['title'], 
                'author': jsondata['author'] , 
                'lyrics' : jsondata['lyrics'], 
                'thumbnail': jsondata['thumbnail']['genius'], 
                'links' : jsondata['links']['genius']}

    async def base64(self, base64_action: str, base64_text: str) -> str:
        '''
        # Base64 encoding and decoding
        Parameters-\n
            `base64_action` (type str) (case-insensitive)
            `base64_text` (type str) (case-sensitive)
        `base64_action` must be one of the elements from this list: `encode, decode`.\n
        Returns-\n
            if `base64_action` is `encode` - A base64 encoded version of `base64_text` (type str).
            if `base64_action` is `decode` - A base64 decoded version of `base64_text` (type str).
        Raises -\n
            ValueError, if `base64_action` is not from the list specified above.
        '''
        if not base64_action.lower() in ['encode', 'decode']:
            raise ValueError('The only actions supported for base64 are encode, decode.')
        
        base64_text = await self.aio_quote(base64_text, safe = '')
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://some-random-api.ml/base64?{base64_action.lower()}={base64_text}&key={self.api_key}') as session_base64:
                jsondata = await session_base64.json()
        if base64_action.lower() == 'encode':
            return jsondata['base64']
        return jsondata['text']

    async def binary(self, binary_action: str, binary_text: str) -> str:
        '''
        # Binary encoding and decoding
        Parameters-\n
            `binary_action` (type str) (case-insensitive)
            `binary_text` (type str) (case-sensitive)
        `binary_action` must be one of the elements from this list: `encode, decode`.\n
        Returns-\n
            if `binary_action` is `encode` - A binary encoded version of `binary_text` (type str).
            if `binary_action` is `decode` - A binary decoded version of `binary_text` (type str).
        Raises -\n
            ValueError, if `binary_action` is not from the list specified above.
        '''
        if not binary_action.lower() in ['encode', 'decode']:
            raise ValueError('The only actions supported for binary are encode, decode.')
        
        binary_text = await self.aio_quote(binary_text.replace(' ', ''), safe = '')
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://some-random-api.ml/binary?{binary_action.lower()}={binary_text}&key={self.api_key}') as session_binary:
                jsondata = await session_binary.json()
        
        if binary_action.lower() == 'encode':
            return jsondata['binary']
        else:
            return jsondata['text']

    async def joke(self) -> str:
        '''
        # Random joke
        Returns - A random joke from the API (type str).\n
        '''
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://some-random-api.ml/joke?key={self.api_key}') as session_joke:
                jsondata = await session_joke.json()
        return jsondata['joke']

    async def minecraft(self, mc_username: str) -> dict:
        '''
        # Minecraft profile details
        Parameters -\n
            `mc_username` (type str) (case-insensitive)
        Returns -\n
            `mc_username`\'s Minecraft profile details (type dict)
            {'username': 'The username of the player', 'uuid': 'The UUID of the player, 'name_history': [The name history of the player]}
        Raises -\n
            ValueError, if the username provided is invalid.
        '''
        if self.warnings is True:
            print('Warning: if you entered a correct username and you still get an invalid username error, then the API is ratelimited.\nThese warnings can be turned off in the class initialisation (warnings = False).')
        
        mc_username = await self.aio_quote(mc_username, safe = '')
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://some-random-api.ml/mc?username={mc_username.lower()}&key={self.api_key}') as session_mc:
                jsondata = await session_mc.json()
        try:
            return {'username' : jsondata['username'],
                'uuid' : jsondata['uuid'],
                'name_history' : jsondata['name_history']
                }
        except KeyError:
            raise ValueError('The Minecraft username you entered is invalid.')

    async def meme(self) -> dict:
        '''
        # Random meme
        Returns -\n
            A random meme (type dict)
            {'id': the id of the meme, 'image': 'a link to the image of the meme', 'caption': 'the meme\'s caption', 'category': 'the category of the meme'}
        '''
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://some-random-api.ml/meme?key={self.api_key}') as session_meme:
                jsondata = await session_meme.json()
        return {'id' : jsondata['id'],
                'image' : jsondata['image'],
                'caption' : jsondata['caption'],
                'category' : jsondata['category']}

    async def chatbot(self, chatbot_message: str, user_id: str = None) -> str:
        '''
        # An AI that responds to your statements
        `API Key of Tier 1 or above required to use this function`\n
        Parameters -\n
            `chatbot_message` (type str)
            `user_id` (type str) (default None) (this parameter can be anything that can be converted to string, it is just there so the API can link a user_id to a particular user)
            `api_key` (type str) (in class initialization, not a function parameter)
        Returns -\n
            An AI response to `chatbot_message` (type str)
        Raises -\n
            SRApi.ApiKeyError - If your API key is invalid or if your API key is not provided/is None.
        '''
        if self.api_key is None:
            raise ApiKeyError('A Tier-1 or above API key is required for this function. To get an API key visit https://some-random-api.ml/docs/Welcome/Keys.')
        
        chatbot_message = await self.aio_quote(chatbot_message, safe = '')
        user_id = await self.aio_quote(user_id, safe = '')
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://some-random-api.ml/chatbot?message={chatbot_message.lower().replace(" ", "%20")}&key={self.api_key}{"&uid=" + await self.aio_quote(user_id, safe = "") if not user_id is None else ""}') as session_ai:
                jsondata = await session_ai.json()
        try:
            return jsondata['response']
        except KeyError:
            await self.errorhandler(jsondata)

    async def rgbToHex(self, r: int, g: int, b: int) -> str:
        '''
        # RGB color values to hexcodes
        Parameters -\n
            `r` (red value) (type int) (must be between 0 and 255, 0, 255 included)
            `g` (green value) (type int) (must be between 0 and 255, 0, 255 included)
            `b` (blue value) (type int) (must be between 0 and 255, 0, 255 included)
        Returns -\n
            The hexcode for the RGB values provided (type str) (format - ffffff).
        Raises -\n
            ValueError, if any of the parameters are not in the range 0-255.
        '''
        for color in [r, g, b]:
            if not color in list(range(0, 256)):
                raise ValueError('The red, blue and green parameters must at minimum 0 or at maximum 255.')
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://some-random-api.ml/canvas/hex?rgb={r},{g},{b}&key={self.api_key}') as session_rgbtohex:
                jsondata = await session_rgbtohex.json()
        return jsondata['hex'][1:]

    async def hexToRgb(self, hexcode: str) -> dict:
        '''
        # Hexcode color values to RGB values
        Parameters -\n
            `hexcode` (case-insensitive), in one of these formats - '#ffffff', '0xffffff', 'ffffff' (type str)
        Returns -\n
            RGB values for the hexcode (type dict)
            {'r': red_value, 'g': green_value, 'b': blue_value}
        Raises -\n
            ValueError, if you entered an invalid hexcode
        '''
        if hexcode.startswith('#'):
            hexcode = hexcode[1:]
        elif hexcode.startswith('0x'):
            hexcode = hexcode[2:]
        if not len(hexcode) == 6:
            raise ValueError(f'{hexcode} is not a valid hexcode. Types of hexcode that are supported - ffffff, #ffffff, 0xffffff.')
        for code in hexcode:
            if not code in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f']:
                raise ValueError(f'{hexcode} is not a valid hexcode. Types of hexcode that are supported - ffffff, #ffffff, 0xffffff.')
        
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://some-random-api.ml/canvas/rgb?hex={hexcode}&key={self.api_key}') as session_hextorgb:
                jsondata = await session_hextorgb.json()
        return {'r' : jsondata['r'],
                'g' : jsondata['g'],
                'b' : jsondata['b']}

    async def filter(self, type_of_filter: str, image: str) -> BytesIO:
        '''
        # Filter an image
        Parameters -\n
            `type_of_filter` (type str) (case-insensitive).
            `image` (type str) (case-sensitive) (A link to the image you want to filter).
        `type_of_filter` must be one of the elements from this list - `greyscale, invert, brightness, threshold, sepia, red, green, blue, blurple, pixelate, blur, jpg`\n
        Returns -\n
            An image in BytesIO form manipulated according to the filter you provided.
        Raises -\n
            ValueError, if the `type_of_filter` argument is not from the list specified above.
            SRApi.InvalidURL, if the `image` argument is an invalid, non-image URL.
        '''
        if not type_of_filter.lower() in ['greyscale', 'invert', 'brightness', 'threshold', 'sepia', 'red', 'green', 'blue', 'blurple', 'pixelate', 'blur', 'jpg']:
            raise ValueError('The only types of filters that are provided are greyscale, invert, brightness, threshold, sepia, red, green, blue, blurple, pixelate, blur, jpg.')
        
        image = await self.aio_quote(image, safe = '')
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://some-random-api.ml/canvas/{type_of_filter.lower()}?avatar={image}&key={self.api_key}') as session_filter:
                try:
                    jsondata = await session_filter.json()
                    await self.errorhandler(jsondata, ['image'])
                except aiohttp.ContentTypeError:
                    return BytesIO(await session_filter.read())

    async def dbotToken(self) -> str:
        '''
        # Discord Bot Token. Note that this function is related to Discord.
        Returns - A randomly generated Discord Bot Token (type str).
        '''
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://some-random-api.ml/bottoken?key={self.api_key}') as session_bottoken:
                jsondata = await session_bottoken.json()
        return jsondata['token']

    async def amongUs(self, username: str, image: str, impostor: bool = choice([False, False, True, False, False])) -> BytesIO:
        '''
        # Among Us ejection GIF
        `API Key of Tier 1 or above required to use this function`\n
        Parameters -\n
            `username` (type str) (max len 20)
            `image` (type str) (a direct link to a PNG, JPG, JPEG or GIF file)
            `impostor` (type bool) (by default a 1/5 chance of showing impostor)
            `api_key` (type str) (in class initialization, not a function parameter)
        Returns -\n
            A GIF of your `image` URL in the form of an Among Us ejection (type BytesIO)
        Raises -\n
            SRApi.ApiKeyError - If your API key is invalid or if your API key is not provided/is None.
            ValueError - If the length of `username` is more than 20.
            SRApi.InvalidURL - If the `image` URL is invalid.
        '''
        if self.api_key is None:
            raise ApiKeyError('A Tier-1 or above API key is required for this function. To get an API key visit https://some-random-api.ml/docs/Welcome/Keys.')
        
        if len(username) > 20:
            raise ValueError('The username parameter must be at maximum 20 characters.')

        if self.warnings is True:
            print('Warning: This function takes time to process.\nThese warnings can be turned off in the class initialisation (warnings = False).')
        
        if impostor is True:
            impostor = 'true'
        elif impostor is False:
            impostor = 'false'

        username = await self.aio_quote(username, safe = '')
        image = await self.aio_quote(image, safe = '')
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://some-random-api.ml/premium/amongus?key={self.api_key}&username={username}&avatar={image}&impostor={impostor}') as session_amongus:
                try:
                    jsondata = await session_amongus.json()
                    await self.errorhandler(jsondata, ['image_to_amongus'])
                except aiohttp.ContentTypeError:
                    return BytesIO(await session_amongus.read())

    async def petPet(self, image: str) -> BytesIO:
        '''
        # Pet Pet gif
        `API Key of Tier 1 or above required to use this function`\n
        Parameters -\n
            `image` (type str) (a direct link to a PNG, JPG, JPEG or GIF file)
            `api_key` (type str) (in class initialization, not a function parameter)
        Returns -\n
            A GIF of `image` being patted by a hand repeatedly.
        Raises -\n
            SRApi.InvalidURL - If `image` is an invalid, non-image URL.
            SRApi.ApiKeyError - If your API key is invalid or if your API key is not provided/is None.
        '''
        if self.api_key is None:
            raise ApiKeyError('A Tier-1 or above API key is required for this function. To get an API key visit https://some-random-api.ml/docs/Welcome/Keys.')
        
        image = await self.aio_quote(image, safe = '')
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://some-random-api.ml/premium/petpet?key={self.api_key}&avatar={image}') as session_petpet:
                try:
                    jsondata = await session_petpet.json()
                    await self.errorhandler(jsondata, ['image'])
                except aiohttp.ContentTypeError:
                    return BytesIO(await session_petpet.read())
        
    async def youtubeComment(self, avatar: str, username: str, comment: str) -> BytesIO:
        '''
        # YouTube Comment Image
        Parameters -\n
            `avatar` (type str) (A direct link to a PNG, JPG, JPEG or GIF file)
            `username` (type str) (max len 25)
            `comment` (type str) (max len 1000)
        Returns -\n
            An image of a YouTube comment with `avatar` as the profile picture, `username` as the name and `comment` as the comment\'s content (type BytesIO).
        Raises -\n
            ValueError - if `username` is more than 25 characters or `comment` is more than 1000 characters.
            SRApi.InvalidURL - if `avatar` is an invalid, non-image URL.
        '''
        if len(username) > 25:
            raise ValueError('The length of the username argument must be at maximum 25 characters.')
        if len(comment) > 1000:
            raise ValueError('The length of the comment argument must be at maximum 1000 characters.')
        
        avatar = await self.aio_quote(avatar, safe = '')
        username = await self.aio_quote(username, safe = '')
        comment = await self.aio_quote(comment, safe = '')
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://some-random-api.ml/canvas/youtube-comment?avatar={avatar}&username={username}&comment={comment.replace(" ", "%20")}&key={self.api_key}') as session_ytcomment:
                try:
                    jsondata = await session_ytcomment.json()
                    await self.errorhandler(jsondata, ['avatar'])
                except aiohttp.ContentTypeError:
                    return BytesIO(await session_ytcomment.read())

    async def simpCard(self, avatar: str) -> BytesIO:
        '''
        # Simp Card Image
        Parameters -\n
            `avatar` (type str) (A direct link to a PNG, JPG, JPEG or GIF file)
        Returns -\n
            An image with a card with the words "Simp card" on it with `avatar` on its left side (type BytesIO).
        Raises -\n
            SRApi.InvalidURL - If `avatar` is an invalid, non-image URL.
        '''
        avatar = await self.aio_quote(avatar, safe = '')
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://some-random-api.ml/canvas/simpcard?avatar={avatar}&key={self.api_key}') as session_simp:
                try:
                    jsondata = await session_simp.json()
                    await self.errorhandler(jsondata, ['avatar'])
                except aiohttp.ContentTypeError:
                    return BytesIO(await session_simp.read())

    async def hornyCard(self, avatar: str) -> BytesIO:
        '''
        # Horny Card Image
        Parameters -\n
            `avatar` (type str) (A direct link to a PNG, JPG, JPEG or GIF file)
        Returns -\n
            An image with a card with the words "License to be horny" on it with `avatar` on its left side (type BytesIO).
        Raises -\n
            SRApi.InvalidURL - If `avatar` is an invalid, non-image URL.
        '''
        avatar = await self.aio_quote(avatar, safe = '')
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://some-random-api.ml/canvas/horny?avatar={avatar}&key={self.api_key}') as session_horny:
                try:
                    jsondata = await session_horny.json()
                    await self.errorhandler(jsondata, ['avatar'])
                except aiohttp.ContentTypeError:
                    return BytesIO(await session_horny.read())

    async def loliceBearcop(self, avatar: str) -> BytesIO:
        '''
        # Horny Card Image
        Parameters -\n
            `avatar` (type str) (A direct link to a PNG, JPG, JPEG or GIF file)
        Returns -\n
            An image where `avatar` is pasted on a bear cop (type BytesIO).
        Raises -\n
            SRApi.InvalidURL - If `avatar` is an invalid, non-image URL.
        '''
        avatar = await self.aio_quote(avatar, safe = '')
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://some-random-api.ml/canvas/lolice?avatar={avatar}&key={self.api_key}') as session_lolice:
                try:
                    jsondata = await session_lolice.json()
                    await self.errorhandler(jsondata, ['avatar'])
                except aiohttp.ContentTypeError:
                    return BytesIO(await session_lolice.read())

    async def itsSoStupid(self, avatar: str, text: str) -> BytesIO:
        '''
        # Its So Stupid Image
        Parameters -\n
            `avatar` (type str) (A direct link to a PNG, JPG, JPEG or GIF file)
            `text` (type str) (max len 20)
        Returns -\n
            An image with a dog saying `text` and someone calling it stupid (type BytesIO).
        Raises -\n
            ValueError - if `text` is more than 20 characters.
            SRApi.InvalidURL - if `avatar` is an invalid, non-image URL.
        '''
        if len(text) > 20:
            raise ValueError('The text argument must be at maximum 20 characters.')
        
        avatar = await self.aio_quote(avatar, safe = '')
        text = await self.aio_quote(text, safe = '')
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://some-random-api.ml/canvas/its-so-stupid?avatar={avatar}&dog={text.replace(" ", "%20")}&key={self.api_key}') as session_stupid:
                try:
                    jsondata = await session_stupid.json()
                    await self.errorhandler(jsondata, ['avatar'])
                except aiohttp.ContentTypeError:
                    return BytesIO(await session_stupid.read())

    async def colorViewer(self, hexcode: str = None, rgbvalues: list = None) -> BytesIO:
        '''
        # Color viewer image
        Parameters -\n
            `hexcode` (type str) (must be in one of the following formats - '#ffffff', '0xffffff', 'ffffff') (default - None)
            `rgbvalues` (type list) (format - [red_value, green_value, blue_value]) (default - None)
        `If both values are unspecified/None, an error will be raised. If both values are specified/not None, an error will be raised. Only pass in either hexcode or rgbvalues to the function.`\n
        Returns -\n
            An image filled with the color you specified (type BytesIO).
        Raises -\n
            ValueError - if a valid color was not provided, if both values `hexcode` and `rgbvalues` are specified, if both values `hexcode` and `rgbvalues` are None/unspecified.
        '''
        if (hexcode is None) and (rgbvalues is None):
            raise ValueError('Either specify the hexcode using hexcode = \'hexcode\' or the RGB values in list form using rgbvalues = [red_value, green_value, blue_value].')

        if (hexcode is not None) and (rgbvalues is not None):
            raise ValueError('Both values cannot be specified. Either specify the hexcode using hexcode = \'hexcode\' or the RGB values in list form using rgbvalues = [red_value, green_value, blue_value].')
        
        if rgbvalues is not None:
            if not len(rgbvalues) == 3:
                raise ValueError('The RGB values given are invalid.')
            for value in rgbvalues:
                if not value in list(range(0,256)):
                    raise ValueError('The RGB values given are invalid.')
            hexcode = '%02x%02x%02x' % (rgbvalues[0], rgbvalues[1], rgbvalues[2])
        
        if hexcode.startswith('#'):
            hexcode = hexcode[1:]
        elif hexcode.startswith('0x'):
            hexcode = hexcode[2:]
        
        if not len(hexcode) == 6:
            raise ValueError(f'{hexcode} is not a valid hexcode.')
        for code in hexcode:
            if not code.lower() in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f']:
                raise ValueError(f'{hexcode} is not a valid hexcode.')

        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://some-random-api.ml/canvas/colorviewer?hex={hexcode}&key={self.api_key}') as session_color:
                return BytesIO(await session_color.read())

    async def pokemon(self, name: str = None, pokemon_id: str = None, did_you_mean = False) -> dict:
        '''
        # Pokemon info
        Parameters -\n
            `name` (type str) (default None)
            `pokemon_id` (type str) (default None) (format - '001', '002', '101' etc)
            `did_you_mean` (type bool) (YOU NEED A TIER 1 OR ABOVE API KEY FOR THIS ARGUMENT TO BE TRUE) (default False)
        `Both name and pokemon_id cannot be specified/not None. Both name and pokemon_id cannot be unspecified/None. Only pass in either the name or the pokemon_id.`\n
        Did you mean argument -\n
            If `did_you_mean` is True,
            If `name` is specified/not None,
            If you have a tier 1 or above API key,
            If `name` got a misspelled pokemon name,
            The function returns the closest pokemon match it could find to `name`, along with the percentage of how accurate your spelling was.
        Returns -\n
            All the details of the specified pokemon (type dict)
            {'name': 'pokemon name', 'id': 'pokemon id', 'type': [types], 'species': [species], 'abilities': [abilities], 'height': 'pokemon height', 'weight': 'pokemon weight', 'base_experience': 'pokemon base_exp',
            'gender': [genders], 'egg_groups': [egg_groups], 'stats': {pokemon_stats}, 'sprites': {pokemon_image_gif_sprites}, 'description': 'pokemon_description', 'generation': 'pokemon_generation'}
            If the pokemon was misspelled and all the criteria of the above `did_you_mean` argument was passed - the function returns the closest pokemon match it could find to `name`, along with the percentage of how accurate your spelling was (type list).
        Raises -\n
            TypeError - if both `name` and `pokemon_id` are None/undefined, if both `name` and `pokemon_id` are not None/defined.
            ValueError - an invalid name for a pokemon was passed (and did_you_mean was False), an invalid ID for a pokemon was passed.
            SRApi.ApiKeyError - if `did_you_mean` was True and your API key was None/invalid/too low.
        '''
        if (did_you_mean is True) and (self.api_key is None):
            raise ApiKeyError('A Tier-1 or above API key is required for the did_you_mean argument to be set to True. To get an API key visit https://some-random-api.ml/docs/Welcome/Keys.')

        if (name is None) and (pokemon_id is None):
            raise TypeError('Either specify the name of the pokemon using name = \'name\' or the ID of the pokemon using pokemon_id = \'id\'.')
        
        if (name is not None) and (pokemon_id is not None):
            raise TypeError('Both name and pokemon_id cannot be specified, either specify the name of the pokemon using name = \'name\' or the ID of the pokemon using pokemon_id = \'id\'.')

        if (pokemon_id is not None) and (did_you_mean is True):
            raise TypeError('The did_you_mean argument cannot be True if only pokemon_id is specified, since pokemon_id cannot be checked and corrected for spelling')

        if name is not None:
            argument = f'pokemon={name.lower()}'
        elif pokemon_id is not None:
            argument = f'id={pokemon_id}'

        name = await self.aio_quote(name, safe = '')
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://some-random-api.ml/pokedex?{argument}{self.formatted_api_key}') as session_poke:
                jsondata = await session_poke.json()
        try:
            if jsondata['error'] == 'Sorry, I could not find that pokemon':
                if did_you_mean is True:
                    try:
                        if not jsondata['dym'] == '':
                            return jsondata['dym']
                        else:
                            return ['unidentified dym', '0%']
                    except KeyError:
                        await self.errorhandler(jsondata)
                if argument.startswith('id='):
                    raise ValueError(f'{pokemon_id} is not a valid ID for a pokemon.')
                elif argument.startswith('pokemon='):
                    raise ValueError(f'{name.capitalize()} is not a valid name for a pokemon.')
        except KeyError:
            return {'name': jsondata['name'],
                    'id': jsondata['id'],
                    'type': jsondata['type'],
                    'species': jsondata['species'],
                    'abilities': jsondata['abilities'],
                    'height': jsondata['height'],
                    'weight': jsondata['weight'],
                    'base_experience': jsondata['base_experience'],
                    'gender': jsondata['gender'],
                    'egg_groups': jsondata['egg_groups'],
                    'stats': jsondata['stats'],
                    'family': jsondata['family'],
                    'sprites': jsondata['sprites'],
                    'description': jsondata['description'],
                    'generation': jsondata['generation']
                }

    async def welcomeGoodbyeMessage(self, avatar: str, username: str, discriminator: str, guild_name: str, membercount: int, template: int = 1, background: str = 'space', type_of_message: str = 'join', textcolor: str = 'white') -> BytesIO:
        '''
        # Welcome/Goodbye image. Note that this function is related to Discord.
        Parameters -\n
            `background` (type str) (case-insensitive) (default 'space')
            `template` (type int) (must be 1, 2, 3 or 4) (default 1)
            `type_of_message` (type str) (case-insensitive) (must be 'join' or 'leave') (default 'join')
            `avatar` (type str) (case-sensitive) (must be a direct image link, formats - JPEG, JPG, PNG, GIF.)
            `username` (type str) (case-sensitive) (max len 30)
            `discriminator` (type str) (format - '0001', '9999' etc)
            `textcolor` (type str) (case-insensitive) (default 'white')
            `guild_name` (type str) (not shown as of now, will be used later)
            `membercount` (type int)
        `The background argument must be one of the elements from this list - stars, stars2, rainbowgradient, rainbow, sunset, night, blobday, blobnight, space (default), gaming1, gaming2, gaming3, gaming4.`\n
        `The textcolor argument must be one of the elements from this list - red, orange, yellow, green, blue, indigo, purple, pink, black, white (default).`\n
        Returns -\n
            if `type_of_message` is `join`: A picture welcoming a member with the name `username`#`discriminator` and with the avatar `avatar`, with the background `background` and so on (type BytesIO).
            if `type_of_message` is `leave`: A picture saying goodbye to a member with the name `username`#`discriminator` and with the avatar `avatar`, with the background `background` and so on (type BytesIO).
        Raises -\n
            ValueError - if the arguments were not right (see above for argument specifications).
            SRApi.InvalidURL - if `avatar` had an invalid, non-image URL.
        '''
        if not template in [1, 2, 3, 4]:
            raise ValueError('The template argument must be 1, 2, 3 or 4.')
        
        if not background.lower() in ['stars', 'stars2', 'rainbowgradient', 'rainbow', 'sunset', 'night', 'blobday', 'blobnight', 'space', 'gaming1', 'gaming2', 'gaming3', 'gaming4']:
            raise ValueError(f'The background argument must be in this list:  ["stars", "stars2", "rainbowgradient", "rainbow", "sunset", "night", "blobday", "blobnight", "space", "gaming1", "gaming2", "gaming3", "gaming4"].')
        
        if not type_of_message.lower() in ['join', 'leave']:
            raise ValueError('The type_of_message argument can either be \'join\' or \'leave\'.')

        if len(username) > 30:
            raise ValueError('The username can be at maximum 30 characters.')
        
        if not len(discriminator) == 4:
            raise ValueError('That is not a valid discriminator. A valid discriminator is a number between 0001-9999')
        else:
            for num in discriminator:
                if not num.isnumeric():
                    raise ValueError('That is not a valid discriminator. A valid discriminator is a number between 0001-9999')

        if not textcolor.lower() in ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple', 'pink', 'black', 'white']:
            raise ValueError(f'The textcolor argument must be in this list: ["red", "orange", "yellow", "green", "blue", "indigo", "purple", "pink", "black", "white"].')

        avatar = await self.aio_quote(avatar, safe = '')
        username = await self.aio_quote(username, safe = '')
        guild_name = await self.aio_quote(guild_name, safe = '')
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://some-random-api.ml/welcome/img/{template}/{background.lower()}?type={type_of_message.lower()}&avatar={avatar}&username={username.replace(" ", "%20")}&discriminator={discriminator}&textcolor={textcolor.lower()}&guildName={guild_name.replace(" ", "%20")}&memberCount={membercount}{self.formatted_api_key}') as session_welc:
                try:
                    jsondata = await session_welc.json()
                    await self.errorhandler(jsondata, ['avatar'])
                except aiohttp.ContentTypeError:
                    return BytesIO(await session_welc.read())

    async def premiumWelcomeGoodbye(self, background_link: str, avatar: str, username: str, discriminator: str, guildname: str, membercount: int, template: int = 1, type_of_message: str = 'join', textcolor: str = 'white') -> BytesIO:
        '''
        # Premium Welcome/Goodbye image. Note that this function is related to Discord.
        `This function requires a Tier 2 or above API Key to use.`\n
        Perks of premium over normal -\n
            You can add a custom linked background.
        Parameters -\n
            `background_link` (type str) (case-insensitive) (must be a direct image link, formats - JPEG, JPG, PNG, GIF) (preferably 1200 x 600.)
            `template` (type int) (must be 1, 2, 3 or 4) (default 1)
            `type_of_message` (type str) (case-insensitive) (must be 'join' or 'leave') (default 'join')
            `avatar` (type str) (case-sensitive) (must be a direct image link, formats - JPEG, JPG, PNG, GIF.)
            `username` (type str) (case-sensitive) (max len 30)
            `discriminator` (type str) (format - '0001', '9999' etc)
            `textcolor` (type str) (case-insensitive) (default 'white')
            `guild_name` (type str) (not shown as of now, will be used later)
            `membercount` (type int)
            `api_key` (type str) (in class initialization, not a function parameter)
        `The textcolor argument must be one of the elements from this list - red, orange, yellow, green, blue, indigo, purple, pink, black, white (default).`\n
        Returns -\n
            if `type_of_message` is `join`: A picture welcoming a member with the name `username`#`discriminator` and with the avatar `avatar`, with the background `background` and so on (type BytesIO).
            if `type_of_message` is `leave`: A picture saying goodbye to a member with the name `username`#`discriminator` and with the avatar `avatar`, with the background `background` and so on (type BytesIO).
        Raises -\n
            ValueError - if the arguments were not right (see above for argument specifications).
            SRApi.InvalidURL - if `avatar` had an invalid URL, if `background_link` had an invaid URL.
            SRApi.ApiKeyError - if your API key is None/invalid/too low.
        '''
        if self.api_key is None:
            raise ApiKeyError('A Tier-2 or above API key is required for this function. To get an API key visit https://some-random-api.ml/docs/Welcome/Keys.')
        
        if not template in [1, 2, 3, 4]:
            raise ValueError('The template argument must be 1, 2, 3 or 4.')
        
        if not type_of_message.lower() in ['join', 'leave']:
            raise ValueError('The type_of_message argument can either be \'join\' or \'leave\'.')

        if len(username) > 30:
            raise ValueError('The username can be at maximum 30 characters.')

        if not len(discriminator) == 4:
            raise ValueError('That is not a valid discriminator. A valid discriminator is a number between 0001-9999')
        else:
            for num in discriminator:
                if not num.isnumeric():
                    raise ValueError('That is not a valid discriminator. A valid discriminator is a number between 0001-9999')

        if not textcolor.lower() in ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple', 'pink', 'black', 'white']:
            raise ValueError(f'The textcolor argument must be in this list: ["red", "orange", "yellow", "green", "blue", "indigo", "purple", "pink", "black", "white"].')

        background_link = await self.aio_quote(background_link, safe = '')
        avatar = await self.aio_quote(avatar, safe = '')
        username = await self.aio_quote(username, safe = '')
        guildname = await self.aio_quote(guildname, safe = '')
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://some-random-api.ml/premium/welcome/{template}?type={type_of_message.lower()}&avatar={avatar}&username={username.replace(" ", "%20")}&discriminator={discriminator}&bg={background_link}&textcolor={textcolor.lower()}&guildName={guildname.replace(" ", "%20")}&memberCount={membercount}&key={self.api_key}') as session_premiumwelc:
                try:
                    jsondata = await session_premiumwelc.json()
                    await self.errorhandler(jsondata, ['avatar', 'background_link'])
                except aiohttp.ContentTypeError:
                    return BytesIO(await session_premiumwelc.read())   

    async def rankcard(self, username: str, discriminator: str, current_xp: int, needed_xp: int, level: int, avatar: str, background_color: str = None, exp_bar_color: str = None, bar_color: str = None, background_link: str = None, rank: int = None, template: int = 3, text_color: str = 'ffffff') -> BytesIO:
        '''
        # Rankcard image for discord levelling bots. This function is related to discord.
        `This function requires a Tier-1 or above API key to use`\n
        Parameters -\n
            `template` (type int) (must be 1, 2, 3, 4 or 5) (default 3)
            `username` (type str) (case-sensitive) (max len 20)
            `discriminator` (type str) (must be numeric) (format - 0001, 9999 etc)
            `current_xp` (type int) (shows up as `current_xp` / `needed_xp` XP)
            `needed_xp` (type int) (shows up as `current_xp` / `needed_xp` XP)
            `level` (type int)
            `avatar` (type str) (case-sensitive) (must be a direct image link, formats - JPEG, JPG, PNG, GIF.)
            `api_key` (type str) (in class initialization, not a function parameter)

            `rank` (type int) (optional) (default None)
            `background_color` (type str) (optional) (default None) (a hexcode, in these formats - '#ffffff', '0xffffff', 'ffffff')
            `exp_bar_color` (type str) (optional) (default None) (a hexcode, in these formats - '#ffffff', '0xffffff', 'ffffff')
            `bar_color` (type str) (optional) (default None) (a hexcode, in these formats - '#ffffff', '0xffffff', 'ffffff')
            `text_color` (type str) (optional) (default 'ffffff', equivalent to None) (a hexcode, in these formats - '#ffffff', '0xffffff', 'ffffff') (do not explicitly set this argument as None)
            `background_link` (type str) (optional) (a link to a background image for the rank card. Supported formats - PNG, JPG, JPEG and GIF.) (This overwrites `background_color` in any other `template` except 4.) (YOU NEED A TIER 2 KEY TO USE THIS)
        Returns -\n
            A levelling rankcard picture with the name `username#discriminator`, with the template `template`, with the level details `current_xp, needed_xp, level, rank`, with the avatar `avatar` and so on.
        Raises -\n
            ValueError - if the arguments provided were invalid.
            SRApi.InvalidURL - if `avatar` had an invalid, non-image URL.
            SRApi.ApiKeyError - if your api key is None/unspecified, invalid, or too low in tier (for the `background_link` parameter).
        '''
        if self.api_key is None:
            raise ApiKeyError('A Tier-1 or above API key is required for this function. To get an API key visit https://some-random-api.ml/docs/Welcome/Keys.')

        if not template in [1, 2, 3, 4, 5]:
            raise ValueError('The template argument must be 1, 2, 3, 4 or 5.')

        if len(username) > 32:
            raise ValueError('The username can be at maximum 32 characters.')

        if not len(discriminator) == 4:
            raise ValueError('That is not a valid discriminator. A valid discriminator is a number between 0001-9999')
        else:
            for num in discriminator:
                if not num.isnumeric():
                    raise ValueError('That is not a valid discriminator. A valid discriminator is a number between 0001-9999')

        if text_color.startswith('#'):
            text_color = text_color[1:]
        elif text_color.startswith('0x'):
            text_color = text_color[2:]
        if not len(text_color) == 6:
            raise ValueError(f'{text_color} is not a valid hexcode.')
        for code in text_color:
            if not code.lower() in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f']:
                raise ValueError(f'{text_color} is not a valid hexcode.')

        if not background_color is None:
            if background_color.startswith('#'):
                background_color = background_color[1:]
            elif background_color.startswith('0x'):
                background_color = background_color[2:]
            if not len(background_color) == 6:
                raise ValueError(f'{background_color} is not a valid hexcode.')
            for code in background_color:
                if not code.lower() in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f']:
                    raise ValueError(f'{background_color} is not a valid hexcode.')

        if not exp_bar_color is None:
            if exp_bar_color.startswith('#'):
                exp_bar_color = exp_bar_color[1:]
            elif exp_bar_color.startswith('0x'):
                exp_bar_color = exp_bar_color[2:]
            if not len(exp_bar_color) == 6:
                raise ValueError(f'{exp_bar_color} is not a valid hexcode.')
            for code in exp_bar_color:
                if not code.lower() in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f']:
                    raise ValueError(f'{exp_bar_color} is not a valid hexcode.')

        if not bar_color is None:
            if bar_color.startswith('#'):
                bar_color = bar_color[1:]
            elif bar_color.startswith('0x'):
                bar_color = bar_color[2:]
            if not len(bar_color) == 6:
                raise ValueError(f'{bar_color} is not a valid hexcode.')
            for code in bar_color:
                if not code.lower() in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f']:
                    raise ValueError(f'{bar_color} is not a valid hexcode.')

        username = await aio_quote(username, safe = '')
        avatar = await aio_quote(avatar, safe = '')
        if background_link is not None:
            if self.api_key is None:
                raise ApiKeyError('A Tier-2 or above API key is required for this function. To get an API key visit https://some-random-api.ml/docs/Welcome/Keys.')
            background_link = await aio_quote(background_link, safe = '')

        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://some-random-api.ml/premium/rankcard/{template}?username={username}&discriminator={discriminator}&cxp={current_xp}&nxp={needed_xp}&level={level}{"&rank=" + str(rank) if not rank is None else ""}&avatar={avatar}&key={self.api_key}&ctext={text_color}{"&cbg=" + background_color if not background_color is None else ""}{"&ccxp=" + exp_bar_color if not exp_bar_color is None else ""}{"&cbar=" + bar_color if not bar_color is None else ""}{"&bg=" + background_link if not background_link is None else ""}') as session_rankcard:
                try:
                    jsondata = await session_rankcard.json()
                    await self.errorhandler(jsondata, ['avatar'])
                except JSONDecodeError:
                    return BytesIO(await session_rankcard.read())

class SRAPI:
    '''
    # Synchronous class wrapper
    `This is the class that contains all the synchronous/normal functions for Some Random API.`\n
    Use the `dir()` method on this class to see all its functions in a list (ignore the `__double_underscore_builtins__`)\n
    Parameters -\n
        `api_key` (type str) (default None)
        `warnings` (type bool) (default True) (defining it as False disables warnings about functions you might get through printing)
    Usage-\n
        Make a new instance of this class with the parameters above,
        Use it's functions using `your_class_instance.function_name()`
    The class for using the asynchronous API wrapper class is `AioSRAPI()`.
    '''
    def __init__(self, api_key: str = None, warnings: bool = True):
        self.api_key = api_key
        if not api_key is None:
            self.formatted_api_key = f'&key={api_key}'
        else:
            self.formatted_api_key = ''

    def errorhandler(self, jsondata, other_args: list = None) -> None:
        '''
        # Error handling
        A function for private use, a global error handler to raise the right errors in right situations.\n
        Returns - None.\n
        Raises - Errors depending on the error message recieved from the API.
        '''
        try:
            e = jsondata['error']
        except KeyError:
            return

        if (e == 'avatar is not a valid url') or (e == 'Image given has not completed loading') or (e == 'Internal image has not completed loading'):
            if other_args[1] == 'background_link':
                raise InvalidUrl(f'The {other_args[0]} or {other_args[1]} argument is an invalid, non-image URL. The URL only supports JPG, JPEG, PNG or GIF files. Also use HTTPS links only and not HTTP.')
            raise InvalidUrl(f'The {other_args[0]} argument is an invalid, non-image URL. The URL only supports JPG, JPEG, PNG or GIF files. Also use HTTPS links only and not HTTP.')

        elif (e == 'Your key isn\'t able to use this endpoint, please consider upgrading your key') or (e == 'Invalid key') or (e == 'Your key has expired'):
            raise ApiKeyError(f'{self.api_key} is not a valid key/is an expired key/is a key of too low tier. Get a valid key at https://some-random-api.ml/docs/Welcome/Keys. Type -vote and follow the instructions.')

        elif (e == 'Too many requests, please try again later.'):
            raise HTTPError('Too many requests are being sent to the API, please try again later. You are being ratelimited. Try sleeping/waiting for sometime.')

        else:
            raise HTTPError(f'{jsondata["error"]}')

    def keycheck(self):
        '''
        # Check your key
        `Checks your API key and returns your key\'s details`\n
        Parameters -\n
            `api_key` (type str) (in class initialization, not a function parameter)
        Returns -\n
            Your key's details (type dict)
            {'id': 'your key\'s id', 'tier': your key\'s tier (type int), 'end': when your key ends (type int) (format - number of milliseconds from `January 1st, 1970 00:00:00 GMT`)}
        Raises -\n
            SRApi.ApiKeyError - If the key you provided is an invalid key, or it is None/unspecified
        '''
        if self.api_key is None:
            raise ApiKeyError('An API key is required for this function. To get an API key visit https://some-random-api.ml/docs/Welcome/Keys.')
        
        if self.warnings is True:
            print('Warning: Do not use this function often as it has a very high ratelimit (you can only use it 10 times per minute)\nThese warnings can be turned off in the class initialisation (warnings = False).')

        jsondata = requests.get(f'https://some-random-api/key/check?key={self.api_key}').json()
        try:
            return {
                'id': jsondata['id'],
                'tier': jsondata['tier'],
                'end': jsondata['end']
            }
        except KeyError:
            if jsondata['error'] == 'No user found with that key':
                raise ApiKeyError('The API key you have given is invalid/expired. To get an API key visit https://some-random-api.ml/docs/Welcome/Keys.')
            self.errorhandler(jsondata)

    def fact(self, type_of_fact: str) -> str:
        '''
        # Random fact
        Parameters - \n
            `type_of_fact` (type str) (case-insensitive)\n
        `type_of_fact` must be one of the elements from this list: `dog, cat, panda, fox, bird (alias - birb), koala, kangaroo, racoon (alias - raccoon), elephant, giraffe, whale`.\n
        Returns -\n
            A random fact about the category you provided (type str).\n
        Raises -\n
            ValueError, if the `type_of_fact` category is not from the list above.
        '''
        if not type_of_fact.lower() in ['dog', 'cat', 'panda', 'fox', 'bird', 'birb', 'koala', 'kangaroo', 'racoon', 'raccoon', 'elephant', 'giraffe', 'whale']:
            raise ValueError('The only type of facts that are provided are dog, cat, panda, fox, bird (alias - birb), koala, kangaroo, racoon (alias - raccoon), elephant, giraffe, whale.')
    
        return requests.get(f'https://some-random-api.ml/facts/{type_of_fact.lower()}?key={self.api_key}').json()['fact']

    def image(self, type_of_image: str) -> str:
        '''
        # Random image link
        Parameters - \n
            `type_of_image` (type str) (case-insensitive)\n
        `type_of_image` must be one of the elements from this list: `dog, cat, panda, red_panda, bird (alias - birb), fox, koala, racoon (alias - raccoon), kangaroo, whale, pikachu`.\n
        Returns -\n
            A link to a random image with the category you provided (type str).\n
        Raises -\n
            ValueError, if the `type_of_image` category is not from the list above.
        '''
        if not type_of_image.lower() in ['dog', 'cat', 'panda', 'red_panda', 'birb', 'bird', 'fox', 'koala', 'racoon', 'raccoon', 'kangaroo', 'whale', 'pikachu']:
            raise ValueError('The only types of images that are provided are dog, cat, panda, red_panda, bird (alias - birb), fox, koala, racoon (alias- raccoon), kangaroo, whale, pikachu.')
        
        return requests.get(f'https://some-random-api.ml/img/{type_of_image.lower()}?key={self.api_key}').json()['link']

    def gif(self, type_of_gif: str) -> str:
        '''
        # Random gif link
        Parameters - \n
            `type_of_gif` (type str) (case-insensitive)\n
        `type_of_gif` must be one of the elements from this list: `wink, pat, hug, face-palm`.\n
        Returns -\n
            A link to a random gif with the category you provided (type str).\n
        Raises -\n
            ValueError, if the `type_of_gif` category is not from the list above.
        '''
        if not type_of_gif.lower() in ['wink', 'pat', 'hug', 'face-palm']:
            raise ValueError('The only types of gifs that are provided are wink, pat, hug, face-palm.')
        
        return requests.get(f'https://some-random-api.ml/animu/{type_of_gif.lower()}?key={self.api_key}').json()['link']

    def animeQuote(self) -> dict:
        '''
        # Random anime quote
        Returns -\n
            A random anime quote with it's details (type dict)
            {'character': 'the character that said the quote', 'anime': 'the anime from where the quote is from', 'quote': 'the quote'}
        '''
        jsondata = requests.get(f'https://some-random-api.ml/animu/quote?key={self.api_key}').json()
        return {
            'character': jsondata['characther'],
            'anime': jsondata['anime'],
            'quote': jsondata['sentence']
        }

    def stringSimilarity(self, string1: str, string2: str) -> str:
        '''
        # Compares two strings to check similarity%
        Parameters -\n
            string1 (type str)
            string2 (type str)
        Returns -\n
            The strings' similarity% (type int)
        '''
        string1 = quote(string1, safe = '')
        string2 = quote(string2, safe = '')
        return requests.get(f'https://some-random-api.ml/stringsimilarity?string1={string1.replace(" ", "%20")}&string2={string2.replace(" ", "%20")}&key={self.api_key}').json()['similarity'] * 100

    def overlay(self, type_of_overlay: str, image_to_overlay: str) -> BytesIO:
        '''
        # Image overlays
        Parameters - \n
            `type_of_overlay` (type str) (case-insensitive), 
            `image_to_overlay` (type str) (case-sensitive)\n
        `type_of_overlay` must be one of the elements from this list: `gay, glass, wasted, triggered, jail`.\n
        `image_to_overlay` must be a direct URL to an image link. Supported image formats - JPG, JPEG, PNG, GIF.\n
        Returns -\n
            if `type_of_overlay` is `gay` - An image in BytesIO form with a rainbow overlay on it (type BytesIO).
            if `type_of_overlay` is `glass` - An image in BytesIO form with a glass-like white overlay on it (type BytesIO).
            if `type_of_overlay` is `wasted` - An image in BytesIO form with the text "wasted" in red colour on a grey version of your original picture (type BytesIO).
            if `type_of_overlay` is `triggered` - A GIF in BytesIO form which has a red-yellow angry shaking overlay on your original picture with the text "Triggered" at the bottom of the GIF (type BytesIO).
            if `type_of_overlay` is `jail` - An image in BytesIO form with jail-cell bars on top of a grey version of your original picture (type BytesIO).
            if `type_of_overlay` is `comrade` - An image in BytesIO form with a red-like overlay and a yellow communist symbol on it.
        Raises -\n
            ValueError, if the `type_of_fact` category is not from the list specified above.
            SRApi.InvalidURL, if the `image_to_overlay` argument\'s URL is invalid.
        '''
        if not type_of_overlay.lower() in ['gay', 'glass', 'wasted', 'triggered', 'jail', 'comrade']:
            raise ValueError('The only types of overlays that are provided are gay, glass, wasted, triggered, jail, comrade.')

        data = requests.get(f'https://some-random-api.ml/canvas/{type_of_overlay.lower()}?avatar={image_to_overlay}&key={self.api_key}')
        image_to_overlay = quote(image_to_overlay, safe = '')
        try:
            jsondata = data.json()
            self.errorhandler(jsondata, ['image_to_overlay'])
        except JSONDecodeError:
            return BytesIO(data.content)

    def lyrics(self, search_query: str) -> dict:
        '''
        # Lyrics to a song
        Parameters - \n
            `search_query` (type str) (case-insensitive)\n
        It is recommended to have the song title in the `search_query` argument and not just the composer of the song.\n
        Returns -\n
            Lyrics to the song you asked for (type str).\n
        Raises -\n
            ValueError, if the lyrics to the song you were looking for couldn\'t be found.
        '''
        search_query = quote(search_query, safe = '')
        jsondata = requests.get(f'https://some-random-api.ml/lyrics?title={search_query.lower().replace(" " , "%20")}&key={self.api_key}').json()
        try:
            if jsondata['error'] == 'Sorry I couldn\'t find that song\'s lyrics':
                raise ValueError(f'{search_query}\'s lyrics couldn\'t be found.')
            self.errorhandler(jsondata)
        except KeyError:
            return {'title' : jsondata['title'], 
                'author': jsondata['author'] , 
                'lyrics' : jsondata['lyrics'], 
                'thumbnail': jsondata['thumbnail']['genius'], 
                'links' : jsondata['links']['genius']}

    def base64(self, base64_action: str, base64_text: str) -> str:
        '''
        # Base64 encoding and decoding
        Parameters-\n
            `base64_action` (type str) (case-insensitive)
            `base64_text` (type str) (case-sensitive)
        `base64_action` must be one of the elements from this list: `encode, decode`.\n
        Returns-\n
            if `base64_action` is `encode` - A base64 encoded version of `base64_text` (type str).
            if `base64_action` is `decode` - A base64 decoded version of `base64_text` (type str).
        Raises -\n
            ValueError, if `base64_action` is not from the list specified above.
        '''
        if not base64_action.lower() in ['encode', 'decode']:
            raise ValueError('The only actions supported for base64 are encode, decode.')
        
        base64_text = quote(base64_text, safe = '')
        jsondata = requests.get(f'https://some-random-api.ml/base64?{base64_action.lower()}={base64_text}&key={self.api_key}').json()
        if base64_action.lower() == 'encode':
            return jsondata['base64']
        return jsondata['text']

    def binary(self, binary_action: str, binary_text: str) -> str:
        '''
        # Binary encoding and decoding
        Parameters-\n
            `binary_action` (type str) (case-insensitive)
            `binary_text` (type str) (case-sensitive)
        `binary_action` must be one of the elements from this list: `encode, decode`.\n
        Returns-\n
            if `binary_action` is `encode` - A binary encoded version of `binary_text` (type str).
            if `binary_action` is `decode` - A binary decoded version of `binary_text` (type str).
        Raises -\n
            ValueError, if `binary_action` is not from the list specified above.
        '''
        if not binary_action.lower() in ['encode', 'decode']:
            raise ValueError('The only actions supported for binary are encode, decode.')
        
        binary_text = quote(binary_text, safe = '')
        jsondata = requests.get(f'https://some-random-api.ml/binary?{binary_action.lower()}={binary_text}&key={self.api_key}').json()
        if binary_action.lower() == 'encode':
            return jsondata['binary']
        else:
            return jsondata['text']

    def joke(self) -> str:
        '''
        # Random joke
        Returns - A random joke from the API (type str).
        '''
        return requests.get(f'https://some-random-api.ml/joke?key={self.api_key}').json()['joke']

    def minecraft(self, mc_username: str) -> dict:
        '''
        # Minecraft profile details
        Parameters -\n
            `mc_username` (type str) (case-insensitive)
        Returns -\n
            `mc_username`\'s Minecraft profile details (type dict)
            {'username': 'The username of the player', 'uuid': 'The UUID of the player, 'name_history': [The name history of the player]}
        Raises -\n
            ValueError, if the username provided is invalid.
        '''
        if self.warnings is True:
            print('Warning: if you entered a correct username and you still get an invalid username error, then the API is ratelimited.\nThese warnings can be turned off in the class initialisation (warnings = False).')
        
        mc_username = quote(mc_username, safe = '')
        jsondata = requests.get(f'https://some-random-api.ml/mc?username={mc_username.lower()}&key={self.api_key}').json()
        try:
            return {'username' : jsondata['username'],
                'uuid' : jsondata['uuid'],
                'name_history' : jsondata['name_history']
                }
        except KeyError:
            raise ValueError('The Minecraft username you entered is invalid.')

    def meme(self) -> dict:
        '''
        # Random meme
        Returns -\n
            A random meme (type dict)
            {'id': the id of the meme, 'image': 'a link to the image of the meme', 'caption': 'the meme\'s caption', 'category': 'the category of the meme'}
        '''
        
        jsondata = requests.get(f'https://some-random-api.ml/meme?key={self.api_key}').json()
        return {'id' : jsondata['id'],
                'image' : jsondata['image'],
                'caption' : jsondata['caption'],
                'category' : jsondata['category']}

    def chatbot(self, chatbot_message: str, user_id: str = None) -> str:
        '''
        # An AI that responds to your statements
        `API Key of Tier 1 or above required to use this function`\n
        Parameters -\n
            `chatbot_message` (type str)
            `user_id` (type str) (default None) (this parameter can be anything that can be converted to string, it is just there so the API can link a user_id to a particular user)
            `api_key` (type str) (in class initialization, not a function parameter)
        Returns -\n
            An AI response to `chatbot_message` (type str)
        Raises -\n
            SRApi.ApiKeyError - If your API key is invalid or if your API key is not provided/is None.
        '''
        if self.api_key is None:
            raise ApiKeyError('A Tier-1 or above API key is required for this function. To get an API key visit https://some-random-api.ml/docs/Welcome/Keys.')
        
        chatbot_message = quote(chatbot_message, safe = '')
        user_id = quote(user_id, safe = '')
        jsondata = requests.get(f'https://some-random-api.ml/chatbot?message={chatbot_message.lower().replace(" ", "%20")}&key={self.api_key}').json()
        try:
            return jsondata['response']
        except KeyError:
            self.errorhandler(jsondata)

    def rgbToHex(self, r: int, g: int, b: int) -> str:
        '''
        # RGB color values to hexcodes
        Parameters -\n
            `r` (red value) (type int) (must be between 0 and 255, 0, 255 included)
            `g` (green value) (type int) (must be between 0 and 255, 0, 255 included)
            `b` (blue value) (type int) (must be between 0 and 255, 0, 255 included)
        Returns -\n
            The hexcode for the RGB values provided (type str) (format - ffffff).
        Raises -\n
            ValueError, if any of the parameters are not in the range 0-255.
        '''
        for color in [r, g, b]:
            if not color in list(range(0, 256)):
                raise ValueError('The red, blue and green parameters must at minimum 0 or at maximum 255.')
        return requests.get(f'https://some-random-api.ml/canvas/hex?rgb={r},{g},{b}&key={self.api_key}').json()

    def hexToRgb(self, hexcode: str) -> dict:
        '''
        # Hexcode color values to RGB values
        Parameters -\n
            `hexcode` (case-insensitive), in one of these formats - '#ffffff', '0xffffff', 'ffffff' (type str)
        Returns -\n
            RGB values for the hexcode (type dict)
            {'r': red_value, 'g': green_value, 'b': blue_value}
        Raises -\n
            ValueError, if you entered an invalid hexcode
        '''
        if hexcode.startswith('#'):
            hexcode = hexcode[1:]
        elif hexcode.startswith('0x'):
            hexcode = hexcode[2:]
        if not len(hexcode) == 6:
            raise ValueError(f'{hexcode} is not a valid hexcode. Types of hexcode that are supported - ffffff, #ffffff, 0xffffff.')
        for code in hexcode:
            if not code in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f']:
                raise ValueError(f'{hexcode} is not a valid hexcode. Types of hexcode that are supported - ffffff, #ffffff, 0xffffff.')
        
        jsondata = requests.get(f'https://some-random-api.ml/canvas/rgb?hex={hexcode}&key={self.api_key}').json()
        return {'r' : jsondata['r'],
                'g' : jsondata['g'],
                'b' : jsondata['b']}

    def filter(self, type_of_filter: str, image: str) -> BytesIO:
        '''
        # Filter an image
        Parameters -\n
            `type_of_filter` (type str) (case-insensitive).
            `image` (type str) (case-sensitive) (A link to the image you want to filter).
        `type_of_filter` must be one of the elements from this list - `greyscale, invert, brightness, threshold, sepia, red, green, blue, blurple, pixelate, blur, jpg`\n
        Returns -\n
            An image in BytesIO form manipulated according to the filter you provided.
        Raises -\n
            ValueError, if the `type_of_filter` argument is not from the list specified above.
            SRApi.InvalidURL, if the `image` argument is an invalid, non-image URL.
        '''
        if not type_of_filter.lower() in ['greyscale', 'invert', 'brightness', 'threshold', 'sepia', 'red', 'green', 'blue', 'blurple', 'pixelate', 'blur', 'jpg']:
            raise ValueError('The only types of filters that are provided are greyscale, invert, brightness, threshold, sepia, red, green, blue, blurple, pixelate, blur, jpg.')
        
        image = quote(image, safe = '')
        data = requests.get(f'https://some-random-api.ml/canvas/{type_of_filter.lower()}?avatar={image}&key={self.api_key}')
        try:
            jsondata = data.json()
            self.errorhandler(jsondata, ['image'])
        except JSONDecodeError:
            return BytesIO(data.content)

    def dbotToken(self) -> str:
        '''
        # Discord Bot Token. Note that this function is related to Discord.
        Returns - A randomly generated Discord Bot Token (type str).
        '''
        return requests.get(f'https://some-random-api.ml/bottoken?key={self.api_key}').json()['token']

    def amongUs(self, username: str, image: str, impostor: bool = choice([False, False, True, False, False])) -> BytesIO:
        '''
        # Among Us ejection GIF
        `API Key of Tier 1 or above required to use this function`\n
        Parameters -\n
            `username` (type str) (max len 20)
            `image` (type str) (a direct link to a PNG, JPG, JPEG or GIF file)
            `impostor` (type bool) (by default a 1/5 chance of showing impostor)
            `api_key` (type str) (in class initialization, not a function parameter)
        Returns -\n
            A GIF of your `image` URL in the form of an Among Us ejection (type BytesIO)
        Raises -\n
            SRApi.ApiKeyError - If your API key is invalid or if your API key is not provided/is None.
            ValueError - If the length of `username` is more than 20.
            SRApi.InvalidURL - If the `image` URL is invalid.
        '''
        if self.api_key is None:
            raise ApiKeyError('A Tier-1 or above API key is required for this function. To get an API key visit https://some-random-api.ml/docs/Welcome/Keys.')
        
        if len(username) > 20:
            raise ValueError('The username parameter must be at maximum 20 characters.')

        if self.warnings is True:
            print('Warning: This function takes time to process.\nThese warnings can be turned off in the class initialisation (warnings = False).')
        
        username = quote(username, safe = '')
        image = quote(image, safe = '')
        if impostor is True:
            impostor = 'true'
        elif impostor is False:
            impostor = 'false'

        data = requests.get(f'https://some-random-api.ml/premium/amongus?key={self.api_key}&username={username}&avatar={image}&impostor={impostor}')
        try:
            jsondata = data.json()
            self.errorhandler(jsondata, ['image_to_amongus'])
        except JSONDecodeError:
            return BytesIO(data.content)

    def petPet(self, image: str) -> BytesIO:
        '''
        # Pet Pet gif
        `API Key of Tier 1 or above required to use this function`\n
        Parameters -\n
            `image` (type str) (a direct link to a PNG, JPG, JPEG or GIF file)
            `api_key` (type str) (in class initialization, not a function parameter)
        Returns -\n
            A GIF of `image` being patted by a hand repeatedly.
        Raises -\n
            SRApi.InvalidURL - If `image` is an invalid, non-image URL.
            SRApi.ApiKeyError - If your API key is invalid or if your API key is not provided/is None.
        '''
        if self.api_key is None:
            raise ApiKeyError('A Tier-1 or above API key is required for this function. To get an API key visit https://some-random-api.ml/docs/Welcome/Keys.')
        
        image = quote(image, safe = '')
        data = requests.get(f'https://some-random-api.ml/premium/petpet?key={self.api_key}&avatar={image}')
        try:
            jsondata = data.json()
            self.errorhandler(jsondata, ['image'])
        except JSONDecodeError:
            return BytesIO(data.content)
        
    def youtubeComment(self, avatar: str, username: str, comment: str) -> BytesIO:
        '''
        # YouTube Comment Image
        Parameters -\n
            `avatar` (type str) (A direct link to a PNG, JPG, JPEG or GIF file)
            `username` (type str) (max len 25)
            `comment` (type str) (max len 1000)
        Returns -\n
            An image of a YouTube comment with `avatar` as the profile picture, `username` as the name and `comment` as the comment\'s content (type BytesIO).
        Raises -\n
            ValueError - if `username` is more than 25 characters or `comment` is more than 1000 characters.
            SRApi.InvalidURL - if `avatar` is an invalid, non-image URL.
        '''
        if len(username) > 25:
            raise ValueError('The length of the username argument must be at maximum 25 characters.')
        if len(comment) > 1000:
            raise ValueError('The length of the comment argument must be at maximum 1000 characters.')
        
        avatar = quote(avatar, safe = '')
        username = quote(username, safe = '')
        comment = quote(comment, safe = '')
        data = requests.get(f'https://some-random-api.ml/canvas/youtube-comment?avatar={avatar}&username={username}&comment={comment.replace(" ", "%20")}&key={self.api_key}')
        try:
            jsondata = data.json()
            self.errorhandler(jsondata, ['avatar'])
        except JSONDecodeError:
            return BytesIO(data.content)

    def simpCard(self, avatar: str) -> BytesIO:
        '''
        # Simp Card Image
        Parameters -\n
            `avatar` (type str) (A direct link to a PNG, JPG, JPEG or GIF file)
        Returns -\n
            An image with a card with the words "Simp card" on it with `avatar` on its left side (type BytesIO).
        Raises -\n
            SRApi.InvalidURL - If `avatar` is an invalid, non-image URL.
        '''
        data = requests.get(f'https://some-random-api.ml/canvas/simpcard?avatar={avatar}&key={self.api_key}')
        avatar = quote(avatar, safe = '')
        try:
            jsondata = data.json()
            self.errorhandler(jsondata, ['avatar'])
        except JSONDecodeError:
            return BytesIO(data.content)

    def hornyCard(self, avatar: str) -> BytesIO:
        '''
        # Horny Card Image
        Parameters -\n
            `avatar` (type str) (A direct link to a PNG, JPG, JPEG or GIF file)
        Returns -\n
            An image with a card with the words "License to be horny" on it with `avatar` on its left side (type BytesIO).
        Raises -\n
            SRApi.InvalidURL - If `avatar` is an invalid, non-image URL.
        '''
        
        avatar = quote(avatar, safe = '')
        data = requests.get(f'https://some-random-api.ml/canvas/horny?avatar={avatar}&key={self.api_key}')
        try:
            jsondata = data.json()
            self.errorhandler(jsondata, ['avatar'])
        except JSONDecodeError:
            return BytesIO(data.content)

    def loliceBearcop(self, avatar: str) -> BytesIO:
        '''
        # Horny Card Image
        Parameters -\n
            `avatar` (type str) (A direct link to a PNG, JPG, JPEG or GIF file)
        Returns -\n
            An image where `avatar` is pasted on a bear cop (type BytesIO).
        Raises -\n
            SRApi.InvalidURL - If `avatar` is an invalid, non-image URL.
        '''

        avatar = quote(avatar, safe = '')
        data = requests.get(f'https://some-random-api.ml/canvas/lolice?avatar={avatar}&key={self.api_key}')
        try:
            jsondata = data.json()
            self.errorhandler(jsondata, ['avatar'])
        except JSONDecodeError:
            return BytesIO(data.content)

    def itsSoStupid(self, avatar: str, text: str) -> BytesIO:
        '''
        # Its So Stupid Image
        Parameters -\n
            `avatar` (type str) (A direct link to a PNG, JPG, JPEG or GIF file)
            `text` (type str) (max len 20)
        Returns -\n
            An image with a dog saying `text` and someone calling it stupid (type BytesIO).
        Raises -\n
            ValueError - if `text` is more than 20 characters.
            SRApi.InvalidURL - if `avatar` is an invalid, non-image URL.
        '''
        if len(text) > 20:
            raise ValueError('The text argument must be at maximum 20 characters.')
        
        avatar = quote(avatar, safe = '')
        text = quote(text, safe = '')
        data = requests.get(f'https://some-random-api.ml/canvas/its-so-stupid?avatar={avatar}&dog={text.replace(" ", "%20")}&key={self.api_key}')
        try:
            jsondata = data.json()
            self.errorhandler(jsondata, ['avatar'])
        except JSONDecodeError:
            return BytesIO(data.content)

    def colorViewer(self, hexcode: str = None, rgbvalues: list = None) -> BytesIO:
        '''
        # Color viewer image
        Parameters -\n
            `hexcode` (type str) (must be in one of the following formats - '#ffffff', '0xffffff', 'ffffff') (default - None)
            `rgbvalues` (type list) (format - [red_value, green_value, blue_value]) (default - None)
        `If both values are unspecified/None, an error will be raised. If both values are specified/not None, an error will be raised. Only pass in either hexcode or rgbvalues to the function.`\n
        Returns -\n
            An image filled with the color you specified (type BytesIO).
        Raises -\n
            ValueError - if a valid color was not provided, if both values `hexcode` and `rgbvalues` are specified, if both values `hexcode` and `rgbvalues` are None/unspecified.
        '''
        if (hexcode is None) and (rgbvalues is None):
            raise ValueError('Either specify the hexcode using hexcode = \'hexcode\' or the RGB values in list form using rgbvalues = [red_value, green_value, blue_value].')

        if (hexcode is not None) and (rgbvalues is not None):
            raise ValueError('Both values cannot be specified. Either specify the hexcode using hexcode = \'hexcode\' or the RGB values in list form using rgbvalues = [red_value, green_value, blue_value].')
        
        if rgbvalues is not None:
            if not len(rgbvalues) == 3:
                raise ValueError('The RGB values given are invalid.')
            for value in rgbvalues:
                if not value in list(range(0,256)):
                    raise ValueError('The RGB values given are invalid.')
            hexcode = '%02x%02x%02x' % (rgbvalues[0], rgbvalues[1], rgbvalues[2])
        
        if hexcode.startswith('#'):
            hexcode = hexcode[1:]
        elif hexcode.startswith('0x'):
            hexcode = hexcode[2:]
        
        if not len(hexcode) == 6:
            raise ValueError(f'{hexcode} is not a valid hexcode.')
        for code in hexcode:
            if not code.lower() in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f']:
                raise ValueError(f'{hexcode} is not a valid hexcode.')

        return requests.get(f'https://some-random-api.ml/canvas/colorviewer?hex={hexcode}&key={self.api_key}').content

    def pokemon(self, name: str = None, pokemon_id: str = None, did_you_mean = False) -> dict:
        '''
        # Pokemon info
        Parameters -\n
            `name` (type str) (default None)
            `pokemon_id` (type str) (default None) (format - '001', '002', '101' etc)
            `did_you_mean` (type bool) (YOU NEED A TIER 2 OR ABOVE API KEY FOR THIS ARGUMENT TO BE TRUE) (default False)
        `Both name and pokemon_id cannot be specified/not None. Both name and pokemon_id cannot be unspecified/None. Only pass in either the name or the pokemon_id.`\n
        Did you mean argument -\n
            If `did_you_mean` is True,
            If `name` is specified/not None,
            If you have a tier 2 or above API key,
            If `name` got a misspelled pokemon name,
            The function returns the closest pokemon match it could find to `name`, along with the percentage of how accurate your spelling was.
        Returns -\n
            All the details of the specified pokemon (type dict)
            {'name': 'pokemon name', 'id': 'pokemon id', 'type': [types], 'species': [species], 'abilities': [abilities], 'height': 'pokemon height', 'weight': 'pokemon weight', 'base_experience': 'pokemon base_exp',
            'gender': [genders], 'egg_groups': [egg_groups], 'stats': {pokemon_stats}, 'sprites': {pokemon_image_gif_sprites}, 'description': 'pokemon_description', 'generation': 'pokemon_generation'}
            If the pokemon was misspelled and all the criteria of the above `did_you_mean` argument was passed - the function returns the closest pokemon match it could find to `name`, along with the percentage of how accurate your spelling was (type list).
        Raises -\n
            TypeError - if both `name` and `pokemon_id` are None/undefined, if both `name` and `pokemon_id` are not None/defined.
            ValueError - an invalid name for a pokemon was passed (and did_you_mean was False), an invalid ID for a pokemon was passed.
            SRApi.ApiKeyError - if `did_you_mean` was True and your API key was None/invalid/too low.
        '''
        if (did_you_mean is True) and (self.api_key is None):
            raise ApiKeyError('A Tier-2 or above API key is required for the did_you_mean argument to be set to True. To get an API key visit https://some-random-api.ml/docs/Welcome/Keys.')

        if (name is None) and (pokemon_id is None):
            raise TypeError('Either specify the name of the pokemon using name = \'name\' or the ID of the pokemon using pokemon_id = \'id\'.')
        
        if (name is not None) and (pokemon_id is not None):
            raise TypeError('Both name and pokemon_id cannot be specified, either specify the name of the pokemon using name = \'name\' or the ID of the pokemon using pokemon_id = \'id\'.')

        if (pokemon_id is not None) and (did_you_mean is True):
            raise TypeError('The did_you_mean argument cannot be True if only pokemon_id is specified, since pokemon_id cannot be checked and corrected for spelling')

        if name is not None:
            argument = f'pokemon={name.lower()}'
        elif pokemon_id is not None:
            argument = f'id={pokemon_id}'

        jsondata = requests.get(f'https://some-random-api.ml/pokedex?{argument}{self.formatted_api_key}').json()
        try:
            if jsondata['error'] == 'Sorry, I could not find that pokemon':
                if did_you_mean is True:
                    try:
                        if not jsondata['dym'] == '':
                            return jsondata['dym']
                        else:
                            return ['unidentified dym', '0%']
                    except KeyError:
                        self.errorhandler(jsondata)
                if argument.startswith('id='):
                    raise ValueError(f'{pokemon_id} is not a valid ID for a pokemon.')
                elif argument.startswith('pokemon='):
                    raise ValueError(f'{name.capitalize()} is not a valid name for a pokemon.')
        except KeyError:
            return {'name': jsondata['name'],
                    'id': jsondata['id'],
                    'type': jsondata['type'],
                    'species': jsondata['species'],
                    'abilities': jsondata['abilities'],
                    'height': jsondata['height'],
                    'weight': jsondata['weight'],
                    'base_experience': jsondata['base_experience'],
                    'gender': jsondata['gender'],
                    'egg_groups': jsondata['egg_groups'],
                    'stats': jsondata['stats'],
                    'family': jsondata['family'],
                    'sprites': jsondata['sprites'],
                    'description': jsondata['description'],
                    'generation': jsondata['generation']
                }

    def welcomeGoodbyeMessage(self, avatar: str, username: str, discriminator: str, guild_name: str, membercount: int, template: int = 1, background: str = 'space', type_of_message: str = 'join', textcolor: str = 'white') -> BytesIO:
        '''
        # Welcome/Goodbye image. Note that this function is related to Discord.
        Parameters -\n
            `background` (type str) (case-insensitive) (default 'space')
            `template` (type int) (must be 1, 2, 3 or 4) (default 1)
            `type_of_message` (type str) (case-insensitive) (must be 'join' or 'leave') (default 'join')
            `avatar` (type str) (case-sensitive) (must be a direct image link, formats - JPEG, JPG, PNG, GIF.)
            `username` (type str) (case-sensitive) (max len 30)
            `discriminator` (type str) (format - '0001', '9999' etc)
            `textcolor` (type str) (case-insensitive) (default 'white')
            `guild_name` (type str) (not shown as of now, will be used later)
            `membercount` (type int)
        `The background argument must be one of the elements from this list - stars, stars2, rainbowgradient, rainbow, sunset, night, blobday, blobnight, space (default), gaming1, gaming2, gaming3, gaming4.`\n
        `The textcolor argument must be one of the elements from this list - red, orange, yellow, green, blue, indigo, purple, pink, black, white (default).`\n
        Returns -\n
            if `type_of_message` is `join`: A picture welcoming a member with the name `username`#`discriminator` and with the avatar `avatar`, with the background `background` and so on (type BytesIO).
            if `type_of_message` is `leave`: A picture saying goodbye to a member with the name `username`#`discriminator` and with the avatar `avatar`, with the background `background` and so on (type BytesIO).
        Raises -\n
            ValueError - if the arguments were not right (see above for argument specifications).
            SRApi.InvalidURL - if `avatar` had an invalid, non-image URL.
        '''
        if not template in [1, 2, 3, 4]:
            raise ValueError('The template argument must be 1, 2, 3 or 4.')
        
        if not background.lower() in ['stars', 'stars2', 'rainbowgradient', 'rainbow', 'sunset', 'night', 'blobday', 'blobnight', 'space', 'gaming1', 'gaming2', 'gaming3', 'gaming4']:
            raise ValueError('The background argument must be in this list: ["stars", "stars2", "rainbowgradient", "rainbow", "sunset", "night", "blobday", "blobnight", "space", "gaming1", "gaming2", "gaming3", "gaming4"].')
        
        if not type_of_message.lower() in ['join', 'leave']:
            raise ValueError('The type_of_message argument can either be \'join\' or \'leave\'.')

        if len(username) > 30:
            raise ValueError('The username can be at maximum 30 characters.')
        
        if not len(discriminator) == 4:
            raise ValueError('That is not a valid discriminator. A valid discriminator is a number between 0001-9999')
        else:
            for num in discriminator:
                if not num.isnumeric():
                    raise ValueError('That is not a valid discriminator. A valid discriminator is a number between 0001-9999')

        if not textcolor.lower() in ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple', 'pink', 'black', 'white']:
            raise ValueError(f'The textcolor argument must be in this list: ["red", "orange", "yellow", "green", "blue", "indigo", "purple", "pink", "black", "white"].')

        avatar = quote(avatar, safe = '')
        username = quote(username, safe = '')
        guild_name = quote(guild_name, safe = '')
        data = requests.get(f'https://some-random-api.ml/welcome/img/{template}/{background.lower()}?type={type_of_message.lower()}&avatar={avatar}&username={username.replace(" ", "%20")}&discriminator={discriminator}&textcolor={textcolor.lower()}&guildName={guild_name.replace(" ", "%20")}&memberCount={membercount}{self.formatted_api_key}')
        try:
            jsondata = data.json()
            self.errorhandler(jsondata, ['avatar'])
        except JSONDecodeError:
            return BytesIO(data.content)

    def premiumWelcomeGoodbye(self, background_link: str, avatar: str, username: str, discriminator: str, guildname: str, membercount: str, template: int = 1, type_of_message: str = 'join', textcolor: str = 'white') -> BytesIO:
        '''
        # Premium Welcome/Goodbye image. Note that this function is related to Discord.
        `This function requires a Tier 2 or above API Key to use.`
        Perks of premium over normal -\n
            You can add a custom linked background.
        Parameters -\n
            `background_link` (type str) (case-insensitive) (must be a direct image link, formats - JPEG, JPG, PNG, GIF) (preferably 1200 x 600.)
            `template` (type int) (must be 1, 2, 3 or 4) (default 1)
            `type_of_message` (type str) (case-insensitive) (must be 'join' or 'leave') (default 'join')
            `avatar` (type str) (case-sensitive) (must be a direct image link, formats - JPEG, JPG, PNG, GIF.)
            `username` (type str) (case-sensitive) (max len 30)
            `discriminator` (type str) (format - '0001', '9999' etc)
            `textcolor` (type str) (case-insensitive) (default 'white')
            `guild_name` (type str) (not shown as of now, will be used later)
            `membercount` (type int)
            `api_key` (type str) (in class initialization, not a function parameter)
        `The textcolor argument must be one of the elements from this list - red, orange, yellow, green, blue, indigo, purple, pink, black, white (default).`\n
        Returns -\n
            if `type_of_message` is `join`: A picture welcoming a member with the name `username`#`discriminator` and with the avatar `avatar`, with the background `background` and so on (type BytesIO).
            if `type_of_message` is `leave`: A picture saying goodbye to a member with the name `username`#`discriminator` and with the avatar `avatar`, with the background `background` and so on (type BytesIO).
        Raises -\n
            ValueError - if the arguments were not right (see above for argument specifications).
            SRApi.InvalidURL - if `avatar` had an invalid URL, if `background_link` had an invaid URL.
            SRApi.ApiKeyError - if your API key is None/invalid/too low.
        '''
        if self.api_key is None:
            raise ApiKeyError('A Tier-2 or above API key is required for this function. To get an API key visit https://some-random-api.ml/docs/Welcome/Keys.')
        
        if not template in [1, 2, 3, 4]:
            raise ValueError('The template argument must be 1, 2, 3 or 4.')
        
        if not type_of_message.lower() in ['join', 'leave']:
            raise ValueError('The type_of_message argument can either be \'join\' or \'leave\'.')

        if len(username) > 30:
            raise ValueError('The username can be at maximum 30 characters.')

        if not len(discriminator) == 4:
            raise ValueError('That is not a valid discriminator. A valid discriminator is a number between 0001-9999')
        else:
            for num in discriminator:
                if not num.isnumeric():
                    raise ValueError('That is not a valid discriminator. A valid discriminator is a number between 0001-9999')

        if not textcolor.lower() in ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple', 'pink', 'black', 'white']:
            raise ValueError(f'The textcolor argument must be in this list: ["red", "orange", "yellow", "green", "blue", "indigo", "purple", "pink", "black", "white"].')

        background_link = quote(background_link, safe = '')
        avatar = quote(avatar, safe = '')
        username = quote(username, safe = '')
        guildname = quote(guildname, safe = '')
        data = requests.get(f'https://some-random-api.ml/premium/welcome/{template}?type={type_of_message.lower()}&avatar={avatar}&username={username.replace(" ", "%20")}&discriminator={discriminator}&bg={background_link}&textcolor={textcolor.lower()}&guildName={guildname.replace(" ", "%20")}&memberCount={membercount}&key={self.api_key}')
        try:
            jsondata = data.json()
            self.errorhandler(jsondata, ['avatar', 'background_link'])
        except JSONDecodeError:
            return BytesIO(data.content)

    def rankcard(self, username: str, discriminator: str, current_xp: int, needed_xp: int, level: int, avatar: str, background_color: str = None, exp_bar_color: str = None, bar_color: str = None, background_link: str = None, rank: int = None, template: int = 3, text_color: str = 'ffffff') -> BytesIO:
        '''
        # Rankcard image for discord levelling bots. This function is related to discord.
        `This function requires a Tier-1 or above API key to use`\n
        Parameters -\n
            `template` (type int) (must be 1, 2, 3, 4 or 5) (default 3)
            `username` (type str) (case-sensitive) (max len 20)
            `discriminator` (type str) (must be numeric) (format - 0001, 9999 etc)
            `current_xp` (type int) (shows up as `current_xp` / `needed_xp` XP)
            `needed_xp` (type int) (shows up as `current_xp` / `needed_xp` XP)
            `level` (type int)
            `avatar` (type str) (case-sensitive) (must be a direct image link, formats - JPEG, JPG, PNG, GIF.)
            `api_key` (type str) (in class initialization, not a function parameter)

            `rank` (type int) (optional) (default None)
            `background_color` (type str) (optional) (default None) (a hexcode, in these formats - '#ffffff', '0xffffff', 'ffffff')
            `exp_bar_color` (type str) (optional) (default None) (a hexcode, in these formats - '#ffffff', '0xffffff', 'ffffff')
            `bar_color` (type str) (optional) (default None) (a hexcode, in these formats - '#ffffff', '0xffffff', 'ffffff')
            `text_color` (type str) (optional) (default 'ffffff', equivalent to None) (a hexcode, in these formats - '#ffffff', '0xffffff', 'ffffff') (do not explicitly set this argument as None)
            `background_link` (type str) (optional) (a link to a background image for the rank card. Supported formats - PNG, JPG, JPEG and GIF.) (This overwrites `background_color` in any other `template` except 4.) (YOU NEED A TIER 2 KEY TO USE THIS)
        Returns -\n
            A levelling rankcard picture with the name `username#discriminator`, with the template `template`, with the level details `current_xp, needed_xp, level, rank`, with the avatar `avatar` and so on.
        Raises -\n
            ValueError - if the arguments provided were invalid.
            SRApi.InvalidURL - if `avatar` had an invalid, non-image URL.
            SRApi.ApiKeyError - if your api key is None/unspecified, invalid, or too low in tier (for the `background_link` parameter).
        '''
        if self.api_key is None:
            raise ApiKeyError('A Tier-1 or above API key is required for this function. To get an API key visit https://some-random-api.ml/docs/Welcome/Keys.')

        if not template in [1, 2, 3, 4, 5]:
            raise ValueError('The template argument must be 1, 2, 3, 4 or 5.')

        if len(username) > 32:
            raise ValueError('The username can be at maximum 32 characters.')

        if not len(discriminator) == 4:
            raise ValueError('That is not a valid discriminator. A valid discriminator is a number between 0001-9999')
        else:
            for num in discriminator:
                if not num.isnumeric():
                    raise ValueError('That is not a valid discriminator. A valid discriminator is a number between 0001-9999')

        if text_color.startswith('#'):
            text_color = text_color[1:]
        elif text_color.startswith('0x'):
            text_color = text_color[2:]
        if not len(text_color) == 6:
            raise ValueError(f'{text_color} is not a valid hexcode.')
        for code in text_color:
            if not code.lower() in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f']:
                raise ValueError(f'{text_color} is not a valid hexcode.')

        if not background_color is None:
            if background_color.startswith('#'):
                background_color = background_color[1:]
            elif background_color.startswith('0x'):
                background_color = background_color[2:]
            if not len(background_color) == 6:
                raise ValueError(f'{background_color} is not a valid hexcode.')
            for code in background_color:
                if not code.lower() in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f']:
                    raise ValueError(f'{background_color} is not a valid hexcode.')

        if not exp_bar_color is None:
            if exp_bar_color.startswith('#'):
                exp_bar_color = exp_bar_color[1:]
            elif exp_bar_color.startswith('0x'):
                exp_bar_color = exp_bar_color[2:]
            if not len(exp_bar_color) == 6:
                raise ValueError(f'{exp_bar_color} is not a valid hexcode.')
            for code in exp_bar_color:
                if not code.lower() in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f']:
                    raise ValueError(f'{exp_bar_color} is not a valid hexcode.')

        if not bar_color is None:
            if bar_color.startswith('#'):
                bar_color = bar_color[1:]
            elif bar_color.startswith('0x'):
                bar_color = bar_color[2:]
            if not len(bar_color) == 6:
                raise ValueError(f'{bar_color} is not a valid hexcode.')
            for code in bar_color:
                if not code.lower() in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f']:
                    raise ValueError(f'{bar_color} is not a valid hexcode.')

        username = quote(username, safe = '')
        avatar = quote(avatar, safe = '')
        if background_link is not None:
            if self.api_key is None:
                raise ApiKeyError('A Tier-2 or above API key is required for this function. To get an API key visit https://some-random-api.ml/docs/Welcome/Keys.')
            background_link = quote(background_link, safe = '')

        data = requests.get(f'https://some-random-api.ml/premium/rankcard/{template}?username={username}&discriminator={discriminator}&cxp={current_xp}&nxp={needed_xp}&level={level}{"&rank=" + str(rank) if not rank is None else ""}&avatar={avatar}&key={self.api_key}&ctext={text_color}{"&cbg=" + background_color if not background_color is None else ""}{"&ccxp=" + exp_bar_color if not exp_bar_color is None else ""}{"&cbar=" + bar_color if not bar_color is None else ""}{"&bg=" + background_link if not background_link is None else ""}')
        try:
            jsondata = data.json()
            self.errorhandler(jsondata, ['avatar'])
        except JSONDecodeError:
            return BytesIO(data.content)