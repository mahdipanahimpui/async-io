"""
    Cancel

"""


import asyncio
from asyncio import CancelledError, TimeoutError


async def one():
    await asyncio.sleep(6)
    print('Hello')



# ------------------ Manually timeout ------------------
# async def main():
#     a = asyncio.create_task(one())
#     secends = 0

#     while not a.done():
#         print('Task is not finished ...')
#         await asyncio.sleep(1)
#         secends += 1
#         if secends == 5:
#             a.cancel()

#     try:
#         await a
#     except CancelledError:
#         print('task is cancelled')


# asyncio.run(main())
    


# -------------------- Automatic Timeout ----------------------
# async def main():
#     a = asyncio.create_task(one())

#     try:
#         await asyncio.wait_for(a, timeout=5)
#     except TimeoutError:
#         print('Deadline reached ...')
    
#     print(f'was task is cancelled? {a.cancelled()}')

# asyncio.run(main())



# -------------------- cancel shield ----------------------
async def main():
    a = asyncio.create_task(one())

    try:
        await asyncio.wait_for(asyncio.shield(a), timeout=5)
    except TimeoutError:
        print('task is takes to long time')
        await a  # await again to continue
    
    print(f'was task is cancelled? {a.cancelled()}')

asyncio.run(main())