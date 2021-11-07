alpah_dict = {
    'c=': '1',
    'c-': '2',
    'dz=': '3',
    'd-': '4',
    'lj': '5',
    'nj': '6',
    's=': '7',
    'z=': '8'
}

input = input()
for alpha, value in alpah_dict.items():
    input = input.replace(alpha, value)

print(len(input))
