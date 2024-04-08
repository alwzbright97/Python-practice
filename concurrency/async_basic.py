import asyncio
import datetime

async def task(seconds):
    print(f"[Started task] {datetime.datetime.now().strftime("%Y-%m-%d %H:%M%S")}")
    print(f"This task will end after {seconds} sec.")
    
    await asyncio.sleep(seconds)
    print(f"Task end.")
    print(f"[Finished task] {datetime.datetime.now().strftime("%Y-%m-%d %H:%M%S")}")


async def main():
    await asyncio.gather(
        task(1),
        task(2),
        task(3)
    )

asyncio.run(main())