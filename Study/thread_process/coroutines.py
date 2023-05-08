# 协程： 当程序遇见了IO操作的时候. 可以选择性的切换到其他任务上.
# # 在微观上是一个任务一个任务的进行切换. 切换条件一般就是IO操作
# # 在宏观上,我们能看到的其实是多个任务一起在执行
# # 多任务异步操作

import asyncio
import time


async def func1():
    print("你好啊, 我叫潘金莲")
    await asyncio.sleep(3)
    print("你好啊, 我叫潘金莲")


async def func2():
    print("你好啊, 我叫王建国")
    await asyncio.sleep(2)
    print("你好啊, 我叫王建国")


async def func3():
    print("你好啊, 我叫李雪琴")
    await asyncio.sleep(4)
    print("你好啊, 我叫李雪琴")


async def main():
    tasks = [asyncio.create_task(func1()), asyncio.create_task(func2()), asyncio.create_task(func3())]
    await asyncio.wait(tasks)


if __name__ == "__main__":
    t1 = time.time()
    asyncio.run(main())
    t2 = time.time()
    print(t2 - t1)