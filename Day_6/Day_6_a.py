input = []

with open('Day_6_input.txt') as f:
    for line in f:
        for num in line:
            if num != ',':
                input.append(int(num))

print(input)
print('Len:' + str(len(input)))
days_left = 80

while days_left > 0:
    for i in range(len(input)):
        if input[i] == 0:
            input[i] = 6
            input.append(8)
        else:
            input[i] -= 1
    days_left -= 1

print(len(input))