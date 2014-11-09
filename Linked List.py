class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        if not self: return 'None'
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        result  = ''
        cursor = self.head
        while (cursor):
            result += "%s -> " % cursor.data
            cursor = cursor.next
        return result + 'None'

    def add_node(self, data):
        ''' Adds a new node to the end of the list. '''
        new_node = Node(data)
        # if list is empty, set both head and tail to the new node
        if self.head == None:
            self.head = self.tail = new_node
        # otherwise, add the new node to the end and update the tail
        else:
            self.tail.next = new_node
            self.tail = new_node

    def reverse_list(self, list, new_ll):
        '''Creates a new reversed list using recursion'''
        if list == None: return
        head = list
        tail = list.next
        self.reverse_list(tail, new_ll)
        new_ll.add_node(head)
        return new_ll

    def reverse_dest_recur(self, head, prev = None):
        '''Destructively reverses list using recursion'''
        if head == None:
            self.head = prev # update head
            return self.head
        next = head.next
        head.next = prev
        result = self.reverse_dest_recur(next, head)
        self.tail = head # update tail
        return result

    def reverse_dest_iter(self, head):
        '''Destructively reverses list using iteration'''
        self.tail = self.head
        curr = head
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev
        return self.head

    def delete_node(self, data):
        # check for null head
        if not self.head: return False
        # delete head
        elif self.head.data == data:
            self.head = self.head.next
            return True

        # find node to delete
        node = self.head
        while node.next != None:
            if node.next.data == data:
                node.next = node.next.next # delete elem.next
                return True
            node = node.next

        # node not found
        return False

def main():
    ll = LinkedList()
    for i in range(5): ll.add_node(i)

    print ll




if __name__ == "__main__":
    main()
