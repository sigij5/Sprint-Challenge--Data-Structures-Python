class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.list = []
        self.tail = 0
        self.head = 0
        # self.buffer = [None] * self.capacity
        self.cursor = 0

    def append(self, item):
        if len(self.list) == self.capacity:
            self.list[self.cursor] = item
            self.cursor = (self.cursor+1) % self.capacity
        else:
            self.list.append(item)
            
    def get(self):
        l = []
        for item in self.list:
            if item is not None:
                l.append(item)
        return l

# test_buffer = RingBuffer(5)

# test_buffer.append(1)
# test_buffer.append(2)
# test_buffer.append(3)
# test_buffer.append(4)
# test_buffer.append(5)
# test_buffer.append(6)
# test_buffer.append(7)
# test_buffer.append(8)

# test_buffer.get()



                


