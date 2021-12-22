a = list()

with open('Day_1_input.txt') as f:
    for line in f:
        num = int(line)
        a.append(num)

b = list()

for i in range(len(a)-2):
    b.append(a[i]+a[i+1]+a[i+2])

increase = 0
decrease = 0

for i in range(len(b)-1):
    if b[i+1] > b[i]:
        increase = increase + 1
    else:
       decrease = decrease + 1

print(increase)
print(decrease)