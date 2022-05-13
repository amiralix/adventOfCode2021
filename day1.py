
with open("D:/input1.txt") as file:
    lines= file.readlines()
lines = [l.strip() for l in lines]
print(lines)
# lines = [199,200,208,210,200,207,240,269,260,263]

num_increase = 0
for i in range(len(lines)-1):
    if int(lines[i+1]) > int(lines[i]):
        print(lines[i] , lines[i+1] , "increased" , num_increase)
        num_increase +=1
    else:
            print(lines[i] , lines[i+1] , "decreased")

print(num_increase)