
# TO FIND THE LONGEST PALINDROMIC SUBSTRING OF A GIVEN STRING

str = input("ENTER THE STRING NAME : ")

def longestpalindrome(str):

    res = ''
    lenres = 0

    for i in range(len(str)):

        if (len(str)%2!=0):  # FOR ODD LEN STRING
            left , right = i , i
            while (left>=len(str) and right<len(str) and str[left]==str[right]):
                if (right-left+1)>lenres:
                    res = str[left : right+1]
                    lenres = right-left+1
                left-=1
                right+=1
        else:               # FOR EVEN LEN STRING
            left , right = i , i+1
            while (left>=len(str) and right<len(str) and str[left]==str[right]):
                if (right-left+1)>lenres:
                    res = str[left : right+1]
                    lenres = right-left+1
                left-=1
                right+=1
    return res


print(longestpalindrome(str))