# AsyncIO: Non-blocking program execution

import asyncio

async def fun1():
    print("fun1");
    await asyncio.sleep(3);
    return "one";

async def fun2():
    print("fun2");
    await asyncio.sleep(3);
    return "two";

async def fun3():
    print("fun3");
    await asyncio.sleep(3);
    return "three";

async def main():
    # runs as task is completed
    # task = asyncio.create_task(fun1());
    # await fun1();
    # await fun2();
    # await fun3();

    # gather & run at the same time
    g = await asyncio.gather(
        fun1(),
        fun2(),
        fun3()
    );
    print(g); # returns a list

# to run asynchronously
asyncio.run(main());