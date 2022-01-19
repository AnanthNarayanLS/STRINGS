
#SPLIT A BINARY STRING INTO 2 SUBTRING WITH EQUAL 0'S AND 1'S ANF IF NOT RETURN -1

def maxsubstr(str , n):
    count0 , count1 , ans = 0 , 0 , 0
    for i in range(n):
        if str[i] == '0':
            count0 += 1
        else:
            count1 += 1
        if count0 == count1:
            ans += 1
    if count0 != count1:
        return -1
    else:
        return ans

str = input("enter the string : ")
print(maxsubstr(str , len(str)))