import json
import re

with open("COG0001.aligned.jplace") as json_data:

    data = json.load(json_data)

    ##json parse
    nodeNum = 0
    tree = data['tree']
    edges = tree.split('{')
    for edge in edges:
        if '}' in edges:
            edges += 1

    branches = re.split('[, ( )]' , tree)
    arbLen = 50
    #smallBranches = branches[0:arbLen]

    leafCount = 0
    edgeTotal = 0
    for i in branches:
      # # if len(i) == 0:
        #    del branches[i]
        if "|" in i:
            leafCount+=1


    #Node(tree)

    print leafCount
    print nodeNum - 1
    #print branches[0:arbLen]
    
