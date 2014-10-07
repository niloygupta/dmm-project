'''
Created on 03-Oct-2014

@author: niloygupta sandeeprao
'''

#edgeList = {1:[2,3,4], 2:[1,3,5,7], 3:[2,4,3], 4:[1,2,3,7], 5:[2,7], 6:[2,5], 7:[4]}
edgeList = {1:[2,3,7], 2:[1,3,7], 3:[1,7,2,4,5], 4:[3,5,6], 5:[3,4,6], 6:[4,5], 7:[1,2,3]}
deg = {}
core = {}
md = -1
bins = []
pos = []
vert = []
n = len(edgeList)



for key, value in edgeList.iteritems():
    deg[key] = len(value)
    if len(value) > md:
        md = len(value)


for d in range(md+1):
    bins.insert(d,0)

pos.insert(0,0)
vert.insert(0,0)
for v in range(1,n+1):
    bins[deg[v]] = bins[deg[v]] + 1
    pos.insert(d,0)
    vert.insert(d,-1)


start = 1

for d in range(md+1):
    num = bins[d]
    bins[d] = start
    start = num +start

for v in range(1,n+1):
    pos[v] = bins[deg[v]]
    vert[pos[v]] = v
    bins[deg[v]] = bins[deg[v]] + 1 

for d in reversed(range(1,md+1)):
    bins[d] = bins[d-1] 

bins[0] = 1

print vert
for i in range(1,n+1):
    v = vert[i]
    print "I:",i
    print "V:",v
    for u in edgeList[v]:
        print "U:",u
        if deg[u] > deg[v]:
            du = deg[u]
            pu = pos[u]
            pw = bins[du]
            w = vert[pw]
            if u!=w:
                pos[u] = pw
                vert[pu] = w
                pos[w] = pu
                vert[pw] = u
            bins[du] = bins[du] + 1
            deg[u] = deg[u] -1 
print deg   

"""
sorted_degreeList = deg.copy()

for i in range(len(edgeList)):
    node = min(sorted_degreeList, key = lambda x: sorted_degreeList.get(x) )
    core[node] = deg[node];
    del sorted_degreeList[node]
    for neighbour in edgeList[node]:
        if(deg[neighbour] > deg[node]):
            sorted_degreeList[neighbour] = sorted_degreeList[neighbour] - 1
            deg[neighbour] = deg[neighbour] - 1

print core"""