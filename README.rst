================
asyncio-throttle
================

|pypi-version| |pypi-license|

Simple, easy-to-use throttler for asyncio.

Example
-------

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
        throttler = Throttler(rate_limit=5)

        tasks = [
            loop.create_task(worker(no, throttler, 10))
                for no in range(5)
        ]
        await asyncio.wait(tasks)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()

Here I limited work rate to 5/sec while there are 5 workers.

Installation
------------

.. code:: bash

    $ pip install asyncio-throttle

Usage
-----

`asyncio_throttle.Throttler` introduces simple APIs:
`flush()` and `acquire()`. But you will not be interested in those
because you can just use it within `with` statement and it looks nicer.

First, create a throttler given desired rate limit.
For example if you want to limit rate to 500/min, you can make it as:

.. code:: python

    from asyncio_throttle import Throttler

    throttler = Throttler(rate_limit=500, period=60)

Then whenever you want to do some jobs which should have limited
rate(e.g. sending request to server), Put it in `async with` statement:

.. code:: python

    async with throttler:
        send_a_request()

It's that easy. `asyncio_throttler` can be easily integrated
with `aiohttp` too:

.. code:: python

    async def worker(throttler, session):
        while True:
            async with throttler:
                async with session.get('http://example.com') as resp:
                    do_some_job_with(await resp.text())

            await asyncio.sleep(0.05)

.. |pypi-version| image:: https://img.shields.io/pypi/v/asyncio-throttle.svg?style=flat-square
   :target: https://pypi.python.org/pypi/asyncio-throttle/

.. |pypi-license| image:: https://img.shields.io/pypi/l/asyncio-throttle.svg?style=flat-square
   :target: https://pypi.python.org/pypi/asyncio-throttle/
