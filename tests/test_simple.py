import sys
import time
import asyncio
from collections import deque

import pytest

from asyncio_throttle import Throttler


class TestThrottle:
    async def worker(self, throttler, logs):
        try:
            while True:
                async with throttler:
                    logs.append(time.time())
                await asyncio.sleep(0.05)
        except asyncio.CancelledError:
            pass

    @pytest.mark.parametrize(
        "rate_limit,workers_to_spawn", [(5, 5), (20, 35), (50, 100),]
    )
    @pytest.mark.asyncio
    async def test_rate_limiting(self, rate_limit, workers_to_spawn):
        throttler = Throttler(rate_limit)
        logs = deque()

        tasks = [
            asyncio.create_task(self.worker(throttler, logs))
            for _ in range(workers_to_spawn)
        ]

        started = time.time()
        while True:
            now = time.time()
            if now - started >= 5.0:
                break

            while logs:
                if now - logs[0] > 1.0:
                    logs.popleft()
                else:
                    break

            assert len(logs) <= rate_limit

            await asyncio.sleep(0.05)

        for task in tasks:
            task.cancel()
