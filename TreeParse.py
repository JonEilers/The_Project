#Author : Shelby Landa
#Project : BIOL497 Final Project
#File name : TreeParse.py
#Date :

import json

with open("COG0001.aligned.jplace") as json_data:

    data = json.load(json_data)
    tree = data['tree']
    branches = tree.split(",")
    internalCount = 0
    for i in branches:
        if "|" in i:
            internalCount+=1
    print len(branches)



##unicode strings??
