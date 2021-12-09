# Opening input file into a list
input = list()
with open('Day_4_input.txt') as f:
    for line in f:
        input.append(line)


# Isolating the drawn numbers into its own list
drawn_numbers = list()
for line in input:
    if ',' in line:
        drawn_numbers.append(line.replace('\n',''))
        input.remove(line)


print(drawn_numbers)

# Making a dictionary with the board_number as the key and the numbers as the value
boards = dict()
boards_num = 0
temp_list = list()

for line in input:
    a = line.split()
#    print(a)
    if len(a) > 0:
        for num in a:
            temp_list.append(num)
            if boards_num == 100 and len(temp_list) == 25:
                boards[boards_num] = temp_list
    else:
        boards[boards_num] = temp_list
#        print(boards[boards_num])
        temp_list = list()
        boards_num = boards_num + 1

#print(boards[99])
#print(boards[100])

# Winning possibilities
bingo_positions = [[0,1,2,3,4]
         , [5,6,7,8,9]
         , [10,11,12,13,14]
         , [15,16,17,18,19]
         , [20,21,22,23,24]
         , [0,5,10,15,20]
         , [1,6,11,16,21]
         , [2,7,12,17,22]
         , [3,8,13,18,23]
         , [4,9,14,19,24]
         , [0,6,12,18,24]
         , [4,8,12,16,20]
         ]

checking_bingo = dict()
#for i in range(1,max(boards.keys()) + 2):
#    print(i)
#    print(boards[i])

#for number in drawn_numbers:
#    for i in range(1,5):
#        print(i)
#        for num in boards[i]:
#            if num == number:
#                then
#            print(boards[i])
#            print(num)