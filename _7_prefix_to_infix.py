#  Write a program to convert prefix expression to infix expression.
def operator(x):
    if x=="+":
        return True
    if x=="-":
        return True
    if x=="*":
        return True
    if x=="/":
        return True
    return False

def pre_to_in(expression):
    stack=[]
    i=len(expression)-1
    while i>=0:
        if not operator(expression[i]):
            stack.append(expression[i])
            i-=1
        else:
            str="("+stack.pop()+expression[i]+stack.pop()+")"
            stack.append(str)
            i-=1
    return stack.pop()

if __name__=="__main__":
    expression="*-A/BC-/AKL"
    print(pre_to_in(expression))