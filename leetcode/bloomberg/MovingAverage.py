"""
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Implement the MovingAverage class:

MovingAverage(int size) Initializes the object with the size of the window size.
double next(int val) Returns the moving average of the last size values of the stream.

"""

from collections import deque


class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.running_sum = 0
        self.queue = deque()
        self.count = 0

    def next(self, val: int) -> float:
        self.running_sum += val
        self.queue.append(val)
        self.count += 1
        if self.count > self.size:
            num_to_remove = self.queue.popleft()
            self.running_sum -= num_to_remove
            return self.running_sum/self.size
        return self.running_sum/self.count

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
