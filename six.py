"""

    lock

"""
import asyncio


counter = 0

async def increament(lock):
    global counter
    # ----------------- Lock acquire(), release() ----------------------
    # await lock.acquire()
    # temp_counter = counter
    # temp_counter += 1
    # await asyncio.sleep(0.03)

    # counter = temp_counter
    # lock.release()

    # -----------Lock using with, context manager --------------
    async with lock:
        temp_counter = counter
        temp_counter += 1
        await asyncio.sleep(0.03)

        counter = temp_counter




async def main():
    lock = asyncio.Lock()
    global counter

    tasks = [asyncio.create_task(increament(lock)) for _ in range(100)]
    await asyncio.gather(*tasks)
    print(f'Counter is {counter}') # retruns 1, because conclusion of tasks source, (counter)


asyncio.run(main())