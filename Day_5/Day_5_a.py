## Opening input file into a list
start = list()
end = list()

with open('Day_5_input.txt') as f:
    for line in f:
        a = line.replace('\n', '')
        b = a.split('->')
        #print(b)
        start.append(b[0])
        end.append(b[1])

#print(len(start))
#print(end)

## divide up x and y coords
x1 = list()
y1 = list()
for num in start:
    a = num.replace(' ','')
    b = a.split(',')
    x1.append(b[0])
    y1.append(b[1])

x2 = list()
y2 = list()
for num in end:
    a = num.replace(' ','')
    b = a.split(',')
    x2.append(b[0])
    y2.append(b[1])

#print(len(x1))
#print(y1)
#print(x2)
#print(y2)

## Horizontal - check 2+ overlap
x_pairs = list()
for i in range(len(x1)):
    if x1[i] == x2[i]:
        for j in range(min(int(y1[i]),int(y2[i])),max(int(y1[i]),int(y2[i]))+1):
            #print(j)
            #print(abs(int(y1[i]) - int(y2[i])))
            #print(str(x1[i])+'-'+str(j))
            x_pairs.append(str(x1[i])+'-'+str(j))




## Vertical - check 2 + overlap
y_pairs = list()
for i in range(len(y1)):
    if y1[i] == y2[i] and x1[i] != x2[i]:
        for j in range(min(int(x1[i]),int(x2[i])),max(int(x1[i]),int(x2[i]))+1):
            #print(j)
            #print(abs(int(x1[i]) - int(x2[i])))
            #print(str(str(j)) + '-' + y1[i])
            y_pairs.append(str(j)+'-'+str(y1[i]))

#print(x_pairs)
#print(y_pairs)
#print(len(x_pairs))
#print(len(y_pairs))

## Counter
counter = {}
for pair in x_pairs:
    if pair not in counter:
        counter[pair] = 1
    else:
        counter[pair] += 1
for pair in y_pairs:
    if pair not in counter:
        counter[pair] = 1
    else:
        counter[pair] += 1
#print(counter)


## Final list
final_list = list()
for key in counter.keys():
    if counter[key] > 1:
        final_list.append(key)

print(len(final_list))
