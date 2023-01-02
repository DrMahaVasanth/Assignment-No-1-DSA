#  Write a program to find the smallest number using a stack.
class minstack:
    def __init__(self):
        self.data = []
    class node:
        def __init__(self,val,Min):
            self.val=val
            self.min=Min
    def push(self,element):
        if not self.data:
            self.data.append(self.node(element,element))
        else:
            Min=min(self.data[-1].min,element)
            self.data.append(self.node(element,Min))

    def pop(self):
        return self.data.pop().val

    def top(self):
        return self.data[-1].val
    def get_min(self):
        return self.data[-1].min

obj=minstack()
obj.push(20)
obj.push(10)
obj.push(30)
obj.push(3)
obj.push(12)
print("Minimum among the elements in the stack")
print(obj.get_min())
print(obj.pop())
print("Minimum among the elements in the stack")
print(obj.get_min())



