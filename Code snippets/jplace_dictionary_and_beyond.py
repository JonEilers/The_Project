import json

# Found this to be interesting. python.json loads the jplace file as a dictionary. 
# There are four keys: version, trees, metadata, and placements.

"""
class jplace(object):
    '''A class for accessing the parts of a jplace file'''
    def __init__(self, metadata, version, placements, tree, fields):
        self.metadata = metadata
        self.version = version
        self.placements = placements
        self.tree = tree
        self.fields = fields


"""

def jplace(file_jplace):
    with open(file_jplace) as data:
        jplace_handle = json.load(data)
        print jplace_handle.keys()
 #       print jplace_handle['metadata']
 #       print jplace_handle['tree']
 #       print jplace_handle['placements']

 
 #       placements = jplace_handle['placements']
 #       print placements[1]  #Or more, it will print each subsequent 'p' (placement and info) 

#        tree = jplace_handle['tree']
#        print tree[1:5]


        first_placement = placements[0]
  #      print first_placement
  #      print first_placement.keys()
  #      print first_placement.values()
  
        fp_internal = first_placement.values()
  #      print fp_internal.values()
  
  
        fp_place = fp_internal[0]
        print fp_place[0]

