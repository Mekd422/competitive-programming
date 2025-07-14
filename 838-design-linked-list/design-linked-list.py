class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    
class MyLinkedList:
    ''''''

    def __init__(self):
        self.head = None
        self.length = 0
        

    def get(self, index: int) -> int:
        if index >= self.length or index < 0:
            return -1
        curr = self.head
        while index:
            curr = curr.next
            index -= 1
        return curr.val

            
    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
            
        

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
        self.length += 1 



        
    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        elif index > self.length or index < 0:
            return
        else:
            curr = self.head
            new_node = Node(val)
            for _ in range(index-1):
                curr = curr.next
            new_node.next = curr.next
            curr.next = new_node
            self.length += 1


    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return
        elif index == 0:
           self.head = self.head.next
        elif index == self.length - 1:
            curr = self.head
            while curr.next.next is not None:
                curr = curr.next
            curr.next = None
        else:
            curr = self.head
            i = index - 1
            while i:
                curr = curr.next
                i -= 1
            curr.next = curr.next.next
        self.length -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)