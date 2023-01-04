class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class Clinkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
    def insertb(self,data):
        if self.head is None and self.tail is None:
            node = Node(data,self.head)
            self.head=self.tail=node
            self.tail.next=self.head
        else:
            node=Node(data,self.head)
            self.head=node
            self.tail.next=self.head
    def inserte(self,data):
        if self.head is None and self.tail is None:
            node = Node(data,None)
            self.head=self.tail=node
            return
        itr=self.head
        while itr.next:
            if itr.next==self.tail:
                self.tail.next=None
            itr=itr.next
        self.tail=itr.next=Node(data,None)
        self.tail.next=self.head
    def insertat(self,index,data):
        len=self.getlength()
        count=1
        itr=self.head
        if index==0:
            self.insertb(data)
            return
        if index==len:
            self.inserte(data)
            return
        while True:
            if count==index:
                while itr:
                    itr.next=Node(data,itr.next)
                    return
            itr=itr.next
            count+=1
    def print(self):
        itr=self.head
        listr=''
        while itr.next!=self.head:
            listr+=str(itr.data)+' '
            itr=itr.next
        listr+=str(self.tail.data)
        print(listr)
    def getlength(self):
        itr=self.head
        length=0
        while itr.next!=self.head:
            length+=1
            itr=itr.next
        return length+1         
c=Clinkedlist()
c.inserte(6)
c.inserte(7)
c.inserte(8)
c.inserte(9)
c.inserte(10)
c.insertat(0,5)
c.insertat(9,11)
c.insertat(1,5.5)
c.insertat(4,7.5)
c.print()
print(c.getlength())
