import numpy as np
timers = [3,4,3,0,2]
timers = np.array(timers)

print("Initial state" , timers)
for days in range(1,19):
    non_zero_indices = list(np.nonzero(timers))[0]
    timers[non_zero_indices] = timers[non_zero_indices] -1 
    zero_indices = list(np.where( timers == 0 ))[0]
    timers[zero_indices] = 6
    for i in range(len(zero_indices)):
        np.append(timers,8)
    print("After ",days," day: ",timers)            
print(len(timers))
