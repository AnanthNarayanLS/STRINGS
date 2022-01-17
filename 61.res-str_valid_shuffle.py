
# CHECK IF THE RESULTANT STRING IS A VALID SHUFFLE OF THE GIVEN TWO STRINGS

str1 = input("enter the string1 : ")
str2 = input("enter the string2 : ")
res_str = input("enter the resultant string  : ")

if ((len(str1)+len(str2)) != len(res_str)):
    print("STRING LENGTHS ARE NOT VALID !! ")
else:
    i,j,k = 0,0,0
    while (k < len(res_str)):
        if (i < len(str1) and str1[i] == res_str[k]):
            i+=1
        elif (j < len(str2) and str2[j] == res_str[k]):
            j+=1
        else:
            break
        k+=1
    if (i < len(str1) or j < len(str2)):
        print("INVALID SHUFFLE")
    else:
        print("VALID SHUFFLE")

