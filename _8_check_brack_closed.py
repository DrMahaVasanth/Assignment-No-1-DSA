# Write a program to check if all the brackets are closed in a given code snippet.
lst1=['[','{','(']
lst2=[']','}',')']
def check_parenthesis(string):
    stack=[]
    for i in string:
        if i in lst1:
            stack.append(i)
        elif i in lst2:
            idx=lst2.index(i)
            if ((len(stack)>0)) and (lst1[idx]==stack[len(stack)-1]):
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack)==0:
        return "Balanced"
    else:
        return "Unbalanced"
string="{[({})]}"
print(string,"--",check_parenthesis(string))

string="{[({})}}}"
print(string,"--",check_parenthesis(string))