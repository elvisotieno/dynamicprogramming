# Design a time-based key-value data structure that can store multiple values for the same key at different time stamps
# and retrieve the key's value at a certain timestamp.
# Implement the TimeMap class:
# TimeMap() Initializes the object of the data structure.
# void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
# String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp.
# If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".

class TimeMap:
    def __init__(self):
        self.store = {}  # key: list of [value,timestamp]

    # The operations that we want to perform

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: str) -> str:
        res = ''
        values = self.store.get(key, [])

        # do  binary saerch
        L, R = 0, len(values) - 1
        while L <= R:
            mid = (L + R) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                L = mid + 1
            else:
                R = mid - 1
        return res
