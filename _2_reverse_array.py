# Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.
class array:
    def __init__(self,fix_size):
        self.fix_size=fix_size
        self.lst=[]
        self.length=0

    def add(self,element):
        if self.length<self.fix_size:
            self.lst.append(element)
            self.length+=1
        else:
            print("Array is full")

    def remove(self, index):
        if index<0 or index>=self.length:
            print("Index out of range!!")
        else:
            self.lst.pop(index)
            self.length-=1

    def update(self,index,element):
        if index<0 or index>=self.length:
            print("Index out of range!!")
        elif self.length==self.fix_size:
            print("Array is full")
        else:
            self.lst[index]=element
            self.length+=1

    def insertat(self,index,element):
        if index<0 or index>=self.length:
            print("Index out of range!!")
        elif self.length==self.fix_size:
            print("Array is full")
        else:
            self.lst.insert(index,element)
            self.length+=1
    def reverse_array(self,lst):
        print(lst[::-1])


if __name__=="__main__":
    obj=array(4)
    obj.add(1)
    obj.add(2)
    obj.add(3)
    obj.add(4)
    print("Original array\n",obj.lst)
    print("Reversed array")
    obj.reverse_array(obj.lst)

