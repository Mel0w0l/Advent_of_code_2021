binary = list()

with open('Day_3_input.txt') as f:
    for line in f:
        binary.append(line.rstrip())

new_binary = binary

print(binary)
print(new_binary)

for i in range(len(line)):
    temp = list()
    for line in new_binary:
        temp.append(line[i])
    most_common_item = max(temp, key=temp.count)
    for line in new_binary:
        if line[i] != most_common_item:
            new_binary.remove(line)
    print(new_binary)



