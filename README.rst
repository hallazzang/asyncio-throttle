================
asyncio-throttle
===============

Simple, easy-to-use throttler for asyncio.

Usage
-----

.. code:: python

    import time
    import random
    import asyncio

    from asyncio_throttle import Throttler

    async def worker(no, throttler, n):
        for _ in range(n):
            await asyncio.sleep(random.random() * 2)

            async with throttler:
                print(time.time(), 'Worker #%d: Bang!' % no)

    async def main():
        throttler = Throttler(5)

        tasks = [loop.create_task(worker(no, throttler, 10)) for no in range(5)]
        await asyncio.wait(tasks)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()

Here I limited work rate to 5/sec while there are 5 workers.

Installation
------------

.. code:: bash

    $ pip install asyncio-throttle
