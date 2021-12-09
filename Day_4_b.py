## Opening input file into a list
input = list()
with open('Day_4_input.txt') as f:
    for line in f:
        input.append(line)


## Isolating the drawn numbers into its own list
temp_list = list()
for line in input:
    if ',' in line:
        temp_list.append(line.replace('\n',''))
        input.remove(line)
        drawn_numbers = temp_list[0].split(",")

#print(drawn_numbers)


## Making a dictionary with the board_number as the key and the numbers as the value
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

## Winning possibilities
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

## Empty dictionary to mark off bingo board positions
checking_bingo = dict()
for i in range(1,max(boards.keys()) + 1):
    checking_bingo[i] = list()

#    checking_bingo[i].append(i)

## Checking for bingo
winning_board = 0
winning_board_marked_pos = 0
finished_boards = list()

for number in drawn_numbers:
    if len(finished_boards) < 100:
    #    print(number)
        for i in range(1,max(boards.keys()) + 1):
            for num in boards[i]:
                if num == number:
                    checking_bingo[i].append(boards[i].index(num))
    #            print(checking_bingo[i])
                for j in range(len(bingo_positions)):
                    result = all(elem in checking_bingo[i] for elem in bingo_positions[j])
                    if result:
                        if i not in finished_boards:
                            finished_boards.append(i)
                        else:
                            continue
                        if len(finished_boards) == 100:
                            winning_board = i
                            winning_board_marked_pos = checking_bingo[i]
                            break
                        else:
                            continue
                    else:
                        continue
    else:
        break

print('Winning board no: ' + str(winning_board))
print('Winning positions:')
print(winning_board_marked_pos)
print('Winning board')
print(boards[winning_board])

## Calculating the board score
score = 0
for num in boards[winning_board]:
#    print(num)
    if boards[winning_board].index(num) not in winning_board_marked_pos:
        score += int(num)
#        print(score)

last_num = boards[winning_board][int(winning_board_marked_pos[len(winning_board_marked_pos)-1])]
#print(last_num)

final_score = score * int(last_num)
print('Final Score: ' + str(final_score))