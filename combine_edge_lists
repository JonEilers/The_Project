##Code to combine edge and number of sequences into one element in the edge list

    #We dont need this first part if we just make the list of edges with placements on the fly in the placement_edge counter function thing
    updatedLeafList = [] #this will be a list of all edges that have placed reads
    for i in range(len(leafList)):
        for j in range(len(leafList[i])-1):
            if leafList[i][j] not in updatedLeafList:
                updatedLeafList.append(leafList[i][j])
    print updatedLeafList
    
  
    ###This is the code for actually combining elements
    newLeafList = [] #this will essentially be an array of [[edge_a, numSequences],[edge_b, numSequences]...etc] without repeating edge numbers
    
    for i in range(len(leafsWithPlacement)):
        counter = 0 #keeps running tally of sequences placed at edge (leafsWithPlacements[i])
        tempEdgeNum = 0
        for j in range(len(leafList)):
            if (leafList[j][0] == leafsWithPlacement[i]):# when the first element in leafList[j] equals the element in the list of edges with placements
                tempEdgeNum = leafsWithPlacement[i]
                counter += leafList[j][1]
        pair_edgeSeq = [tempEdgeNum, counter]
        newLeafList.append(pair_edgeSeq)
    newLeafList.sort(key=lambda x: x[0]) #sort new list numerically by edge number

    print newLeafList

    newInternalList = [] #this will essentially be an array of [[edge_a, numSequences],[edge_b, numSequences]...etc] without repeating edge numbers

    for i in range(len(internalWithPlacement)):
        counter = 0 #keeps running tally of sequences placed at edge (leafsWithPlacements[i])
        tempEdgeNum = 0
        for j in range(len(internalList)):
            if (internalList[j][0] == internalWithPlacement[i]):# when the first element in leafList[j] equals the element in the list of edges with placements
                tempEdgeNum = internalWithPlacement[i]
                counter += internalList[j][1]
        pair_edgeSeq = [tempEdgeNum, counter]
        newInternalList.append(pair_edgeSeq)
    newInternalList.sort(key=lambda x: x[0]) #sort new list numerically by edge number

    print newInternalList
