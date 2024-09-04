"""

    Future

"""

import asyncio
import aiohttp


# f = asyncio.Future() # future object

# print(f.done())
# f.set_result("DONE")
# print(f.done())
# print(f.result())



# ---------------------- 
async def show_status(session, url, delay):
    await asyncio.sleep(delay)

    async with session.get(url) as result:
        print(f'status for {url} is {result.status}')


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [
            show_status(session, 'https://www.vikipedia.org', 3),
            show_status(session, 'https://www.vikipedia.org/Persian_cat', 5)
        ]

        for task in asyncio.as_completed(tasks):
        # as_completed: 
            #       - creates future
            #       - gets a list
            #       - returns value in no order
            #       - return each result at the moment
            await task

asyncio.run(main())
