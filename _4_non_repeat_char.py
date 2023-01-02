#  Write a program to print the first non-repeated character from a string?
from collections import Counter

def first_non_repeat(str1):
        freq=Counter(str1)
        for i in str1:
            if freq[i]==1:
                print("First non-repeating character in given string is",i)
                break
if __name__=="__main__":
    str1=str(input("Enter the string: "))
    first_non_repeat(str1)
