import numbers


current_position = [0,0,0] # horizon and depth , aim



# input = ['forward 5','down 5','forward 8','up 3','down 8','forward 2'
# ]
with open("D:/input2.txt") as file:
    input = file.readlines()
input = [input[x].strip() for x in range(len(input))]

for i in range(len(input)):
    command = (input[i].split())[0]
    number = int((input[i].split())[1])
    if (command == 'forward') :
        current_position[0] = current_position[0] + number
        current_position[1] = current_position[1] + current_position[2] * number
    if (command == 'up'):
        current_position[2] = current_position[2] - number
    if (command == 'down'):
        current_position[2] = current_position[2] + number
print(current_position[0]*current_position[1])