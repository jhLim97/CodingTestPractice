s = input()

def reverse_word():
    global start, end, s
    if start != -1:
        if end != -1:
            converted_data = s[start:end + 1]
            s = s[:start] + converted_data[::-1] + s[end + 1:]
        start, end = -1, -1


closed = True
start = -1
end = -1
for index, s_ in enumerate(s):
    if s_ == '<':
        reverse_word()
        closed = False
    elif s_ == '>':
        closed = True
    elif closed and s_ == ' ':
        reverse_word()
    elif closed:
        if start == -1:
            start = index
        else:
            end = index

reverse_word()
print(s)
