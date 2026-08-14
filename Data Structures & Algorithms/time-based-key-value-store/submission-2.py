class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append([value, timestamp])

        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key not in self.timemap:
            return ""
        l, r = 0, len(self.timemap[key]) - 1

        while l <= r:
            mid = ((l + r) // 2)
            # if the timestamp we are at is <= timestamp
            if self.timemap[key][mid][1] <= timestamp:
                res = self.timemap[key][mid][0]
                l = mid + 1
            else:
                r = mid - 1
        print(res)
        return res

        
        
