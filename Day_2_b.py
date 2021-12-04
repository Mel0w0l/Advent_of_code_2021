direction = list()
magnitude = list()

with open('Day_2_input.txt') as f:
    for line in f:
        temp = line.split()
        direction.append(temp[0])
        magnitude.append(int(temp[1]))

horizontal = 0
depth = 0
aim = 0

for i in range(len(direction)):
    if direction[i] == 'forward':
        horizontal = horizontal + magnitude[i]
        depth = depth + (aim * magnitude[i])
    elif direction[i] == 'down':
        aim = aim + magnitude[i]
    elif direction[i] == 'up':
        aim = aim - magnitude[i]

print(horizontal)
print(depth)

print('input:' + str(horizontal*depth))