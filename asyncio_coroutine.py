#!usr/bin/env python3
# -*- coding:utf-8 -*-


import asyncio
import threading

@asyncio.coroutine
def hello():
    print('hello world')
    yield from asyncio.sleep(1)
    print('hello again')

loop=asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait([hello(),hello(),hello(),hello(),hello()]))
loop.close()