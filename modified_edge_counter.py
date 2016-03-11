import json
import re

internal_count = 0
external_count = 0


with open("COG0002.aligned.jplace") as json_data:

    data = json.load(json_data)

    ##json parse--extract tree string
    tree = data['tree']

    branches = re.split('[, ( )]' , tree)##splitting at ')' '(' and ',' eliminates all delimiters that are not curly braces--
        # leaves either empty elements ex: u'' or elements withedge numbers/labels/lengths in each element of the list

    #initialize totalEdgeCount at -1 because the root is indicated by a {x} but we dont want to count that in the edgeCount variable
    totalEdgeCount = -1
    leafCount = 0
    internalCount = 0
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
            leaf_edgeNum = int(v.split('{')[1].split('}')[0])
            leafEdges.append(leaf_edgeNum)
        elif v != '':
            internal_edgeNum = int(v.split('{')[1].split('}')[0])
            internalCount += 1
            internalEdges.append(internal_edgeNum)

    placements = data['placements'] #placement key in json


    #initialize lists
    leafList = []
    internalList = []
    total_placements = 0
    # there are i pquery elements in the 'placements list--for loop iterates through each pquery--basically placements[i]
        #each pquery consists of a unicode list of placements (u'p') and short-read names (u'nm')
    for i in placements: #it works, but I am guessing there is a more efficient way to dig deep into a dictionary

        #verify total number of placements in the file
        total_placements += 1
        #i.values() retrieves the values (p and nm) of the unicode list (u'p', u'nm')
        #indeces: [0][0][2]
            #first [0]: retrieves pquery placements (p) from the [p , nm] list at index i
            #second [0]: retrieves the first element in the list of potential placements (p) at index i
                #the first placement listed has the highest posterior probability (this element contains the placement edge)
            #[2]: the highest probability placement edge is the 3rd element in the placement information
        placement_edge = i.values()[0][0][2]

        #multiplicity is number of reads placed at that edge
        multiplicity = i.values()[1]
        numReads = len(multiplicity)

        #check placement edge number against internal edge list
        if placement_edge in internalEdges:
            internal_count += 1
            smallList = [placement_edge , numReads]
            internalList.append(smallList)
        #check placement edge number against leaf edge list
        elif placement_edge in leafEdges:
            external_count += 1
            smallList = [placement_edge , numReads]
            leafList.append(smallList)

    #combine list elements
    leafList.sort(key=lambda x: x[0])
    internalList.sort(key=lambda x: x[0])

    leafList.sort(key=lambda x: x[0])
    #l.sort(key=lambda x: x[2])
    internalList.sort(key=lambda x: x[0])

    print leafList
    print internalList
    
    
    #goals:
      #clean up program--implement main(), package loops/elifs into functions
      #combine edge counts--if you look in sorted lists when it prints out there are multiple pqueries for the same edge
        #check with robin about 'nm' and what it actually means--jplace file description says it could be a modified counter that likely doesnt reflect the absolute number of sequences
      #ask robin about the placement of the edge element--do all klab jplace files have the edge number in that specific position
      #write to file
        #header containing total # of edges, # internal, # leaf, internal:leaf ratio
        #some kind of delimited format to display the specific edge counts
   
