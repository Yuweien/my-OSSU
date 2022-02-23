## Function
def getSum(fileDirName):
    import re
    handle = open(fileDirName)
    lines = handle.readlines()
    nums = []
    for line in lines:
        nums += [int(num) for num in re.findall('[0-9]+', line)]
    return sum(nums)

#sample data
getSum('/Users/yuweiwang/Downloads/regex_sum_42.txt')

#Actural data
getSum('/Users/yuweiwang/Downloads/regex_sum_1497882.txt')