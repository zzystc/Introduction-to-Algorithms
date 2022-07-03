class Stack():
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items) - 1]
    def size(self):
        return self.items[len(self.items)]
    
s = Stack()
num = int(input())
for i in range(num):
    a=input()
    if a[0:4] == 'push':
        b = a.split(' ')
        s.push(int(b[1]))
    if a == 'pop':
        if s.isEmpty() == True:
            print('error')
        else:
            print(s.peek())
            s.pop()
    if a == 'top':
        if s.isEmpty() == True:
            print('error')
        else:
            print(s.peek())