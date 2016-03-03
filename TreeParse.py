import json
import re
import ast


with open("COG0001.aligned.jplace") as json_data:

    data = json.load(json_data)

    ##json parse--extract tree string
    tree = data['tree']
    #each edge is numbered by {x}, split each
    edges = tree.split('{')
    for edge in edges:
        if '}' in edges:
            edges += 1

    branches = re.split('[, ( )]' , tree)

    #initialize edgeCount at -1 because the root is indicated by a {x} but we dont want to count that in the edgeCount variable
    edgeCount = -1
    leafCount = 0
    #initialize list to place all leaf edge numbers
    leafEdges = []
    internalEdges = []

    # i is integer index of each element in list
    # v is value (string) at each index
    for i,v in enumerate(branches):
        if '{' in v:
            edgeCount += 1
        if "|" in v:
            leafCount += 1
            edgeNum = int(v.split('{')[1].split('}')[0])
            leafEdges.append(edgeNum)
        elif v != '':
            internal_edgeNum = int(v.split('{')[1].split('}')[0])
            internalEdges.append(internal_edgeNum)

    print "Leaf count " + str(leafCount)
    print "Edge count " + str(edgeCount)
    print branches[0:50]
    print leafEdges[0:10]
