# asyncio-throttle

[![travis-ci](https://travis-ci.org/hallazzang/asyncio-throttle.svg?branch=master)](https://travis-ci.org/hallazzang/asyncio-throttle)
[![pypi-version](https://badge.fury.io/py/asyncio-throttle.svg)](https://badge.fury.io/py/asyncio-throttle)

Simple, easy-to-use throttler for asyncio.

## Example

```python
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
```

Here I limited work rate to 5/sec while there are 5 workers.
And the result:

```plain
1508273760.3462772 Worker #2: Bang!
1508273760.590009 Worker #3: Bang!
1508273760.856431 Worker #0: Bang!
1508273761.0110679 Worker #2: Bang!
1508273761.086856 Worker #4: Bang!
1508273761.350699 Worker #3: Bang!
1508273761.5906 Worker #1: Bang!
1508273761.8655958 Worker #4: Bang!
1508273762.224158 Worker #0: Bang!
1508273762.600234 Worker #2: Bang!
1508273762.694332 Worker #2: Bang!
1508273762.726774 Worker #0: Bang!
1508273762.944273 Worker #4: Bang!
```

## Installation

```bash
$ pip install asyncio-throttle
```

It requires Python 3.6 or later.

## Usage

`asyncio_throttle.Throttler` introduces simple APIs: `flush()` and
`acquire()`. But you will not be interested in those because you can
just use it within `with` statement and it looks nicer.

First, create a throttler given desired rate limit. For example if you
want to limit rate to 500/min, you can make it as:

```python
from asyncio_throttle import Throttler

throttler = Throttler(rate_limit=500, period=60)
```

Then whenever you want to do some jobs which should have limited
rate(e.g. sending request to server), Put it in `async with` statement:

```python
async with throttler:
    send_a_request()
```

It's that easy. `asyncio_throttler` can be easily integrated with
`aiohttp` too:

```python
async def worker(throttler, session):
    while True:
        async with throttler:
            async with session.get('http://example.com') as resp:
                do_some_job_with(await resp.text())

        await asyncio.sleep(0.05)
```
