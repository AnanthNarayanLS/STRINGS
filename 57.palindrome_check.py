
str1 = input("enter the string name : ")

# USING SLICING
if(str1 == str1[::-1]):
    print("the string is palindrome")
else:
    print("the string is not palindrome !! ")

# USING RECURSION
def reverse(str1):
    if len(str1)==0:
        return str1
    else:
        return reverse(str1[1:]) + str1[0]
rev_str1 = reverse(str1)
if(str1 == rev_str1):
    print("the string is palindrome")
else:
    print("the string is not palindrome !! ")
