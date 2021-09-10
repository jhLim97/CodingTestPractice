from collections import defaultdict
            
def solution(record):
    answer = []
    data = []
    dic = defaultdict(int)
    for record_ in record:
        temp = record_.split(' ')
        if temp[0] == 'Change':
            dic[temp[1]] = temp[2]
            continue
        elif temp[0] == 'Enter':
            dic[temp[1]] = temp[2]
        data.append(temp)
    
    for data_ in data:
        if data_[0] == 'Enter':
            answer.append(dic[data_[1]] + "님이 들어왔습니다.")
        elif data_[0] == 'Leave':
            answer.append(dic[data_[1]] + "님이 나갔습니다.")
    return answer
