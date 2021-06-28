def helper(s, n):
    prev = s[:n]
    i = n
    result = ''
    count = 1
    while i + n <= len(s):
        if prev != s[i:i + n]:
            if count == 1:
                result += prev
            else:
                result += (str(count) + prev)
            prev = s[i:i + n]
            count = 1
        else:
            count += 1
        i += n   
        
    if count == 1:
        result += prev
    else:
        result += (str(count) + prev)
    result += s[i:]
    return result

def solution(s):
    answer = 0
    data = [s]
    
    for i in range(1, len(s)):
        data.append(helper(s, i))
    answer = len(min(data, key = lambda x : len(x)))
    return answer
