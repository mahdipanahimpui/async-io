"""

        aiohttp, gather

"""


import aiohttp
import asyncio


async def show_status(session, url):
    async with session.get(url) as result:
        return result.status

# ------------------- one url request --------------------------------
# async def main():
#     async with aiohttp.ClientSession() as session:
#         url = 'https://www.wikipedia.org/'
#         status = await show_status(session, url)
#         print(f'status is {status}')

# asyncio.run(main())


# -------------- many url request ----------------------------------------
async def main():
    async with aiohttp.ClientSession() as session:
        urls = ['https://www.wikipedia.org/', 
                'https://en.wikipedia.org/wiki/Persian',
                'https://en.wikipedia.org/wiki/Persian_language'
        ]
        rqs = [show_status(session, url) for url in urls]
        status_codes = await asyncio.gather(*rqs, return_exceptions=True)
        # return_exception returns the exception as a successfull result 
        print(f'status is {status_codes}')


asyncio.run(main())

