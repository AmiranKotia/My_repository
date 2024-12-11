# Davaleba 29(1):
import asyncio

async def task_one():
    print("Task one started.")
    await asyncio.sleep(2)
    print("Task one finished.")

async def task_two():
    print("Task two started.")
    await asyncio.sleep(5)
    print("Task two finished.")

async def main():
    task1 = asyncio.create_task(task_one())
    task2 = asyncio.create_task(task_two())

    await task1
    await task2

asyncio.run(main())


# Davaleba 29(2):
import asyncio
import random

async def print_random():
    for _ in range(5):
        random_number = random.randint(1, 10)
        print(f"Random number: {random_number}")
        await asyncio.sleep(random.randint(1, 3))

async def main():
    await print_random()

asyncio.run(main())