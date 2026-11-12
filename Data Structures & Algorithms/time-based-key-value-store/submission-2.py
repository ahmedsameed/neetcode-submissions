from sortedcontainers import SortedDict
class TimeMap:

    def __init__(self):
        self.keyStore=defaultdict(SortedDict)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyStore[key][timestamp]=value
        """if key not in self.keyStore:
            self.keyStore[key]={}
        if timestamp not in self.keyStore[key]:
            self.keyStore[key][timestamp]=[]
        self.keyStore[key][timestamp].append(value)"""

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keyStore:
            return ""
        timestamps=self.keyStore[key]
        index=timestamps.bisect_right(timestamp)-1

        if index>=0:
            time=timestamps.values()[index]
            return time
        return ""