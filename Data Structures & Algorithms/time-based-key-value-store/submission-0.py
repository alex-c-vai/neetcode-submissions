class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            self.store[key].append((timestamp, value))
        else:
            self.store[key] = [(timestamp, value)]
    def get(self, key: str, timestamp: int) -> str:
        l, r = -1, -1
        res = ""
        if key in self.store:
            l, r = 0, len(self.store[key])-1
            while l <= r:
                mid = (l+r) // 2
                if timestamp < self.store[key][mid][0]:
                    r = mid - 1
                elif timestamp >= self.store[key][mid][0]:
                    l = mid + 1
                    res = self.store[key][mid][1]
        return res

