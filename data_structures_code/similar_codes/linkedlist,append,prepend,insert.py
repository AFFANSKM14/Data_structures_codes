class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
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
                

            #print('the previous node is not present in list so data cannot be inserted')
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
    ll.append('ali')
    ll.append('nawaz')
    ll.append('affan')
    ll.insert(ll.head.next.next,'ali')
    ll.print()
    
