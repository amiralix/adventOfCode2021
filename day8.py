ZERO = 6
ONE = 2
TWO = 5
THREE = 5
FOUR = 4
FIVE = 5
SIX = 6
SEVEN = 3 
EIGHT = 7
NONE = 6

with open("D:/day8.txt") as file:
    input = file.readlines()

input = [(((x.split("|"))[1]).strip().split(" ")) for x in input]

one = 0
four = 0
seven = 0
eight = 0
for row in range(0,len(input)):
    # print("\n")
    for column in range(0,4):
        if len(input[row][column]) == ONE:
            one += 1
        if len(input[row][column]) == FOUR:
            four += 1
        if len(input[row][column]) == SEVEN:
            seven += 1
        if len(input[row][column]) == EIGHT:
            eight += 1
print(one+four+seven+eight)
        
