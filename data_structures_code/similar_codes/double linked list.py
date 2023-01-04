class Node:
    def __init__(self,data):
        self.next=None
        self.data=data
        self.prev=None
class Double_linked_list:
    def __init__(self):
        self.head=None
        self.tail=None
    def is_empty(self):
        if self.head is None and self.tail is None:
            print("linked list is empty")
        else:
            print("linked list is not empty")
    def length(self):
        if self.head and self.tail is None:
            print("linked list is empty")
            return 0
        else:
            L=0
            a=self.head
            while True:
                L+=1
                if a.next is None:
                    break
                
                a=a.next
            return L
            
    def append(self,data):
        newNode=Node(data)
        if self.head is None and self.tail is None:
            self.head=newNode
            self.tail=newNode
        else:
            lastNode=self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode=lastNode.next
            lastNode.next=newNode
            newNode.prev=lastNode
        self.tail=newNode
    def prepend(self,data):
        newNode=Node(data)
        if self.head is None and self.tail is None:
            self.head=newNode
            self.tail=newNode
        else:
            self.head.prev=newNode
            newNode.next=self.head
            self.head=newNode
        
            
    def print_reverse(self):
        if self.tail is None:
            print("the double linked lsit is empty")
        else:
            a=self.tail
            while True:
                print(a.data)
                if a.prev is None:
                    break
                a=a.prev
    def print_forward(self):
        if self.head is None:
            print("the double linked lsit is empty")
        else:
            a=self.head
            while True:
                print(a.data)
                if a.next is None:
                    break
                a=a.next
        
dll=Double_linked_list()

dll.append(3)
dll.append(4)
dll.append(5)


dll.print_reverse()
print()
dll.print_forward()
print("the length of list is",dll.length())

            
        
