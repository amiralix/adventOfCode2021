
import node
import itertools
import numpy as np

with open("D:/day12.txt") as file:
    input = file.readlines()
input = [x.strip() for x in input]
input = [x.split("-") for x in input]

graph = [[0]*5]*7
for i in range(0,len(input)):
    if  input[i][0] not in graph[:][0] :
        graph[i][0] = str(input[i][0])
        graph[i][1] = str(input[i][1])
        continue
    else :
        index = graph[:][0].index(input[i][0])
        for column in range(0,len(graph[index])):
            if graph[index][column] == 0:
                    graph[index][column] = input[i][1]
                    break
print(graph)