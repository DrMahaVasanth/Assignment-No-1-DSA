# Write a program to reverse a stack.
class stack:
    def __init__(self):
        self.data = []

    def push(self,element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def display(self):
        print(self.data)

    def isEmpty(self):
        return self.data==[]

def insert(s,element):
        if s.isEmpty():
            s.push(element)
        else:
            popped=s.pop()
            insert(s,element)
            s.push(popped)
            
def reverse_stack(s):
        if s.isEmpty():
            pass
        else:
            popped=s.pop()
            reverse_stack(s)
            insert(s,popped)
            
obj=stack()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
obj.push(5)
print("Original Stack")
obj.display()
print("Reversed stack")
reverse_stack(obj)
obj.display()

