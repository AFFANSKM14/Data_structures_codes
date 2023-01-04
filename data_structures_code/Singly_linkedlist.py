class Node:
    def __init__(self,data=None,next_pointer=None):
        self.data=data
        self.next_pointer=next_pointer
class Slinkedlist:
    def __init__(self):
        self.head=None
    def getlength(self):
        length=0
        itr = self.head
        while itr:
            length+=1
            itr = itr.next_pointer
        return length
    def getmax(self):
        itr=self.head
        maximum=itr.data
        while itr:          
            if itr.next_pointer is None:
                return maximum
            if maximum>itr.next_pointer.data:
                pass
            else:
                maximum=itr.next_pointer.data
            itr=itr.next_pointer
    def getmin(self):
        itr=self.head
        minimum=itr.data
        while itr:
            if itr.next_pointer is None:
                return minimum
            if minimum<itr.next_pointer.data:
                pass
            else:
                minimum=itr.next_pointer.data
            itr=itr.next_pointer
    def insertb(self,data):
        self.head=Node(data,self.head)
    def inserte(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        itr = self.head
        while itr.next_pointer:
            itr=itr.next_pointer
        itr.next_pointer=Node(data,None)
    def insertat(self,data,index):
        if index<0 or index>self.getlength():
            raise Exception('Invalid Index')
        if index == 0:
            self.insertb(data)
        count=1
        itr=self.head
        while itr:
            if count == index:
                itr.next_pointer=Node(data,itr.next_pointer) 
                break
            itr=itr.next_pointer
            count+=1
    def insertbyvalue(self,data_given,data_to_put):
        itr=self.head
        if self.head is None:
            print('Linked list is empty')
        while itr:
            if itr.data == data_given:
                itr.data=data_to_put
            itr=itr.next_pointer
    def removeat(self, index):
        if index<0 or index>=self.getlength():
            raise Exception("Invalid Index")
        if index==0:
            self.head = self.head.next_pointer
            return
        count = 1
        itr = self.head
        while itr:
            if count == index:
                itr.next_pointer = itr.next_pointer.next_pointer
                break
            itr = itr.next_pointer
            count+=1
    def removebyvalue(self,data_given):
        itr=self.head
        if self.head is None:
            print('Linked list is empty')
        if data_given == self.head.data:
                self.head = self.head.next_pointer
                return
        while itr:
            if itr.data == data_given:
                itr.data=itr.next_pointer.data
                itr.next_pointer = itr.next_pointer.next_pointer
                break
            itr = itr.next_pointer                
    def sort(self,key=False):
        if key==True:
            itr=self.head
            for i in range(self.getlength()):
                if self.head is None:
                    print("the list is empty")
                    return
                while True:
                    if itr.next_pointer is None:
                        break
                    if itr.data<itr.next_pointer.data:
                        temp=itr.data
                        itr.data=itr.next_pointer.data
                        itr.next_pointer.data=temp
                    itr=itr.next_pointer
                itr=self.head
        else:
            itr=self.head
            for i in range(self.getlength()):
                if self.head is None:
                    print("the list is empty")
                    return
                while True:
                    if itr.next_pointer is None:
                        break
                    if itr.data>itr.next_pointer.data:
                        temp=itr.data
                        itr.data=itr.next_pointer.data
                        itr.next_pointer.data=temp
                    itr=itr.next_pointer
                itr=self.head

    def print(self):
        if self.head is None:
            print('Linked List is empty')
            return
        itr=self.head
        listr=''
        while itr:
            listr+=str(itr.data)+'  '
            itr=itr.next_pointer
        print(listr)
c=Slinkedlist()
print('insertion from begining')
c.insertb(60)
c.insertb(3)
c.insertb(90)
c.insertb(7)
c.insertb(1)
c.insertbyvalue(3,45)
c.removeat(2)
c.print()

print()
print('maximum number of this list is :',c.getmax())
print()
print('minimum number of this list is :',c.getmin())
print()
print('the length is  :', c.getlength())

