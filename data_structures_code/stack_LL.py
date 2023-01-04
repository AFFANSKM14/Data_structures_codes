class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class StackLL:
    def __init__(self):
        self.top=None
    def push(self,data):
        self.top=Node(data,self.top)
    def pop(self):
        self.top=self.top.next
    def print(self):
        itr=self.top
        listr=''
        while itr:
            listr+=str(itr.data)+' '
            itr=itr.next
        print(listr)
c=StackLL()
c.push(5)
c.push(6)
c.push(7)
c.push(8)
c.push(9)
c.print()
c.pop()
c.pop()
c.pop()
c.print()
