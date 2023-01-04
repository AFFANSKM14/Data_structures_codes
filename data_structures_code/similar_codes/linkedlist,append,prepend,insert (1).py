class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def is_empty(self):
        if self.head is None:
            print("the linked list is empty")
        else:
            print("the linked lsit is not empty")
    def length(self):
        if self.head is None:
            return 0
        else:
            i=1
            a=self.head
            while True:
                if a.next is None:
                    break
                a=a.next
                i+=1
            return i
    def append(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
        else:
            lastNode=self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode=lastNode.next
            lastNode.next=newNode
    def prepend(self,data):
        newNode=Node(data)
        if self.head is None:
            print("the linked list is empty we cant prepend")
            return
        else:
            
            newNode.next=self.head
            self.head=newNode
    def insert(self,prevNode,data):
        newNode=Node(data)
        a=self.head
        while True:
            
            if prevNode.data is a.data:
                newNode.next=prevNode.next
                prevNode.next=newNode
                break
            if prevNode.next is None:
                newNode.next=None
                prevNode.next=newNode
                break
                
            else:
                if a.next is None:
                    print("the prevnode is not present in linked lsit so insertion is not happened")
                    break
                else:
                    a=a.next
    def delete_start(self):
        a=self.head
        self.head=a.next
        a.next=None
    def delete_end(self):
        a=self.head
        while True:
            if a.next is None:
                b.next=None
                break
            b=a
            a=a.next
            
    def delete_position(self,position):
        current_position=0
        a=self.head
        while True:
            if current_position==position:
                b.next=a.next
                a.next=None
                break
            b=a
            a=a.next
            current_position+=1
    def get_max(self):
        a=self.head
        maximum=a.data
        while True:          
            if a.next is None:
                return maximum
            if maximum>a.next.data:
                pass
            else:
                maximum=a.next.data
            a=a.next
    def get_min(self):
        a=self.head
        minimum=a.data
        while True:          
            if a.next is None:
                return minimum
            if minimum<a.next.data:
                pass
            else:
                minimum=a.next.data
            a=a.next     
    def sort(self,key=False):
        if key==True:
            a=self.head
            for i in range(self.length()):
                if self.head is None:
                    print("the list is empty")
                    return
                while True:
                    if a.next is None:
                        break
                    if a.data<a.next.data:
                        temp=a.data
                        a.data=a.next.data
                        a.next.data=temp
                    a=a.next
                a=self.head
        else:
            a=self.head
            for i in range(self.length()):
                if self.head is None:
                    print("the list is empty")
                    return
                while True:
                    if a.next is None:
                        break
                    if a.data>a.next.data:
                        temp=a.data
                        a.data=a.next.data
                        a.next.data=temp
                    a=a.next
                a=self.head
            
                
        
    def print(self):
        if self.head is None:
            print("Linkedlist is empty")
            return
        currentNode=self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode=currentNode.next
                
if __name__=='__main__':
    ll=LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(100)
    ll.append(50)
    ll.append(200)
    ll.append(75)
    ll.append(60)
    L=ll.length()
    print("the length is ",L)
    print("list before any methods")
    ll.print()
    ll.insert(ll.head.next.next,10)
    print('lsit after inserting')
    ll.print()
    ll.delete_position(1)
    ll.delete_start()
    print("list after deleting first and given position")
    ll.print()
    ll.delete_end()
    print("list after deleting end")
    ll.print()
    
    m=ll.get_max()
    print("the maximum is ",m)
    
    mi=ll.get_min()
    print("the minimum is",mi)
    ll.sort()
    print('after sort in ascending')
    ll.print()
    ll.sort(key=True)
    print('after sort in descending')
    ll.print()
    
