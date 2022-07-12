import time
import asyncio
from collections import deque
from typing import Deque


class Throttler:
    def __init__(self, rate_limit: int, period=1.0):
        self.rate_limit = rate_limit
        self.period = period

        self._task_logs: Deque[float] = deque()

    def flush(self):
        now = time.monotonic()
        while self._task_logs:
            if now - self._task_logs[0] > self.period:
                self._task_logs.popleft()
            else:
                break

    async def acquire(self):
        while True:
            self.flush()
            if len(self._task_logs) < self.rate_limit:
                break
            time_to_release = self._task_logs[0] + self.period - time.monotonic()
            await asyncio.sleep(time_to_release)

        self._task_logs.append(time.monotonic())

    async def __aenter__(self):
        await self.acquire()

    async def __aexit__(self, exc_type, exc, tb):
        pass
