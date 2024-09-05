"""

    Subprocess

"""


import asyncio


async def main():
    process = await asyncio.create_subprocess_exec('ls')
    print(f'Process ID is {process.pid}')
    status_code = await process.wait() 
    print(f'Status code is {status_code}')



asyncio.run(main())