import asyncio
from aiomysql import SSCursor
from aiomysql import sa, create_pool



loop = asyncio.new_event_loop()
async def init_pool(loop):
    global __pool
    __pool = await create_pool(host='localhost',
                                      port=3306,
                                      user='root',
                                      db='awesome',
                                      password='',
                                      use_unicode=True,
                                      loop=loop)
    __pool = __pool.acquire()

async def test_pool():
    global __pool
    await init_pool(loop)
    print(__pool)
    #async with ( await __pool) as pool:
    #async with (await __pool) as pool:
    async with( await __pool) as conn:
        async with (await conn.cursor()) as cur:
            await cur.execute("SELECT * from users")
        conn.close()

loop.run_until_complete(test_pool())
'''
loop = asyncio.new_event_loop()
async def init_pool(loop):
    global __pool
    __pool = create_pool(host='localhost',
                                      port=3306,
                                      user='root',
                                      db='awesome',
                                      password='',
                                      use_unicode=True,
                                      loop=loop)

async def test_pool():
    global __pool
    await init_pool(loop)
    print(__pool)
    #async with ( await __pool) as pool:
    async with (await __pool) as pool:
        async with( pool) as conn:
            async with (await conn.cursor()) as cur:
                await cur.execute("SELECT * from users")

loop.run_until_complete(test_pool())
'''