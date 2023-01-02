#  Read about the Tower of Hanoi algorithm. Write a program to implement it.
def tower_of_hanoi(n,source,destination,auxillary):
    if n==1:
        print("Move disk 1 from source",source,"to destination",destination)
        return
    tower_of_hanoi(n-1,source,auxillary,destination)
    print("Move disk",n, "from source",source,"to destination",destination)
    tower_of_hanoi(n-1,auxillary,destination,source)
   
    
if __name__=="__main__":
    n=4
    tower_of_hanoi(n,'A','B','C')
