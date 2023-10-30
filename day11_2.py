import numpy as np


def update_adjacents(input,row,column):
    if ( row == 0 ):
        if (column == 0):
        #done
            if flash_status[row][column+1] != 1:
                input[row][column+1] +=1
            if flash_status[row+1][column] != 1:
                input[row+1][column] +=1
            if flash_status[row+1][column+1] != 1:
                input[row+1][column+1] +=1
            #done
        if (column == len(input) -1 ):
            #done
            if flash_status[row][column-1] != 1:
                input[row][column-1] +=1
            if flash_status[row+1][column] != 1:
                input[row+1][column] +=1
            if flash_status[row+1][column-1] != 1:
                input[row+1][column-1] +=1
            #done
    if (row == len(input) -1 ):
        if( column == 0) :
            #done
            if flash_status[row-1][column] != 1:
                input[row-1][column] +=1
            if flash_status[row-1][column+1] != 1:
                input[row-1][column+1] +=1
            if flash_status[row][column+1] != 1:
                input[row][column+1] +=1
            #done
        if (column == len(input) -1 ):
            #done
            if flash_status[row][column-1] != 1:
                input[row][column-1] +=1
            if flash_status[row-1][column] != 1:
                input[row-1][column] +=1
            if flash_status[row-1][column-1] != 1:
                input[row-1][column-1] +=1
            #done
# check for row not to be 0 or max
    if ( 0 < row < len(input) -1 ):
        if (  0 < column < len(input[0]) -1 ):
        #done
            if flash_status[row][column-1] == 0 :
                input[row][column-1] +=1
            if flash_status[row-1][column-1] == 0 :
                input[row-1][column-1] +=1
            if flash_status[row-1][column] == 0 :
                input[row-1][column] +=1
            if flash_status[row-1][column+1] == 0 :
                input[row-1][column+1] +=1
            if flash_status[row][column+1] == 0 :
                input[row][column+1] +=1
            if flash_status[row+1][column+1] == 0:
                input[row+1][column+1] +=1
            if flash_status[row+1][column] == 0:
                input[row+1][column] +=1
            if flash_status[row+1][column-1] == 0 :
                input[row+1][column-1] +=1
        #done
        if column == 0:
            #done
            if flash_status[row-1][column] != 1:
                input[row-1][column] +=1
            if flash_status[row+1][column] != 1:
                input[row+1][column] +=1
            if flash_status[row][column+1] != 1:
                input[row][column+1] +=1
            if flash_status[row-1][column+1] != 1:
                input[row-1][column+1] +=1
            if flash_status[row+1][column+1] != 1:
                input[row+1][column+1] +=1
            #done
        if column == len(input[0]) -1 :
            #done
            if flash_status[row-1][column] != 1:
                input[row-1][column] +=1
            if flash_status[row+1][column] != 1:
                input[row+1][column] +=1
            if flash_status[row][column-1] != 1:
                input[row][column-1] +=1
            if flash_status[row-1][column-1] != 1:
                input[row-1][column-1] +=1
            if flash_status[row+1][column-1] != 1:
                input[row+1][column-1] +=1
            #done
    if (  0 < column < len(input[0]) -1 ):
        if row == 0 :
            #done
                if flash_status[row][column-1] != 1:
                    input[row][column-1] +=1
                if flash_status[row][column+1] != 1:
                    input[row][column+1] +=1
                if flash_status[row+1][column] != 1:
                    input[row+1][column] +=1
                if flash_status[row+1][column-1] != 1:
                    input[row+1][column-1] +=1
                if flash_status[row+1][column+1] != 1:
                    input[row+1][column+1] +=1
            #done
        if row == len(input) -1 :
                    #done
                if flash_status[row][column-1] != 1:
                    input[row][column-1] +=1
                if flash_status[row][column+1] != 1:
                    input[row][column+1] +=1
                if flash_status[row-1][column] != 1:
                    input[row-1][column] +=1
                if flash_status[row-1][column-1] != 1:
                    input[row-1][column-1] +=1
                if flash_status[row-1][column+1] != 1:
                    input[row-1][column+1] +=1
            #done
    for i in range(0,len(input)):
        for j in range (0, len(input[0])):
            if input[i][j] > 9 and flash_status[i][j] == 0 :
                flash_status[i][j] = 1
       
def find_one(input):
    for i in range(0,len(input)):
        for j in range (0, len(input[0])):
            if input[i][j] == 1 :
                return i,j

with open("D:/day11.txt") as file:
    energy = file.readlines()
energy = [x.strip() for x in energy]

input2 = np.zeros((len(energy[0]),len(energy)))
for i in range(0,len(energy)):
    for j in range (0, len(energy[0])):
        input2[i][j] = energy[i][j]

energy = input2
flash_status = np.zeros((len(energy),len(energy[0])))
MAX_STEPS = 2000

print("Before any steps:")
print(energy)
flash_number = 0
test_for_all_zero = np.zeros((len(energy),len(energy[0])))

for steps in range(0,MAX_STEPS):
    flash_status = np.zeros((len(energy),len(energy[0])))
    for row in range(0,len(energy)):
        for column in range(0,len(energy[0])):
            energy[row][column] +=1
            if( energy[row][column] > 9):
                flash_status[row][column] = 1
    while (1 in flash_status):
        to_be_updated_row,to_be_updated_cloumn = find_one(flash_status)
        update_adjacents(energy,to_be_updated_row,to_be_updated_cloumn)
        flash_status[to_be_updated_row][to_be_updated_cloumn] = 2
    for i in range(0,len(energy)):
        for j in range (0, len(energy[0])):
            if flash_status[i][j] == 2:
                energy[i][j] = 0
                flash_number += 1    
    if (False not in (energy == test_for_all_zero)) :
        print(steps+1)
        print(energy)
        break
    print("after","steps",steps+1)
    print(energy)
    # print(flash_number)
