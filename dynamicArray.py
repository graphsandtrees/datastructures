import time
import random

def nothing(length):
    l = [None for i in range(length)]
    return l
print(nothing(3))
class dynamicArray:
    def __init__(self, data):
        self.data = data
        self.length = len(data)

    def append(self, value):
        if self.length == len(self.data):
            tempdata = self.data
            self.data = tempdata + [value] + nothing(self.length-1)
            for i in range(self.length):
                self.data[i] = tempdata[i]
            self.data[self.length] = value
            self.length += 1
        else:
            self.data[self.length] = value
            self.length+=1

    def delete_last_element(self):
        val = self.data[self.length-1]
        self.data[self.length-1] = None
        return val
    def dumbappend(self, value):
        if (self.length) == len(self.data):
            tempdata = self.data
            self.data = nothing(self.length+1)
            for i in range(self.length):
                self.data[i] = tempdata[i]
            self.data[self.length] = value
            self.length += 1
        else:
            self.data[self.length] = value
            self.length+=1

#testing

a = dynamicArray([1,2,3])

a.append(4)
print(a.data)
a.delete_last_element()
print(a.data)

#testing program

normaladddifferences = []
values = [random.randint(10,300000) for i in range(10)]
for j in range(10):
    test = dynamicArray([0])
    start = time.clock()
    for i in range(values[j]):
        test.append(0)
    stop = time.clock()
    normaladddifferences.append(stop-start)

print(values)
print(normaladddifferences)





dumbadddifferences = []
dumbvalues = []
for j in range(10):
    test = dynamicArray([0])
    start = time.clock()
    for i in range(values[j]):
        test.dumbappend(0)
    stop = time.clock()
    dumbadddifferences.append(stop-start)
    print('completed')


print(dumbadddifferences)

deletedifferences = []
for j in range(10):
    test = dynamicArray([0]*(values[j]+1))
    start = time.clock()
    for i in range(values[j]):
        test.delete_last_element()
    stop = time.clock()
    deletedifferences.append(stop-start)

print deletedifferences
