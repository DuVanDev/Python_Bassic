class Node:
    def __init__(self , data = Node, next = Node):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = Node

    def insert_at_begining(self , data):
        node = Node(data, self.head)
        self.head = node
    
    def print(self):
        if self.head is None:
            print('Linked list is empty')
            return
        
        itr = self.head
        listr = ''
        while itr:
            listr += str(itr.data) + '--->'
            itr = itr.next
        
        print(listr)


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert_at_begining(5)
    linked_list.insert_at_begining(89)
    linked_list.print()