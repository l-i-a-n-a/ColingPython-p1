class OneIndexedList:

    def __init__(self, items=None):
        self.items = items or []

    def __getitem__(self, idx):
        return self.items[idx-1]

    def __setitem__(self, idx, value):
        self.items[idx-1] = value
        return value

a = OneIndexedList([])
a.items.append(0)
print(a[1])

b = OneIndexedList([2,3,5,8,9,4])
b[4] = 17
print(b[4])
