'''
Created on 03-Oct-2014

@author: niloygupta sandeeprao
'''

edgeList = {1:[2,3,4], 2:[1,3,5,7], 3:[2,4,3], 4:[1,2,3,7], 5:[2,7], 6:[2,5], 7:[4]}
#edgeList = {1:[2,3,7], 2:[1,3,7], 3:[1,7,2,4,5], 4:[3,5,6], 5:[3,4,6], 6:[4,5], 7:[1,2,3]}
degreeList = {}
core = {}

for key, value in edgeList.iteritems():
    degreeList[key] = len(value)

sorted_degreeList = degreeList.copy()

for i in range(len(edgeList)):
    node = min(sorted_degreeList, key = lambda x: sorted_degreeList.get(x) )
    core[node] = degreeList[node];
    del sorted_degreeList[node]
    for neighbour in edgeList[node]:
        if(degreeList[neighbour] > degreeList[node]):
            sorted_degreeList[neighbour] = sorted_degreeList[neighbour] - 1
            degreeList[neighbour] = degreeList[neighbour] - 1

print core