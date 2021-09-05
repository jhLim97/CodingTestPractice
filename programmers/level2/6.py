import re
def helper(str):
    p = re.compile('[a-z]{2}')
    answer = p.findall(str)
    if not answer:
        return False
    return True

def intersection(str1, str2):
    result = []
    for str1_ in str1:
        if str1_ in str2 and result.count(str1_) < str2.count(str1_):
            result.append(str1_)
    return result

def union(str1, str2):
    result = str1[:]
    for str2_ in str2:
        if str2_ not in result or result.count(str2_) < str2.count(str2_):
            result.append(str2_)
    return result

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    str1List = []
    str2List = []
    for i in range(len(str1) - 1):
        temp = str1[i:i+2]
        if helper(temp):
            str1List.append(temp)
    for i in range(len(str2) - 1):
        temp = str2[i:i+2]
        if helper(temp):
            str2List.append(temp)
    result1 = intersection(str1List, str2List)
    result2 = union(str1List, str2List)
    if not result1 and not result2:
        return 65536
    result = (len(result1) / len(result2)) * 65536
    return int(result)
