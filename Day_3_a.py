binary = list()

with open('Day_3_input.txt') as f:
    for line in f:
        binary.append(line.rstrip())

gamma = list()
epsilon = list()

for i in range(len(line)):
    temp = list()
    for line in binary:
        temp.append(line[i])
    most_common_item = max(temp, key=temp.count)
    least_common_item = min(temp, key=temp.count)
    gamma.append(most_common_item)
    epsilon.append(least_common_item)

gamma_rate = int(''.join(gamma),2)
epsilon_rate = int(''.join(epsilon),2)
print(gamma_rate)
print(epsilon_rate)

print('input: '+ str(gamma_rate * epsilon_rate))