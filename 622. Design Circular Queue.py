class MyCircularQueue:

    def __init__(self, k: int):
        self.arr = [None] * k
        self.length = k
        

    def enQueue(self, value: int) -> bool:
        if None not in self.arr:
            return False
        
        self.arr[self.arr.index(None)] = value
        return True
        

    def deQueue(self) -> bool:
        if [None]*self.length != self.arr:
            self.arr = self.arr[1:] + [None]
            return True
        
        return False
        

    def Front(self) -> int:
        if self.arr[0] == None:
            return -1
        return self.arr[0]
        

    def Rear(self) -> int:
        if None not in self.arr:
            return self.arr[-1]
        
        if [None]*self.length != self.arr:
            return self.arr[self.arr.index(None)-1]
        
        return -1
        

    def isEmpty(self) -> bool:
        return [None]*self.length == self.arr
        

    def isFull(self) -> bool:
        return None not in self.arr


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
