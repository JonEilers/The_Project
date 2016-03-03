import json
import re

with open("COG0001.aligned.jplace") as json_data:

    data = json.load(json_data)
    tree = data['tree']
    branches = tree.split(",")
    for i in branches:
        if "|" in i:
            internalCount+=1
    print len(branches)

internal_count = 0
external_count = 0
    jplace_handle = json.load(jplace_file)
    placements = jplace_handle['placements'] #placement key in json
    for placement in placements: #it works, but I am guessing there is a more efficient way to dig deep into a dictionary
        placement_edge = placement.values()[0][0][2]
        if placement_edge in test_internal
            internal_count += 1
        elif placement_edge in test_external:
            external_count += 1
    print(internal_count)
    print(external_count)
