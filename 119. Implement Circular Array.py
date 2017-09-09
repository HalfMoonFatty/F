'''
Problem:

implement circular buffer with read & write functions

http://www.geeksforgeeks.org/circular-queue-set-1-introduction-array-implementation/
'''


class CircularQueue(object):
    def __init__(self, size):
        self.rear = self.front = -1
        self.size = size
        self.arr = [0] * self.size
        self.lock = threading.Lock()



    def enQueue(self, val):
        with self.lock:
            if self.front == 0 and self.rear == self.size - 1 or self.rear == self.front - 1:
                print "Queue is full"

            elif self.front == -1:    # insert fisrt element
                self.front = self.rear = 0
                self.arr[self.rear] = val

            elif self.rear == self.size - 1 and self.front != 0:
                self.rear = 0
                self.arr[self.rear] = val

            else:
                self.rear += 1
                self.arr[self.rear] = val



    def deQueue(self):
        with self.lock:
            if self.front == -1:
                print "Queue is empty"
                return 

            data = self.arr[self.front]
            self.arr[self.front] = -1

            if self.front == self.rear:  # pop out last element
                self.front = -1
                self.rear = -1

            elif self.front == self.size - 1:
                self.front = 0

            else:
                self.front += 1
            return data



    def peek(self):
        with self.lock:
            return self.arr[self.front]




cq = CircularQueue(5)
cq.enQueue(14)
cq.enQueue(22)
cq.enQueue(13)
cq.enQueue(-6)
print cq.peek()
print cq.deQueue()
print cq.deQueue()
cq.enQueue(9)
cq.enQueue(20)
cq.enQueue(5)
cq.enQueue(6)
 
 
