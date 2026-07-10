class DynamicArray:
    
    def __init__(self, capacity: int):
        self.internal = []
        self.size = 0
        self.capacity = capacity

    def get(self, i: int) -> int:
        return self.internal[i]

    def set(self, i: int, n: int) -> None:
        self.internal[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        
        self.internal.append(n)
        self.size += 1

    def popback(self) -> int:
        toReturn = self.internal[self.size - 1]
        self.size -= 1
        return toReturn

    def resize(self) -> None:
        self.capacity *= 2

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
