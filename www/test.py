from www.orm import *
from www.Models import User,Blog,Comment
import asyncio
@asyncio.coroutine
def test(loop):
    yield from create_pool(loop=loop,host='192.168.0.106',user='www-data',password='www-data',db='awesome')
    u = User(name='Testasd1',email='zhuyubao@woza1123iiot.com',passwd='123145678asd',image='asdabout:blank')
    yield from u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()