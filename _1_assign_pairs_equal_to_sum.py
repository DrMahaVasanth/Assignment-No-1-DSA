# Write a program to find all pairs of an integer array whose sum is equal to a given number?

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
    def print_pairs(self,lst,n,sum):
        for i in range(n):
            for j in range(n):
                if lst[i]+lst[j]==sum:
                    print("(",lst[i],",",lst[j],")",end=",")
if __name__=="__main__":
    obj=array(4)
    obj.add(1)
    obj.add(2)
    obj.add(3)
    obj.add(4)
    arr=[1,2,3,4]
    print("Original array",obj.lst)
    n=obj.length
    sum=5
    obj.print_pairs(obj.lst,n,sum)