"""
    Coroutine
"""

import asyncio
import datetime

async def one(name):
    await asyncio.sleep(2)
    print(f'Hello {name}')



# print(type(one('amir'))) # <class 'coroutine'>

# --------------------- run --------------------------
# not plays async, the sleep not overlaped!!   THIS IS BAD
# print(datetime.datetime.now())
# asyncio.run(one('amir')) 
# asyncio.run(one('Kevin')) 
# print(datetime.datetime.now())

# --------------------- run --------------------------
# not plays async, the sleep not overlaped!!   THIS IS BAD
# print(datetime.datetime.now())
# asyncio.run(one('amir')) 
# asyncio.run(one('Kevin')) 
# print(datetime.datetime.now())


# ----------------- coroutine ------------------------------
# run async
async def main():
    a = asyncio.create_task(one('amir'))
    b = asyncio.create_task(one('kevin'))

    await a
    await b


print(datetime.datetime.now())
asyncio.run(main()) 
print(datetime.datetime.now())