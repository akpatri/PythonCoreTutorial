#asynchronous(non blocking)
import asyncio

async def task1():
    await asyncio.sleep(2)
    print("Task 1 done")

async def task2():
    await asyncio.sleep(1)
    print("Task 2 done")

async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main()) #Task 2 done -> Task 1 done

#parallelism(simultanously)
from multiprocessing import Pool
def square(n):
    return n * n
with Pool(4) as p:
    print(p.map(square, [1, 2, 3, 4]))

