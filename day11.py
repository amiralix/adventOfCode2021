import numpy as np

def do_flash_dumbo(input):
    for row in range(0,len(input)):
        for column in range(0,len(input[0])):
            if( flash_status[row][column] == 1 ):
                flash_status[row][column] = 1
                update_adjacents(input,row,column)
                input[row][column] = 0


def check_dumbo_flash(input):
    flash_status = np.zeros((len(input),len(input[0])))
    for row in range(0,len(input)):
        for column in range(0,len(input[0])):
            if( input[row][column] >= 9):
                flash_status[row][column] = 1
                

def update_adjacents(input,row,column):
    if row == 0 and column == 0:
        #done
        if flash_status[row][column+1] == 0:
            input[row][column+1] +=1
        if flash_status[row+1][column] == 0:
            input[row+1][column] +=1
        if flash_status[row+1][column+1] == 0:
            input[row+1][column+1] +=1
        #done
    if row == 0 and column == len(input):
        #done
        if flash_status[row][column-1] == 0:
            input[row][column-1] +=1
        if flash_status[row+1][column] == 0:
            input[row+1][column] +=1
        if flash_status[row+1][column-1] == 0:
            input[row+1][column-1] +=1
        #done
    if row == len(input) and column == 0:
        #done
        if flash_status[row-1][column] == 0:
            input[row-1][column] +=1
        if flash_status[row-1][column+1] == 0:
            input[row-1][column+1] +=1
        if flash_status[row][column+1] == 0:
            input[row][column+1] +=1
        #done
    if row == len(input) and column == len(input):
        #done
        if flash_status[row][column-1] == 0:
            input[row][column-1] +=1
        if flash_status[row-1][column] == 0:
            input[row-1][column] +=1
        if flash_status[row-1][column-1] == 0:
            input[row-1][column-1] +=1
        #done
# check for row not to be 0 or max
    if ( 0 < row < len(input)):
        if (  0 < column < len(input[0]) ):
        #done
            if flash_status[row][column-1] == 0:
                input[row][column-1] +=1
            if flash_status[row-1][column-1] == 0:
                input[row-1][column-1] +=1
            if flash_status[row-1][column] == 0:
                input[row-1][column] +=1
            if flash_status[row-1][column+1] == 0:
                input[row-1][column+1] +=1
            if flash_status[row][column+1] == 0:
                input[row][column+1] +=1
            if flash_status[row+1][column-1] == 0:
                input[row+1][column-1] +=1
            if flash_status[row+1][column+1] == 0:
                input[row+1][column+1] +=1
            if flash_status[row+1][column] == 0:
                input[row+1][column] +=1
        #done
        if column == 0:
            #done
            if flash_status[row-1][column] == 0:
                input[row-1][column] +=1
            if flash_status[row+1][column] == 0:
                input[row+1][column] +=1
            if flash_status[row][column+1] == 0:
                input[row][column+1] +=1
            if flash_status[row-1][column+1] == 0:
                input[row-1][column+1] +=1
            if flash_status[row+1][column+1] == 0:
                input[row+1][column+1] +=1
            #done
        if column == len(input[0]):
            #done
            if flash_status[row-1][column] == 0:
                input[row-1][column] +=1
            if flash_status[row+1][column] == 0:
                input[row+1][column] +=1
            if flash_status[row][column-1] == 0:
                input[row][column-1] +=1
            if flash_status[row-1][column-1] == 0:
                input[row-1][column-1] +=1
            if flash_status[row+1][column-1] == 0:
                input[row+1][column-1] +=1
            #done
    if row == 0:
        #done
            if flash_status[row][column-1] == 0:
                input[row][column-1] +=1
            if flash_status[row][column+1] == 0:
                input[row][column+1] +=1
            if flash_status[row+1][column] == 0:
                input[row+1][column] +=1
            if flash_status[row+1][column-1] == 0:
                input[row+1][column-1] +=1
            if flash_status[row+1][column+1] == 0:
                input[row+1][column+1] +=1
        #done

    if row == len(input):
                #done

            if flash_status[row][column-1] == 0:
                input[row][column-1] +=1
            if flash_status[row][column+1] == 0:
                input[row][column+1] +=1
            if flash_status[row-1][column] == 0:
                input[row-1][column] +=1
            if flash_status[row-1][column-1] == 0:
                input[row-1][column-1] +=1
            if flash_status[row-1][column+1] == 0:
                input[row-1][column+1] +=1
        #done
       
with open("D:/day11.txt") as file:
    input = file.readlines()
input = [x.strip() for x in input]

input2 = np.zeros((len(input[0]),len(input)))
for i in range(0,len(input)):
    for j in range (0, len(input[0])):
        input2[i][j] = input[i][j]

input = input2
flash_status = np.zeros((len(input),len(input)))
MAX_STEPS = 2

print("Before any steps:")
print(input)

for steps in range(0,MAX_STEPS):
    for row in range(0,len(input)):
        for column in range(0,len(input[0])):
            if( input[row][column] <9 ):
                input[row][column] +=1
    check_dumbo_flash(input)
    do_flash_dumbo(input)
    print("after",steps+1,"steps")
    print(input)
