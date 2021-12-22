a = list()

with open('Day_1_input.txt') as f:
    for line in f:
        num = int(line)
        a.append(num)
#print(a)

increase = 0
decrease = 0

for i in range(len(a)-1):

    if a[i+1] > a[i]:
        increase = increase + 1
    else:
        decrease = decrease + 1

print(increase)
print(decrease)