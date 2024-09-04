"""

    wait

"""

import asyncio
import aiohttp


async def show_status(session, url):
    async with session.get(url) as result:
        return f'status for {url} is {result.status}'


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [
            asyncio.create_task(
                show_status(session, 'https://www.vikipedia.org/')
            ), 
            asyncio.create_task(
                show_status(session, 'https://www.vikipedia.ERRRRRorg/Persian_cat')
            )
        ]

        done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_EXCEPTION) # return_when=ALL_COMPLETED by default
        # FIRST_COMPLETED: return the tasks after the first finished, other not complete
        # if TIMEOUT_ERROR sets: the time_out error sets the task in the pending set
        print(f'Done --> {done}')
        print(f'Pending --> {pending}')

        for d in done:
            # print(d.result()) # or
            # print(await d)

            if d.exception() is None:
                print(d.result())
            else:
                print('Error ...')

            for p in pending:
                p.cancel()

        print(f'after cancel {pending}')

asyncio.run(main())