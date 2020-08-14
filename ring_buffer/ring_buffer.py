class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.list = []  # empty list
        self.current = 0 # the current length of our list/where we are at
        # we want it 
        # to be a certain size, if the size is passed the capacity
        # then we will start back at the beginnig and then overwrite the value at that index


    def append(self, item):
        # can only be a certain length 
        # if we reach the ending index or 
        # if self.current === self.capacity, we want to start back at the beginning
        # to overwrite the current info


        if len(self.list) < self.capacity:
            self.list.append(item)
            self.current += 1
        else:
            if self.current == self.capacity:

                self.current = 0
                self.list[self.current] = item
                self.current += 1

            else:
                self.list[self.current] = item
                self.current += 1 # lol i forgot to increment here 

        



        

        # if self.current == self.capacity:
        #     # make the current equal to the first one
        #     self.current = 0
        #     self.list[self.current] = item
        #     self.current += 1

        # else:
        #     self.list[self.current] = item
        #     self.current += 1

    def get(self):

        return self.list


ring = RingBuffer(5)

ring.append(1)
ring.append(2)
ring.append(3)
ring.append(4)
ring.append(5)
ring.append(6)
ring.append(7)
ring.append(8)
ring.append(9)
ring.append(10)

print(ring.get(), 'the list with all 5 elements appended')