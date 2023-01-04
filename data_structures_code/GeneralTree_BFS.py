class Treenode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None
    def addchild(self,child):
        child.parent=self
        self.children.append(child)
    def BFS(self):
        if len(self.children)>=0:
            self.push(self.data)
            for i in self.children:
                self.push(i)
            list1.append(list[0])
            self.pop()
            for i,j in enumerate(list):
                x=isinstance(j,str)#removing objects 
                if x is True:
                    list1.append(j)
                    list.pop(i)
            if len(list)==0:
                return
            self=list[0]
            self.BFS()
    def push(self,data):
        list.append(data)
    def pop(self):
        list.pop(0)
    def print(self):
        listr=''
        for i,j in enumerate(list1):
            y=isinstance(j,str)
            if y is True:
                listr+=str(j)+' '
        return listr
list=[]
list1=[]
laptop=Treenode('laptop')
microsoft=Treenode('microsoft')
mac=Treenode('mac') 
pixelbook=Treenode('pixelbook')
A11=Treenode('Android 11')
microsoft.addchild(Treenode('Windows 10'))
microsoft.addchild(Treenode('Windows 11'))
mac.addchild(Treenode('ios 13'))
mac.addchild(Treenode('ios 14'))
pixelbook.addchild(Treenode('Android 10'))
A11.addchild(Treenode('Beta version'))
pixelbook.addchild(A11)
laptop.addchild(microsoft)
laptop.addchild(mac)
laptop.addchild(pixelbook)
laptop.BFS()
print(laptop.print())
