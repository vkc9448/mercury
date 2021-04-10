import asyncio
import asyncpg


async def run():
    connection = await asyncpg.connect(user='admin', password='BoltBolt6126', database='mercury', host='127.0.0.1')
    values = await connection.fetch(
        'SELECT * FROM mytable WHERE id = $1',
        10,
    )
    await connection.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(run())
