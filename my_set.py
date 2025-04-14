""" Делаем сет, сделать класс сет сделать чтобы он оставлял только уникальные элементы"""

class MySet:
    def __init__(self, setsize=10):
        self.setsize = setsize
        self.myset = [[] for i in range(self.setsize)]

    def add(self, x):
        if x in self.myset[x % self.setsize]:
            pass
        else:
            self.myset[x % self.setsize].append(x)

    def find(self, x):
        for now in self.myset[x % self.setsize]:
            if now == x:
                return True
        return False

    def delete(self, x):
        xlist = self.myset[x % self.setsize]
        for i in range(len(xlist)):
            if xlist[i] == x:
                xlist[i] = xlist[len(xlist) - 1]
                xlist.pop()
                return self.myset

    def __repr__(self):
        return str(self.myset)


my_set = MySet()

my_set.add(x=25)
my_set.add(x=251)
my_set.add(x=25)
my_set.add(x=265)
my_set.add(x=15)

print(my_set.delete(x=265))
print(my_set.find(x=265))
print(my_set)



