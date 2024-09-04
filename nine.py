"""

    condition

"""
import asyncio

counter = 0

async def do_work(condition):
    global counter

    async with condition:
        print('Locked')
        await condition.wait()

        counter += 1
        print(f'Event happened... counter = {counter}')

        await asyncio.sleep(3)
        counter += 1
        print(f'Work finished. counter = {counter}')


async def fire_event(condition):
    await asyncio.sleep(5)
    async with condition:
        print('Notify all tasks...')
        condition.notify_all()

    print('Notification finished')


async def main():
    condition = asyncio.Condition()
    asyncio.create_task(fire_event(condition))

    await asyncio.gather(do_work(condition), do_work(condition))


asyncio.run(main())