# Write a program to check if two strings are a rotation of each other?
def check_string(s1,s2,indexfound,size):
    for i in range(size):
        if s1[i]==s2[indexfound]:
            return True

if __name__=="__main__":
    s1='abcd'
    s2='dabc'
    if (len(s1)!=len(s2)):
        print(f"{s2} is not a rotation of {s1}")
    else:
        indexes=[]
        size=len(s1)
        firstchar=s1[0]
        for i in range(size):
            if (s2[i]==firstchar):
                indexes.append(i)
        print(indexes)
        isRotation=False
        for idx in indexes:
            isRotation=check_string(s1,s2,idx,size)
            print(isRotation)
        if isRotation:
            print("strings are rotation of each other")
        else:
            print("Strings are not rotation of each other")