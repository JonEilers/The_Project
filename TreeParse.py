#Author : Shelby Landa
#Project : BIOL497 Final Project
#File name : TreeParse.py
#Date :

import json
import re

with open("COG0001.aligned.jplace") as json_data:

    data = json.load(json_data)
    tree = data['tree']
    branches = re.split('[, ( )]' , tree)
    
    #arbitrary length to test ability of loops to do the right thing
    arbLen = 50
    #small subsect of larger tree
    smallBranches = branches[0:arbLen]
    
    #initialize leafCount variable 
    leafCount = 0
    
    # | is only present in tip labels
    for i in smallBranches:
       # if len(i) == 0:
        #    del branches[i]
        if "|" in i:
            #increment leafCount by 1
            leafCount+=1
    #does leafCount work with smallBranches length??
    print leafCount
    #check branches with leafCount
    print branches[0:arbLen]
    
