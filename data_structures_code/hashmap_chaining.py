class Hash:
    def __init__(self,size):
        self.size=size
        self.list=[[] for i in range(self.size)]
    def __setitem__(self,key,value):
        h=self.hashmap(key)
        found = False
        for i,element in enumerate(self.list[h]):
            if len(element)==2 and element[0]==key:
                self.list[h].append((key,value))
                found=True
                break
        if not found:
            self.list[h].append((key,value))
    def get(self,key):
        h=self.hashmap(key)
        c=[]
        key1=[]
        if len(self.list[h])>1: 
            for i,elem in enumerate(self.list[h]):
                if elem[0] == key:
                    yield elem
        else:
            yield self.list[h]
    def hashmap(self,key):
        hash=0
        for k in key:
            hash+=ord(k)
        return hash%self.size
c=Hash(10)
print('Hash values of particular keys are :')
print()
c['march 17']=156
print('17 is',c.hashmap('march 17'))
c['march 17']=651
print('17 is',c.hashmap('march 17'))
c['march 6']=151
print('6 is',c.hashmap('march 6'))
c['march 9']=152
print('9 is',c.hashmap('march 9'))
c['march 7']=153
print('7 is',c.hashmap('march 7'))
c['march 2']=154
print('2 is',c.hashmap('march 2'))
c['march 2']=154
print('2 is',c.hashmap('march 2'))
c['march 2']=154
print('2 is',c.hashmap('march 2'))
c['march 8']=155
print('8 is',c.hashmap('march 8'))
c['march 30']=156
print('30 is',c.hashmap('march 30'))
c['march 29']=157
print('29 is',c.hashmap('march 29'))
c['march 26']=158
print('26 is',c.hashmap('march 26'))
c['march 16']=159
print('16 is',c.hashmap('march 16'))
print()
print()
print(c.list)
print()
print("the value('s) of key march 17 is")
for i in c.get('march 17'):
    print('\n')

    print(i,end='')
