
# TO CHECK WHETHER STRING1 IS A ROTATION OF ANOTHER STRING

str1 = input("enter the string 1 : ")
str2 = input("enter the string 2 : ")

def are_rotate(str1 , str2):
    temp = ""

    if len(str1) != len(str2):
        print("THE STRINGS ARE NOT OF SAME LENGTH !! ")

    temp = str1 + str2

    if (temp.count(str2) > 0):
        return 1
    else:
        return 0

print(are_rotate(str1 , str2))