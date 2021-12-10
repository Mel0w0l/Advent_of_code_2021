## Opening input file into a list
input = list()
with open('Day_5_input.txt') as f:
    for line in f:
        a = line.replace('\n','')
        b = a.split('->')
        for line_a in b:
            c = line_a.split(',')
            for line_b in c:
                d = line_b.split(',')
                for num in d:
                    input.append(num.replace(' ',''))

print(input)

#list_a = list()
#for line in input:
#    for x_y in line:
#        a = x_y.split(',')
#        list_a.append(a)

#print(list_a)
