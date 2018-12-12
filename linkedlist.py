class link:
    __init__(self,data):
        self.value = data
        self.prev = None
        self.next = None
class linkedList:
    __init__(self):
        self.currentnode = None
        self.printnode = None
        self.length = 0
    append(self, data):
        c = 0
        newnode = link(data)
        newnode.prev = self.currentnode
        self.currentnode.next = newnode
        self.currentnode = newnode
        self.printnode = newnode
    deletelast(self):
        self.currentnode = self.currentnode.prev
        self.currentnode.next = None
        self.printnode = self.currentnode
    showlist(self):
        c = 0
        datalist = []
        while self.printnode.prev != None:
            datalist.insert(0,self.printnode.value)
            self.printnode = self.printnode.prev
        return datalist
    create(data = None):
        c = 0
        if data != None:
            assert type(data) = 'list'
            for i in data:
                self.append(i)
    reverse():
        c = 0
        
