import asyncio

from fastapi import FastAPI

from timewheel import TimeWheel
from timewheel.schedule import Schedule

app = FastAPI()


async def mf():
    print("OLAR")
    await asyncio.sleep(10)


@app.on_event('startup')
async def setup():

    tw = TimeWheel([
        Schedule(name="my-s",
                 expression="38 10,11,12 * * *",
                 timezone="America/Sao_Paulo",
                 job=mf)])
    asyncio.create_task(tw.run())

