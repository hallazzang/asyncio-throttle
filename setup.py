from setuptools import setup

"""
================
asyncio-throttle
================

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

"""

setup(
    name='asyncio-throttle',
    version='0.0.1',
    url='https://github.com/hallazzang/asyncio-throttle',
    license='MIT',
    author='hallazzang',
    author_email='hallazzang@gmail.com',
    description='Simple, easy-to-use throttler for asyncio',
    long_description=__doc__,
    py_modules=['asyncio_throttle'],
    zip_safe=False,
    platforms='any',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
