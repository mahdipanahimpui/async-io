"""

    Semaphore

"""


import asyncio


async def show(smp):
    # await smp.acquire()

    # print('Show Method')

    # await asyncio.sleep(3)

    # smp.release()

    # -------- using context manager -----------

    async with smp:
        print('Show method')
        await asyncio.sleep(3)


async def main():
    smp = asyncio.Semaphore(2)
    # smp = asyncio.BoundedSemaphore(2) # not release more than acquire
    await asyncio.gather(*[show(smp) for _ in range(20)])



asyncio.run(main())