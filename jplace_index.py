'''
This is a function to determine the edge placement number index in jplace file metadata
'''

def get_index(field):
  if field in data.metadata:
    index = data.metadata['field']
  else:
    return "Error, that field is not in this file"
