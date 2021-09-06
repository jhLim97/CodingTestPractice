import re
def solution(s):
    answer = []
    
    p = re.compile('{([0123456789,]*)}')
    result = p.findall(s)
    temp = []
    for data in result:
        temp.append(data.split(','))
    temp = sorted(temp, key = lambda x : len(x))
    for data in temp:
        for data_ in data:
            if int(data_) not in answer:
                answer.append(int(data_))
    
    return answer
