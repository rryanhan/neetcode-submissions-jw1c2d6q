class TimeMap:

    def __init__(self):
        self.store = {} # { key : [ [value, timestamp] ]}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        timestamps = self.store.get(key, [])

        l, r = 0, len(timestamps) - 1
        while l <= r:
            mid = (l + r) // 2
            if timestamps[mid][1] <= timestamp:
                res = timestamps[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res

        
