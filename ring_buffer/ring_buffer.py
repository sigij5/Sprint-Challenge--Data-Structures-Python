class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.list = []
        self.tail = 0
        self.head = 0
        self.buffer = [None] * self.capacity
        self.cursor = 0

    def append(self, item):
        if self.size == self.capacity:
            self.list[self.cursor] = item
            self.cursor += 1
            if self.cursor == self.capacity:
                self.cursor = 0
            if self.size <= self.capacity:
                self.size += 1
        else:
            self.list.append(item)
            self.size += 1
        # if self.size 


        # if self.size >= self.capacity:
        #     self.list[self.head] = item
        #     if self.head == self.capacity - 1:
        #         self.head = 0
        #     else:
        #         self.head += 1
        #     if self.tail == self.capacity - 1:
        #         self.tail = 0
        #     else:
        #         self.tail += 1
        #     self.size += 1
        # else:
        #     self.list.append(item)
        #     self.tail = self.tail + 1
        #     self.size += 1
            



    def get(self):
        if self.size == 0:
            return
       
        else:
            for item in self.list:
                if item is not None:
                    print(item)

                


