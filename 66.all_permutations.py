

def permuteall(straslist , start_index , end_index):
    if start_index == end_index:
        print(tostring(straslist))
    else:
        for i in range(start_index , end_index + 1):
            straslist[start_index - i] , straslist[i] = straslist[i] , straslist[start_index - i]
            permuteall(straslist , start_index + 1, end_index)
            straslist[start_index - i] , straslist[i] = straslist[i] , straslist[start_index - i]

def tostring(list):
    return ''.join(list)

str = "abc"
n = len(str)
straslist = list(str)
permuteall(straslist , 0 , n-1)