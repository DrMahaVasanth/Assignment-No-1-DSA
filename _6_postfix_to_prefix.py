#  Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression
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

def post_to_pre(expression):
    stack=[]
    length=len(expression)
    for i in range(length):
        if (operator(expression[i])):
            op1=stack[-1]
            stack.pop()
            op2=stack[-1]
            stack.pop()

            temp=expression[i]+op2+op1
            stack.append(temp)
        else:
            stack.append(expression[i])
    res=""
    for i in stack:
        res+=i
    return res

if __name__=="__main__":
    expression="AB+CD-"
    print("Prefix:",post_to_pre(expression))

