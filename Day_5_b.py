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

## Horizontal - check 2+ overlap
x_pairs = list()
for i in range(len(x1)):
    if x1[i] == x2[i]:
        for j in range(min(int(y1[i]),int(y2[i])),max(int(y1[i]),int(y2[i]))+1):
            x_pairs.append(str(x1[i])+'-'+str(j))

## Vertical - check 2 + overlap
y_pairs = list()
for i in range(len(y1)):
    if y1[i] == y2[i] and x1[i] != x2[i]:
        for j in range(min(int(x1[i]),int(x2[i])),max(int(x1[i]),int(x2[i]))+1):
            y_pairs.append(str(j)+'-'+str(y1[i]))

########################################################################################
## Diagonal - check 2+ overlap
dia_pairs = list()
y_start = 0
for i in range(len(x1)):
    if x1[i] != x2[i] and y1[i] != y2[i]:
        if min(int(x1[i]),int(x2[i])) == int(x1[i]): #start with y1[i]
            y_start = int(y1[i])
            for j in range(min(int(x1[i]), int(x2[i])), max(int(x1[i]), int(x2[i])) + 1):
                #print('start with x1 y1')
                dia_pairs.append(str(j) + '-' + str(y_start))
                #print(str(j) + '-' + str(y_start))
                if y1[i] > y2[i]: # /
                    y_start -= 1
                else:
                    y_start += 1

        else:
            y_start = int(y2[i]) # start with y2[i]
            for j in range(min(int(x1[i]), int(x2[i])), max(int(x1[i]), int(x2[i])) + 1):
                #print('start with x2,y2')
                dia_pairs.append(str(j) + '-' + str(y_start))
                #print(str(j) + '-' + str(y_start))
                if y2[i] > y1[i]: # /
                    y_start -= 1
                else:
                    y_start += 1

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
for pair in dia_pairs:
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
