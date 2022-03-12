class OrderedStream:

    def __init__(self, n: int):
        self.l = {}
        self.ptr = 1
    def insert(self, idKey: int, value: str) -> List[str]:
        self.l[idKey] = value
        chunk = []
        while self.ptr in self.l:
            chunk.append(self.l[self.ptr])
            self.ptr += 1
        return chunk
        
        
# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)