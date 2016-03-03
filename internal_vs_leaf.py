import json
import re
import ast

internal_count = 0
external_count = 0


with open("COG0001.aligned.jplace") as json_data:

    data = json.load(json_data)

    ##json parse--extract tree string
    tree = data['tree']
    branches = re.split('[, ( )]' , tree)

    #initialize edgeCount at -1 because the root is indicated by a {x} but we dont want to count that in the edgeCount variable
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

    placements = jplace_handle['placements'] #placement key in json
    for placement in placements: #it works, but I am guessing there is a more efficient way to dig deep into a dictionary
        placement_edge = placement.values()[0][0][2]
        if placement_edge in internalEdges:
            internal_count += 1
        elif placement_edge in leafEdges:
            external_count += 1
    print(internal_count)
    print(external_count)
