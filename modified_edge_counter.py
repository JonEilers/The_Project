import json
import re


internal_count = 0
external_count = 0


with open("COG0001.aligned.jplace") as json_data:

    data = json.load(json_data)

    ##json parse--extract tree string
    tree = data['tree']

    branches = re.split('[, ( )]' , tree)##splitting at ')' '(' and ',' eliminates all delimiters that are not curly braces--
        # leaves either empty elements ex: u'' or elements withedge numbers/labels/lengths in each element of the list

    #initialize totalEdgeCount at -1 because the root is indicated by a {x} but we dont want to count that in the edgeCount variable
    totalEdgeCount = -1
    leafCount = 0
    #initialize lists to place leaf and internal edge numbers
    leafEdges = []
    internalEdges = []

    # i is integer index of each element in list
    # v is value (string) at each index
    for i,v in enumerate(branches):
        if '{' in v:
            totalEdgeCount += 1
        if "|" in v:
            leafCount += 1
            edgeNum = int(v.split('{')[1].split('}')[0])
            leafEdges.append(edgeNum)
        elif v != '':
            internal_edgeNum = int(v.split('{')[1].split('}')[0])
            internalEdges.append(internal_edgeNum)

    placements = data['placements'] #placement key in json


    #initialize lists
    leafList = []
    internalList = []
    
    #initialize abundance counts
    num_leaf_placements = 0
    num_internal_placements = 0  

    for i in placements: #it works, but I am guessing there is a more efficient way to dig deep into a dictionary

        placement_edge = i.values()[0][0][2] 
        
        # from what I understand the 'nm' list under 'p' is the sequences assigned to that edge. want to clarify with robin though
        multiplicity = i.values()[1]
        
        #by logic above, the length of the nm list would be the number of short-read sequences associated with that pquery
        numReads = len(multiplicity)
        
        #named small list b/c we are placing it into a larger list (internalList or leafList, initialized above)
        smallList = [placement_edge , numReads]
        if placement_edge in internalEdges:
            internalList.append(smallList)
            internal_count += 1
            num_internal_placements += numReads
        elif placement_edge in leafEdges:
            leafList.append(smallList)
            external_count += 1
            num_leaf_placements += numReads
    print(internal_count)
    print(external_count)
    
    #sort [edge,seqNum] lists from lowest to highest edge number
    leafList.sort(key=lambda x: x[0])
    internalList.sort(key=lambda x: x[0])
    print(leafList)
    print(internalList)
    
    
    #goals:
      #clean up program--implement main(), package loops/elifs into functions
      #combine edge counts--if you look in sorted lists when it prints out there are multiple pqueries for the same edge
        #check with robin about 'nm' and what it actually means--jplace file description says it could be a modified counter that likely doesnt reflect the absolute number of sequences
      #ask robin about the placement of the edge element--do all klab jplace files have the edge number in that specific position
      #write to file
        #header containing total # of edges, # internal, # leaf, internal:leaf ratio
        #some kind of delimited format to display the specific edge counts
   
