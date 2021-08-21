import re
def solution(new_id):
    answer = new_id.lower()
    answer = re.sub('[^0-9a-z\._-]', '', answer)
    answer = re.sub('(\.+)', '.', answer)
    answer = re.sub('^\.', '', answer)
    answer = re.sub('\.$', '', answer)
    if answer == '':
        answer = 'a'
    if len(answer) >= 16:
        answer = answer[:15]
        answer = re.sub('\.$', '', answer)
    if len(answer) <= 2:
        while len(answer) < 3:
            answer += answer[-1]
    return answer
