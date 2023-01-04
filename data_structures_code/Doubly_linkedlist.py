class Node:
    def __init__(self,data,next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev
class Dlinkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
    def getlength(self):
        itr=self.tail
        length=0
        while itr:
            length+=1
            itr=itr.prev
        return length
    def getmax(self):
        itr=self.head
        maximum=itr.data
        while itr:          
            if itr.next is None:
                return maximum
            if maximum>itr.next.data:
                pass
            else:
                maximum=itr.next.data
            itr=itr.next
    def getmin(self):
        itr=self.head
        minimum=itr.data
        while itr:
            if itr.next is None:
                return minimum
            if minimum<itr.next.data:
                pass
            else:
                minimum=itr.next.data
            itr=itr.next
    def printf(self):
        itr=self.head
        listr=''
        while itr:
            listr+=str(itr.data)+' '
            itr=itr.next
        print(listr)
    def printb(self):
        itr=self.tail
        listr=''
        while itr:
            listr+=str(itr.data)+' '
            itr=itr.prev
        print(listr)

    def insertb(self,data):
        node=Node(data)
        if self.head is None and self.tail is None:
            self.head=node
            self.tail=node
        else:
            self.head.prev=node
            node.next=self.head
            self.head=node
    def inserte(self,data):
        if self.head is None and self.tail is None:
            node=Node(data)
            self.head=node
            self.tail=node
        else:
            node=Node(data)
            prev_node=self.head
            while True:
                if prev_node.next is None:
                    break
                prev_node=prev_node.next
            prev_node.next=node
            node.prev=prev_node
        self.tail=node
    def insertat(self,index,data,reverse=False):
        if index<0 or index>self.getlength():
            raise Exception('Invalid Index')
        if reverse == False:
            if index == 0:
                first=self.head
                node=Node(data,first)
                first.prev=node
                self.head=node
            itr=self.head
            itr1=self.tail
            count=1
            length=self.getlength()
            while itr:
                prev=itr
                front=itr1
                if count==index:
                    node=Node(data)
                    prev.next=node
                    node.prev=prev
                    while length!=(count+1):
                        length-=1
                        front=front.prev
                    node.next=front
                    front.prev=node
                    return
                count+=1
                itr=itr.next
        else:
            if index == 0:
                last=self.tail
                node=Node(data)
                node.prev=last
                self.tail=node
            itr=self.head
            itr1=self.tail
            count=1
            length=self.getlength()
            while itr:
                prev=itr
                front=itr1
                if count==index:
                    node=Node(data)
                    while length!=(count+1):
                        length-=1
                        prev=prev.next
                    prev.next=node
                    node.prev=prev
                    node.next=front
                    front.prev=node
                    return
                count+=1
                itr1=itr1.prev
    def insertbyvalue(self,data_given,data_to_put,reverse=False):
        if reverse == False:
            itr=self.head
            while itr:
                if itr.data == data_given:
                    itr.data=data_to_put
                    break
                itr=itr.next
        else:
            itr1=self.tail
            while itr1:
                if itr1.data == data_to_put:
                    itr1.data=data_to_put
                    break
                itr1=itr1.prev
    def remove(self,index,reverse=False):
        if reverse == False:
            if index==0:
                self.head=self.head.next
                self.head.prev=None
                return
            count=1
            length=self.getlength()
            while True:
                prev=self.head
                front=self.tail
                if count==index:
                    prev.next=prev.next.next
                    while length!=(count+1):
                        length=length-1
                        front=front.prev
                    front.prev=front.prev.prev
                    break
                count+=1
        else:
            if index==0:
                self.tail=self.tail.prev
                self.tail.next=None
                return
            count=1
            length=self.getlength()
            while True:
                prev=self.head
                front=self.tail
                if count==index:
                    front.prev=front.prev.prev
                    while length!=(count+1):
                        length=length-1
                        prev=prev.next
                    prev.next=prev.next.next
                    break
                count+=1
    def removebyvalue(self,data_given,reverse=False):
        itr=self.head
        itr1=self.tail
        length=self.getlength()
        count=1
        if data_given == self.head.data:
            self.head = self.head.next_pointer
            self.head.prev=None
            return
        if data_given == self.tail.data:
            self.tail=self.tail.prev
            self.tail.next=None
            return
        if reverse==False:
            while itr:
                if itr.data == data_given:
                    itr.data=itr.next.data
                    itr.next=itr.next.next
                    while length!=(count+1):
                        length-=1
                        itr1=itr1.prev
                    itr1.prev=itr1.prev.prev
                    return
                count+=1
                itr=itr.next
        else:
            while itr1:
                if itr1.data == data_given:
                    itr1.data=itr1.next.data
                    itr1.prev=itr1.prev.prev
                    while length!=(count+1):
                        length-=1
                        itr=itr.next
                    itr.next=itr.next.next
                    return
                count+=1
                itr1=itr1.prev

c=Dlinkedlist()
c.inserte(5)
c.inserte(6)
c.inserte(7)
c.inserte(8)
c.insertat(1,10)
c.getlength()
c.insertbyvalue(5,1,reverse=False)
c.removebyvalue(7,reverse=True)
c.printf()
print()
c.printb()
print(c.getmax())
print()
print(c.getmin())
