import asyncio

import discover
from light import Light


async def main():
    print(await discover.discover())
    light: Light = Light(ip="192.168.178.23")
    light.set_rgb(g=255)
    await light.apply()
    await light.is_on()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
