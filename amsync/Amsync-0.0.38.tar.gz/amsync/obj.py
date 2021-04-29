from __future__ import annotations
from re import M

from uuid import uuid4
from typing import Any, Awaitable, Callable, Literal, NoReturn, Dict
from pathlib import Path
from asyncio import gather
from platform import system
from datetime import datetime
from subprocess import run
from contextlib import suppress
from unicodedata import normalize

from ujson import dumps, loads, dump, load
from aiohttp import request, ClientResponse
from filetype import guess_mime
from pybase64 import b64encode

from .enum import MediaType
from .exceptions import (
    SmallReasonForBan,
    InvalidReturn,
    AminoSays
)

ignore_codes = []
headers: dict[str, str] = {'NDCDEVICEID': '0184a516841ba77a5b4648de2cd0dfcb30ea46dbb4e911a6ed122578b14c7b662c59f9a2c83101f5a1'}
actual_com:  str | None = None
actual_chat: str | None = None
bot_id:      str | None = None
API = 'https://service.narvii.com/api/v1/'

Req_json = Dict[str, Any]

in_win = system() == 'Windows'
def clear() -> None:
    run('cls' if in_win else 'clear', shell=True)

def words(s):
    return s.strip().count(' ')+1

def get_value(
    d:       Req_json,
    *k:      str,
    convert: Any | None = None
) -> Any | None:

    tmp = None
    with suppress(KeyError):
        for i in k:
            tmp = d[i]

        if convert:
            return convert(tmp)
        return tmp

def fix_ascii(s: str) -> str:
    return normalize('NFKD', s).encode('ASCII', 'ignore').decode().strip()


def on_limit(
    obj:   list[Any],
    limit: int
) -> bool:
    return limit and len(obj) >= limit


async def upload_media(file: str) -> str:
    return (
        await _req(
            'post',
            '/g/s/media/upload',
            data=await FILE.get(file),
            need_dumps=False,
        )
    )['mediaValue']

async def upload_chat_bg(file: str) -> str:
    return (
        await _req(
            'post',
            'g/s/media/upload/target/chat-background',
            data=await FILE.get(file),
            need_dumps=False,
        )
    )['mediaValue']

async def upload_chat_icon(file: str) -> str:
    return (
        await _req(
            'post',
            'g/s/media/upload/target/chat-cover',
            data=await FILE.get(file),
            need_dumps=False,
        )
    )['mediaValue']



async def _req(
    method:     str,
    url:        str,
    *,
    data:       dict[str, Any] | None = None,
    need_dumps: bool                  = True,
    return_:    str                   = 'json',
) -> Awaitable[Req_json | str | bytes] | ClientResponse:

    async with request(
        method           = method,
        url              = API + url,
        data             = dumps(data) if need_dumps else data,
        headers          = headers,
    ) as res:
        if res.status < 400 and (j := await res.json(loads=loads))['api:statuscode']:
            raise AminoSays(f"{j['api:message']}. Code: {j['api:statuscode']}")
        if return_ == 'json':
            return await res.json(loads=loads)
        if return_ == 'text':
            return await res.text()
        if return_ == 'file':
            return await res.read()
        if return_ == 'aiohttp':
            return res
        raise InvalidReturn(return_)


class Message:
    __slots__ = (
        'author',
        'chat',
        'com',
        'extensions',
        'file_link',
        'icon',
        'id',
        'media_type',
        'mentioned_users',
        'nickname',
        'text',
        'type',
        'uid'
    )

    def from_ws(self, j: Req_json) -> Message:
        _cm: dict[str, Any] = j['chatMessage']

        global actual_chat, actual_com
        self.chat: str | None = get_value(_cm, 'threadId', convert=str)
        self.com:  str | None = get_value(j, 'ndcId', convert=str)

        actual_chat = self.chat
        actual_com  = self.com

        self.extensions:  dict[str, Any] | None = get_value(_cm, 'extensions')
        self.file_link:   str | None            = get_value(_cm, 'mediaValue')

        self.icon:            str | None       = get_value(_cm, 'author', 'icon')
        self.id:              str | None       = get_value(_cm, 'messageId')
        self.media_type:      str | None       = get_value(_cm, 'mediaType')
        self.mentioned_users: list[str] | None = [u.uid for u in get_value(self.extensions, 'mentionedArray') or []]

        self.nickname: str | None = get_value(_cm, 'author', 'nickname')
        self.text:     str | None = get_value(_cm, 'content')
        self.type:     str | None = get_value(_cm, 'type')
        self.uid:      str | None = get_value(_cm, 'uid')

        return self

    def from_chat(self, j: Req_json) -> Message:
        self.author:      User | None           = User(get_value(j, 'author'))
        self.chat:        str  | None           = get_value(j, 'threadId')
        self.extensions:  dict[str, Any] | None = get_value(j, 'extensions')

        self.id:              str | None        = get_value(j, 'messageId')
        self.mentioned_users: list[str] | None  = [u['uid'] for u in get_value(self.extensions, 'mentionedArray') or []]
        self.text: str | None = get_value(j, 'content')
        self.type: str | None = get_value(j, 'type')

        return self

    class _CreateData:
        async def msg(type, msgs):
            return [{'type': type, 'content': i} for i in msgs]

        async def file(files):
            return [await FILE.process(i) for i in files]

        async def embed(embed: Embed):
            if embed.image:
                embed.image = [[100, await upload_media(embed.image), None]]
            return [
                {
                    'content': embed.msg_text,
                    'attachedObject': {
                        'link':      embed.link,
                        'title':     embed.title,
                        'content':   embed.text,
                        'mediaList': embed.image,
                    },
                }
            ]

    async def send(
        self,
        *msgs: list[str],
        files: str | list[str] | None = None,
        type_: int | None             = 0,
        embed: Embed | None           = None,
        com:   str | None             = None,
        chat:  str | None             = None,
    ) -> list[Req_json]:

        com = com or actual_com
        chat = chat or actual_chat
        files = [files] if files and not isinstance(files, (tuple, list)) else files

        if msgs:
            data = await self._CreateData.msg(type_, msgs)
        elif files:
            data = await self._CreateData.file(files)
        else:
            data = await self._CreateData.embed(embed)

        async def foo(i: msgs | files | list[Embed]) -> _req:
            return await _req(
                'post',
                f'x{com}/s/chat/thread/{chat}/message',
                data=i
            )

        return await gather(*[foo(i) for i in data])


class Embed:
    __slots__ = (
        'msg_text',
        'title',
        'text',
        'link',
        'image'
    )

    def __init__(
        self,
        msg_text: str,
        title:    str,
        text:     str,
        link:     str,
        image:    str | bytes = None
    ):
        self.msg_text = msg_text
        self.title    = title
        self.text     = text
        self.link     = link
        self.image    = image


class User:
    __slots__ = (
        'bio',
        'blogs_count',
        'com',
        'comments_count',
        'created_time',
        'followers_count',
        'following_count',
        'id',
        'im_following',
        'is_online',
        'level',
        'nickname',
        'posts_count',
        'reputation',
        'role',
        'visitors_count',
    )

    def __init__(self, j: Req_json | None = None):
        if j:
            self.bio             = get_value(j, 'content')
            self.blogs_count     = get_value(j, 'blogsCount')
            self.com             = get_value(j, 'ndcId', convert=str)
            self.comments_count  = get_value(j, 'commentsCount')
            self.created_time    = get_value(j, 'createdTime')
            self.followers_count = get_value(j, 'membersCount')
            self.following_count = get_value(j, 'joinedCount')
            self.im_following    = get_value(j, 'followingStatus') == 1
            self.level           = get_value(j, 'level')
            self.nickname        = get_value(j, 'nickname')
            self.posts_count     = get_value(j, 'postsCount')
            self.id              = get_value(j, 'uid')
            self.reputation      = get_value(j, 'reputation')
            self.role            = {0: 'member', 101: 'curator', 100: 'leader', 102: 'leader-agent'}[j['role']]
            self.visitors_count  = get_value(j, 'visitoresCount')

    @classmethod
    async def search(
        cls,
        uids: str | list[str],
        com:  str | None = None
    ) -> Awaitable[list[User]]:

        com = com or actual_com
        uids = [uids] if not isinstance(uids, (list, tuple)) else uids

        async def foo(uid: str) -> User:
            return cls(
                (await _req('get', f'x{com}/s/user-profile/{uid}'))['userProfile']
            )

        return await gather(*[foo(uid) for uid in uids])

    async def ban(
        self,
        uid:    str,
        *,
        reason: str,
        com:    str | None = None
    ):
        com = com or actual_com
        if words(reason) < 3:
            raise SmallReasonForBan('Put a reason with at least three words')

        return await _req(
            'post',
            f'x{com}/s/user-profile/{uid}/ban',
            data={'reasonType': 200, 'note': {'content': reason}},
        )

    async def unban(
        self,
        uid:    str,
        *,
        reason: str        = '',
        com:    str | None = None
    ):
        com = com or actual_com

        return await _req(
            'post',
            f'x{com}/s/user-profile/{uid}/unban',
            data={'note': {'content': reason}} if reason else None,
        )


class File:
    @staticmethod
    def type(file: str | bytes) -> Literal[MediaType.LINK, MediaType.BYTES, MediaType.PATH]:
        if isinstance(file, str) and file.startswith('http'):
            return MediaType.LINK

        if isinstance(file, bytes):
            return MediaType.BYTES

        return MediaType.PATH

    @staticmethod
    async def get(file: str | bytes) -> bytes:
        type = File.type(file)

        if type == MediaType.LINK:
            async with request('get', file) as res:
                return await res.read()

        if type == MediaType.BYTES:
            return file

        with open(file, 'rb') as f:
            return f.read()

    @staticmethod
    def b64(file_bytes: bytes) -> str:
        return b64encode(file_bytes).decode()

    async def process(self, file: str | bytes) -> dict[str, Any] | NoReturn:
        if (
            self.type(file) not in (MediaType.LINK, MediaType.BYTES)
            and not Path(file).exists()
        ):
            raise FileNotFoundError(file)

        b = await self.get(file)
        b64 = self.b64(b)
        type = (guess_mime(b) or 'audio/mp3').split('/')

        if type[-1] == 'gif':
                return {
                'mediaType': 100,
                'mediaUploadValue': b64,
                'mediaUploadValueContentType': 'image/gif',
                'mediaUhqEnabled': True,
            }

        if type[0] == 'image':
            return {
                'mediaType': 100,
                'mediaUploadValue': b64,
                'mediaUhqEnabled': True,
            }

        if type[-1] == 'mp3':
            return {
                'type': 2,
                'mediaType': 110,
                'mediaUploadValue': b64,
                'mediaUhqEnabled': True,
            }


class Chat:
    __slots__ = (
        'announcement',
        'bg',
        'can_send_coins',
        'co_hosts',
        'created_in',
        'adm',
        'extensions',
        'icon',
        'id',
        'is_pinned',
        'is_private',
        'members_can_invite',
        'name',
        'only_fans',
        'only_view',
        'text'
    )

    def __init__(self, j=None):
        if j:
            t = get_value(j, 'thread') or j
            self.extensions         = get_value(t, 'extensions')

            self.announcement       = get_value(self.extensions, 'announcement') or ''
            self.bg                 = get_value(self.extensions, 'bm')[1] if 'bm' in self.extensions else None
            self.can_send_coins     = get_value(t, 'tipInfo', 'tippable')
            self.co_hosts           = get_value(self.extensions, 'coHost') or []
            self.created_in         = int(datetime.fromisoformat(t['createdTime'][:-1]).timestamp()) if t['createdTime'] else None
            self.adm                = get_value(t, 'author', 'uid')
            self.icon               = get_value(t, 'icon')
            self.id                 = get_value(t, 'threadId')
            self.is_pinned          = get_value(t, 'isPinned')
            self.is_private         = get_value(t, 'membersQuota') == 2
            self.members_can_invite = get_value(t, 'membersCanInvite') or True
            self.name               = get_value(t, 'title')
            self.only_fans          = get_value(self.extensions, 'fansOnly')
            self.only_view          = get_value(self.extensions, 'viewOnly') or False
            self.text               = get_value(t, 'content') or ''

    @classmethod
    async def search(
        cls,
        com:  str | None = None,
        chat: str | None = None
    ):
        com = com or actual_com
        chat = chat or actual_chat

        return cls(await _req('get',f'x{com}/s/chat/thread/{chat}'))

    async def messages(
        self,
        *,
        check: Callable[[Message], bool] = lambda _: True,
        com:   str | None = None,
        chat:  str | None = None,
        start: int | None = None,
        end:   int | None = None,
    ) -> list[Message.from_chat]:

        com = com or actual_com
        chat = chat or actual_chat
        messages = []

        res = await _req(
            'get',
            f'x{com}/s/chat/thread/{chat}/message?v=2&pagingType=t&size=100',
        )
        token = res['paging']['nextPageToken']
        for msg_ in res['messageList']:
            if check(msg := Message().from_chat(msg_)):
                messages.append(msg)

        while True:
            res = await _req(
                'get',
                f'x{com}/s/chat/thread/{chat}/message?v=2&pagingType=t&pageToken={token}&size=100',
            )
            for msg in res['messageList']:
                if check(msg := Message().from_chat(msg)):
                    messages.append(msg)

            if on_limit(messages, end):
                break

            try:
                token = res['paging']['nextPageToken']
            except KeyError:
                break

        return messages[start:end]

    async def clear(
        self,
        msgs:  str | list[str] | None = None,
        check: Callable[[Message], bool] = lambda _: True,
        com:   str | None = None,
        chat:  str | None = None,
        start: int | None = None,
        end:   int | None = None,
    ) -> list[Req_json]:

        com = com or actual_com
        chat = chat or actual_chat
        msgs = (
            ([msgs] if not isinstance(msgs, (tuple, list)) else msgs)
            if msgs
            else [
                msg.id for msg in await self.messages(
                    check=check, com=com, chat=chat, start=start, end=end
                )
            ]
        )

        async def foo(msg):
            return await _req(
                'post',
                f'x{com}/s/chat/thread/{chat}/message/{msg}/admin',
                data={'adminOpName': 102},
            )

        return await gather(*[foo(msg) for msg in msgs])

    async def members(
        self,
        check: Callable[[Message], bool] = lambda _: True,
        com:   str | None = None,
        chat:  str | None = None,
        start: int | None = None,
        end:   int | None = None,
    ) -> list[User]:

        com = com or actual_com
        chat = chat or actual_chat

        async def foo(i):
            res = await _req(
                'get',
                f'x{com}/s/chat/thread/{chat}/member?start={i}&size=100&type=default&cv=1.2',
            )
            return [
                i for i in [
                    User(i) for i in res['memberList'] if res['memberList']
                ]
                if check(i)
            ]

        members_count = (await _req(
            'get', f'x{com}/s/chat/thread/{chat}'
        ))['thread']['membersCount']

        MAX_MEMBERS_COUNT_IN_CHAT = 1000
        return (
            await gather(
                *[
                    foo(i) for i in range(0, MAX_MEMBERS_COUNT_IN_CHAT, 100)
                    if i <= members_count
                ]
            )
        )[0][start:end]

    async def join(
        self,
        chat: str, 
        com: str | None = None
    ) -> Req_json:

        com = com or actual_com
        chat = [chat] if not isinstance(chat, (list, tuple)) else chat

        async def foo(i):
            return await _req(
                'post', f'x{com}/s/chat/thread/{i}/member/{bot_id}'
            )

        return await gather(*[foo(i) for i in chat])

    async def leave(
        self,
        chat: str,
        com: str | None = None
    ) -> Req_json:

        com = com or actual_com
        chat = [chat] if not isinstance(chat, (list, tuple)) else chat

        async def foo(i):
            return await _req(
                'delete', f'x{com}/s/chat/thread/{i}/member/{bot_id}'
            )

        return await gather(*[foo(i) for i in chat])

    async def create(
        self,
        name:           str,
        text:           str | None  = None,
        bg:             str | bytes = None,
        icon:           str | bytes = None,
        only_fans:      bool        = False,
        invite_members: list[str]   = [],
        com:            str | None  = None
    ) -> Req_json:

        com = com or actual_com

        img = [100, await upload_chat_bg(bg), None] if bg else bg
        data = {
            'backgroundMedia': img,
            'extensions': {
                'bm': img,
                'fansOnly': only_fans
            },
            'title': name,
            'content': text,
            'icon': await upload_chat_icon(icon) if icon else icon,
            'inviteeUids': invite_members,

            # need this to work
            'type': 2,
            'eventSource': 'GlobalComposeMenu'
        }

        return await _req('post', f'x{com}/s/chat/thread', data=data)

    async def delete(
        self,
        com:  str | None = None,
        chat: str | None = None
    ) -> bool:

        com = com or actual_com
        chat = chat or actual_chat

        return (await _req('delete', f'x{com}/s/chat/thread/{chat}', return_='aiohttp')).ok

    async def config(
        self,
        name:               str | None         = None,
        text:               str | None         = None,
        bg:                 str | bytes | None = None,
        pin:                bool | None        = None,
        announcement:       str | None         = None,
        only_view:          bool | None        = None,
        members_can_invite: bool | None        = None,
        can_send_coins:     bool | None        = None,
        change_adm_to:      str | None         = None,
        com:                str | None         = None,
        chat:               str | None         = None
    ) -> None:

        com = com or actual_com
        chat = chat or actual_chat

        info = await self.search(chat=chat)
        if name or text:
            data = {
                'extensions': {
                    'bm': [100, await upload_chat_bg(bg), None] if bg else bg,
                    'fansOnly': info.only_fans
                },
                'title': name or info.name,
                'content': text or info.text,
                'icon': await upload_chat_icon(info.icon) if info.icon else info.icon,

                # need this to work
                'type': 2,
                'eventSource': 'GlobalComposeMenu'
            }
            await _req('post', f'x{com}/s/chat/thread/{chat}', data=data)


        if bg:
            await _req('post', f'x{com}/s/chat/thread/{chat}/member/{bot_id}/background', data=await FILE.process(bg))
        elif bg == False:
            await _req('delete', f'x{com}/s/chat/thread/{chat}/member/{bot_id}/background')

        if pin:
            await _req('post', f'x{com}/s/chat/thread/{chat}/pin')
        elif pin == False:
            await _req('post', f'x{com}/s/chat/thread/{chat}/unpin')

        if announcement:
            await _req('post', f'x{com}/s/chat/thread/{chat}', data={'announcement': announcement, 'pinAnnouncement': True})
        elif announcement == False:
            await _req('post', f'x{com}/s/chat/thread/{chat}', data={'pinAnnouncement': False})

        if only_view:
            await _req('post', f'x{com}/s/chat/thread/{chat}/view-only/enable')
        elif only_view == False:
            await _req('post', f'x{com}/s/chat/thread/{chat}/view-only/disable')

        if members_can_invite:
            await _req('post', f'x{com}/s/chat/thread/{chat}/members-can-invite/enable')
        elif members_can_invite == False:
            await _req('post', f'x{com}/s/chat/thread/{chat}/members-can-invite/disable')

        if can_send_coins:
            await _req('post', f'x{com}/s/chat/thread/{chat}/tipping-perm-status/enable')
        elif can_send_coins == False:
            await _req('post', f'x{com}/s/chat/thread/{chat}/tipping-perm-status/disable')

        if change_adm_to:
            await _req('post', f'x{com}/s/chat/thread/{chat}/transfer-organizer', data={'uidList': [change_adm_to]})

    async def change_co_hosts(
        self,
        add:    list[str] | str | None = None,
        remove: str | None = None,
        com:    str | None = None,
        chat:   str | None = None
    ) -> None:

        com = com or actual_com
        chat = chat or actual_chat
        add = [add] if add and not isinstance(add, (list, tuple)) else add

        if add:
            await _req('post', f'x{com}/s/chat/thread/{chat}/co-host', data={'uidList': add})
        elif remove:
            await _req('delete', f'x{com}/s/chat/thread/{chat}/co-host/{remove}')

    async def save(self, filename: str | None = None) -> None:
        chat = await Chat.search()
        info = {
            'name': chat.name,
            'text': chat.text,
            'announcement': chat.announcement,

            'bg': chat.bg,
            'icon': chat.icon,

            'adm': chat.adm,
            'co_hosts': chat.co_hosts,

            'members_can_invite': chat.members_can_invite,
            'can_send_coins': chat.can_send_coins,
            'is_pinned': chat.is_pinned,
            'only_view': chat.only_view,
            'only_fans': chat.only_fans,

            'members': [i.id for i in await self.members()]
        }

        n = 0
        while Path(f'{n}.json').exists():
            n += 1
        with open(filename or f'{n}.json', 'w') as f:
            dump(info, f, indent=4, escape_forward_slashes=False)

    async def load(self, filename: str) -> None:
        with open(filename, 'r') as f:
            f = load(f)

        tmp_chat_name = str(uuid4())
        await self.create(
            name = tmp_chat_name,
            text = f['text'],
            bg = f['bg'],
            icon = f['icon'],
            only_fans= f['only_fans'],
            invite_members=f['members']
        )

        chats = list((await Community.chats()).values())[0]
        names = [i.name for i in chats]
        ids = [i.id for i in chats]

        await self.config(
            name               = f['name'],
            pin                = f['is_pinned'],
            announcement       = f['announcement'],
            only_view          = f['only_view'],
            members_can_invite = f['members_can_invite'],
            can_send_coins     = f['can_send_coins'],
            change_adm_to      = f['adm'] if f['adm'] != bot_id else None,
            chat               = ids[names.index(tmp_chat_name)]
        )

        await self.change_co_hosts(f['co_hosts'])

class Community:
    @staticmethod
    async def chats(
        need_print:   bool       = False,
        ignore_ascii: bool       = False,
        com:          str | None = None
    ) -> dict[str, list[Chat]]:

        if not actual_com and not com:
            raise Exception('Enter a com or send a message in a chat')

        com = com or actual_com
        com = [com] if not isinstance(com, (list, tuple)) else com

        async def foo(i):
            res = await _req(
                'get', f'x{i}/s/chat/thread?type=public-all&start=0&size=100'
            )
            return {str(i): [Chat(i) for i in res['threadList']]}

        a = await gather(*[foo(i) for i in com])
        chats = {k: v for i in a for k, v in i.items()}

        if need_print:
            for i, e in chats.items():
                max_name = len(
                    max(
                        [
                            i.name if not ignore_ascii else fix_ascii(i.name)
                            for i in e
                        ],
                        key=len,
                    )
                )
                print(i)
                for n in e:
                    name = n.name if not ignore_ascii else fix_ascii(n.name)
                    a = max_name - len(name)
                    print(f"    {name} {' '*a}-> {n.id}")
                print()
        return chats


class My:
    @staticmethod
    async def chats(
        need_print:   bool = True,
        ignore_ascii: bool = False
    ) -> dict[str, list[str, list[str]]]:

        res = await _req('get', 'g/s/community/joined?v=1&start=0&size=50')
        coms = {str(i['ndcId']): [i['name'], []] for i in res['communityList']}

        async def foo(i):
            return await _req(
                'get', f'x{i}/s/chat/thread?type=joined-me&start=0&size=100'
            )

        chats = await gather(*[foo(i) for i in coms])

        for i in chats:
            for j in i['threadList']:
                com_id = str(j['ndcId'])
                chat_id = j['threadId']
                is_private_chat = j['membersQuota'] == 2
                chat_name = (
                    j['membersSummary'][1]['nickname']
                    if is_private_chat
                    else j['title']
                )

                coms[com_id][1].append(
                    (
                        chat_name if not ignore_ascii else fix_ascii(chat_name),
                        chat_id,
                    )
                )

        if need_print:
            for i, e in coms.items():
                max_name = (
                    len(max([i[0] for i in e[1]], key=len)) if e[1] else 0
                )
                print(f'{coms[i][0]} - {i}')
                for j in coms[i][1]:
                    a = (max_name - len(j[0])) + 1
                    print(f'    {j[0]} {" "*a}-> {j[1]}')
                print()

        return coms

    @staticmethod
    async def communities(
        need_print:   bool = True,
        ignore_ascii: bool = False
    ) -> dict[str, str]:

        res = await _req('get', f'g/s/community/joined?v=1&start=0&size=50')
        coms = {
            i['name']
            if not ignore_ascii
            else fix_ascii(i['name']): str(i['ndcId'])
            for i in res['communityList']
        }

        if need_print:
            max_name = len(max(coms.keys(), key=len))
            for i, e in coms.items():
                a = max_name - len(i)
                print(f'{i} {" "*a} -> {e}')

        return coms


# # # # # # #
#   Cache   #
# # # # # # #

FILE    = File()
MESSAGE = Message()
