<<<<<<< HEAD
# import time 
# import numpy as np
import collections as collection
# timers = collection.deque([3,4,3,1,2])

timers = collection.deque([4,1,1,4,1,1,1,1,1,1,1,1,3,4,1,1,1,3,1,3,1,1,1,1,1,1,1,1,1,3,1,3,1,1,1,5,1,2,1,1,5,3,4,2,1,1,4,1,1,5,1,1,5,5,1,1,5,2,1,4,1,2,1,4,5,4,1,1,1,1,3,1,1,1,4,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,1,2,1,1,1,1,1,1,1,2,4,4,1,1,3,1,3,2,4,3,1,1,1,1,1,2,1,1,1,1,2,5,1,1,1,1,2,1,1,1,1,1,1,1,2,1,1,4,1,5,1,3,1,1,1,1,1,5,1,1,1,3,1,2,1,2,1,3,4,5,1,1,1,1,1,1,5,1,1,1,1,1,1,1,1,3,1,1,3,1,1,4,1,1,1,1,1,2,1,1,1,1,3,2,1,1,1,4,2,1,1,1,4,1,1,2,3,1,4,1,5,1,1,1,2,1,5,3,3,3,1,5,3,1,1,1,1,1,1,1,1,4,5,3,1,1,5,1,1,1,4,1,1,5,1,2,3,4,2,1,5,2,1,2,5,1,1,1,1,4,1,2,1,1,1,2,5,1,1,5,1,1,1,3,2,4,1,3,1,1,2,1,5,1,3,4,4,2,2,1,1,1,1,5,1,5,2])
# start = time.time()
print("Initial state  " , timers)
for days in range(1,256):
    # timers2 = []
    # zero_indices =  list(np.where( timers == 0 ))[0]
    # non_zero_indices = list(np.nonzero(timers))[0]
    # timers[non_zero_indices] = timers[non_zero_indices] -1 
    # timers[zero_indices] = 6
    # timers2 = np.insert(timers,len(timers), [8] * len(zero_indices))
    # timers = timers2
    # zero_indices = []
    # non_zero_indices = []
    # print("After ",days," day: ",timers)            
    # zero_indices = []
    # non_zero_indices = []

    # for items in range(0,len(timers)):
    #     if(timers[items] == 0):
    #         zero_indices.append(items)
    #     else:
    #         non_zero_indices.append(items)
    
    for iterator in range(0,len(timers)):
        if(timers[iterator]  != 0):
            timers[iterator] = timers[iterator]  -1 
        else:
            timers[iterator] = 6
            timers.extend([8])
    # for t in range(0,len(non_zero_indices)):
    #     timers[non_zero_indices[t]] = timers[non_zero_indices[t]] -1 
    # for k in range(0,len(zero_indices)):
    #     timers[zero_indices[k]] = 6
    # timers.extend([8] * len(zero_indices))
    # zero_indices =  list(np.where( timers2 == 0 ))[0]
    # non_zero_indices = list(np.nonzero(timers2))[0]
    # timers2[non_zero_indices] = timers2[non_zero_indices] -1 
    # timers2[zero_indices] = 6
    # timers = collection.deque(timers2)
    # timers.extend([8] * len(zero_indices))
    # del timers2
    # del zero_indices
    # del non_zero_indices
    print("After ",days," day: ")            
print(len(timers))
# print("elapsed time is " %(time.time()-start))


=======
# import numpy as np
# timers = [4,1,1,4,1,1,1,1,1,1,1,1,3,4,1,1,1,3,1,3,1,1,1,1,1,1,1,1,1,3,1,3,1,1,1,5,1,2,1,1,5,3,4,2,1,1,4,1,1,5,1,1,5,5,1,1,5,2,1,4,1,2,1,4,5,4,1,1,1,1,3,1,1,1,4,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,1,2,1,1,1,1,1,1,1,2,4,4,1,1,3,1,3,2,4,3,1,1,1,1,1,2,1,1,1,1,2,5,1,1,1,1,2,1,1,1,1,1,1,1,2,1,1,4,1,5,1,3,1,1,1,1,1,5,1,1,1,3,1,2,1,2,1,3,4,5,1,1,1,1,1,1,5,1,1,1,1,1,1,1,1,3,1,1,3,1,1,4,1,1,1,1,1,2,1,1,1,1,3,2,1,1,1,4,2,1,1,1,4,1,1,2,3,1,4,1,5,1,1,1,2,1,5,3,3,3,1,5,3,1,1,1,1,1,1,1,1,4,5,3,1,1,5,1,1,1,4,1,1,5,1,2,3,4,2,1,5,2,1,2,5,1,1,1,1,4,1,2,1,1,1,2,5,1,1,5,1,1,1,3,2,4,1,3,1,1,2,1,5,1,3,4,4,2,2,1,1,1,1,5,1,5,2]
# timers = np.array(timers)
# print("Initial state  " , timers)
# for days in range(1,257):
#     zero_indices = list(np.where( timers == 0 ))[0]
#     non_zero_indices = list(np.nonzero(timers))[0]
#     timers[non_zero_indices] = timers[non_zero_indices] -1 
#     timers[zero_indices] = 6
#     timers = np.insert(timers,len(timers), [8] * len(zero_indices))
#     print("After ",days," day: ",timers)            
# print(len(timers))



with open("D:/day6.txt") as file:
    input = file.readlines()

input = [x.strip() for x in input]
input = input[0].split(",")
my_dict = []
DAYS = 19

for days in range(0,DAYS):
    for i in range(0,len(input)):
        input[i] = int(input[i]) 
        input[i] -= 1
        if input[i] == -1:
            input[i] = 6
            my_dict.append(9)
    if len(my_dict) != 0:
        for j in range(0,len(my_dict)):
            my_dict[j] -= 1
            if( my_dict[j] == -1):
                my_dict.append(9)
                input.append(6)
                del my_dict[j]
print("After ",days," day: ",input,my_dict)            
>>>>>>> 320f09b610e0335d36d6322ce1c0abe0eb67b1dc
