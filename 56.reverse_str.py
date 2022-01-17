
# TO REVERSE A STRING

str_name = input("enter the string name : ")

# GENERAL METHOD
print(str_name[ : :-1])

# USING RECURSION
def reverse(str_name):
    if len(str_name) == 0:
        return str_name
    else:
        return reverse(str_name[1:]) + str_name[0]
print(reverse(str_name))

#USINF LOOPS
for i in range(len(str_name)-1 , -1 , -1):
    print(str_name[i] , end = '')
