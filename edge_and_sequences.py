'''
This is a function that takes an edge number and all sequences IDs placed on that edge. This is stored as a dictionary with keys as edge number
and values as a list of sequence IDs.

This data structure will work for the basics. But if we want to include other information such as level of taxonomy classification,
then it may not be the best approach.

This is psuedocode. I haven't tried to making it functional. 
'''

def create_edge_dict(jplace_file?):
  edge_sequence = {}
  for p in data.placements:
    placement_edge = p[0][0][index_value_for_edge_number]
    if placement_edge in edge_sequence.keys:
      edge_sequence.value[placement_edge].append(p.nm)
    else:
      edge_sequence[placement_edge] = [p.nm]
      
    
      
      
'''     
This is something I found on the web after I wrote the code above. 

  # say we're building a word->pagenumbers index -- a key piece of code might be:

theIndex = {}
def addword(word, pagenumber):
    if theIndex.has_key(word):
        theIndex[word].append(pagenumber)
    else:
        theIndex[word] = [pagenumber]

# incidentally, a good Pythonic instinct would be to substitute this
# "look before you leap" pattern with a "easier to get permission":

def addword(word, pagenumber):
    try: theIndex[word].append(pagenumber)
    except AttributeError: theIndex[word] = [pagenumber]

# but this is by the by -- just a minor simplification.  However,
# this meets the pattern "use the entry if already present, else
# add a new entry".  Here's how using setdefault simplifies this:

def addword(word, pagenumber):
    theIndex.setdefault(word,[]).append(pagenumber)
'''
