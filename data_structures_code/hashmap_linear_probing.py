class Hash:
    def __init__(self,size):
        self.size=size
        self.list=[None for i in range(self.size)]
        self.h1=[]
    def geth(self):
        h=0
        if self.list[h] ==None:
            return h
        for i in range(len(self.list)):
            if self.list[h] is not None:
                h+=1
        return h
    def __setitem__(self,key,value):
        h=self.hashmap(key)
        if h not in self.h1:
            self.h1.append(h)
            self.list[h]=(key,value)
            return
        elif h in self.h1:
            h=h+1
            if h>=len(self.list):
                h=self.geth()
                if h not in self.h1:
                    self.h1.append(h)
                    self.list[h]=(key,value)
                    return
            self.h1.append(h)
            self.list[h]=(key,value)
        return self.list[h]
    def get(self,key):
        h=self.hashmap(key)
        #if self.list[h][0]==key:
         #   yield self.list[h]
        #else:
        for i in range(len(self.list)):
            if self.list[i] is None:
                continue
            if self.list[i][0]==key :
                yield self.list[i]
    def hashmap(self,key):
        hash=0
        for k in key:
            hash+=ord(k)
        h=hash%self.size
        return h

c=Hash(10)
c['march 5']=132
c['march 5']=135
c['march 6']=142
c['march 6']=165
c['march 6']=156
c['march 6']=156
c['march 6']=156
c['dec 6']=126
print(c.hashmap('dec 6'))
print(c.list)
for i in c.get('dec 6'):
    print(i,end='')
