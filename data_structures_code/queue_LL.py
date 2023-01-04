class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class QueueLL:
    def __init__(self):
        self.top=None
        self.bottom=None
    def push(self,data):
        if self.top is None and self.bottom is None:
            node=Node(data)
            self.top=self.bottom=node
        else:
            itr=self.top
            while itr.next:
                itr=itr.next
            node=itr.next=Node(data,itr.next)
            self.bottom=node
    def pop(self):
        if self.getlen()>0:
            self.top=self.top.next
        else:
            print('Queue is Empty')
    def print(self):
        itr=self.top
        listr=''
        while itr:
            listr+=str(itr.data)+' '
            itr=itr.next
        print(listr)
    def getlen(self):
        itr=self.top
        length=0
        while itr:
            length+=1
            itr=itr.next
        return length        
c=QueueLL()
c.push(5)
c.push(6)
c.push(7)
c.push(8)
c.push(9)
print(c.getlen())
c.print()
c.pop()
c.pop()
c.print()
c.push(2)

c.pop()
c.pop()
c.pop()
c.pop()
c.print()
