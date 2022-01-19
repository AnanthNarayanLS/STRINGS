
def printsubsequence(user_str , output_str):

    if (len(user_str) == 0):
        print(output_str,end='\n')
        return
    printsubsequence(user_str[1:] , output_str + user_str[0])
    printsubsequence(user_str[1:] , output_str )

print(printsubsequence('abcd',''))