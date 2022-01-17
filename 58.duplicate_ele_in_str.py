
str1 = input("enter the string name : ")

for i in range(len(str1)):
    for j in range(i+1 , len(str1)):
        if str1[i] == str1[j]:
            print(f"the duplicate element is {i},{j}")
