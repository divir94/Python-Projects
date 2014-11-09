#!/usr/bin/env python
class Queue:
    '''
    A simple bounded queue (First-In-First-Out) implemented using a circular buffer.
    '''
    def __init__(self, size):
        '''
        Constructor that creates an array of length 'size'.
        Also, initializes instance attributes for the head of the queue (i.e. where the next item will be added)
        and the number of items stored.
        '''
        self.size = size
        self.Q = [None]*size
        self.head = 0
        self.num_items = 0

    def enqueue(self, item):
        '''
        If queue is not full, adds item to the queue.
        Otherwise, prompts the user if he/she wants to overwrite the oldest element in the queue.
        '''
        # Check if queue is full
        queue_full = self.num_items >= self.size
        if queue_full and not \
                        input('Queue is full. Overwrite older item? Enter 1 (overwrite) or 0 (exit): '):
            print "%d not added to queue" % item
            return
        # Add item if either queue is not full or the user wants to overwrite.
        self.Q[self.head] = item
        self.head = (self.head + 1) % self.size # circulate the array
        if not queue_full: self.num_items += 1
        return self.Q

    def dequeue(self):
        '''
        Returns the item at the head of the queue, if queue is not empty.
        '''
        if self.num_items == 0:
            print "Queue is empty"
            return
        # If queue is not empty, remove and return the item from the head.
        previous_head = (self.head - 1) % self.size
        item = self.Q[previous_head]
        self.head = previous_head
        self.num_items -= 1
        return item

    def __str__(self):
        return "Head: %d, Number of items: %d\nQueue: %s" % (self.head, self.num_items, str(self.Q))


def main():
    '''
    Q = Queue(5)

    for item in range(1, 8):
        Q.enqueue(item)
    print Q

    for item in range(1, 7):
        Q.dequeue()
    print Q
    '''

    return

if __name__ == '__main__':
    main()