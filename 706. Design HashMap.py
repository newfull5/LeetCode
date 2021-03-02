class MyHashMap:

    def __init__(self):
        self.diction = dict()
        

    def put(self, key: int, value: int) -> None:
        self.diction[key] = value
        

    def get(self, key: int) -> int:
        if key not in self.diction.keys():
            return -1
        return self.diction[key]
        

    def remove(self, key: int) -> None:
        if key in self.diction.keys():
            del self.diction[key]
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
