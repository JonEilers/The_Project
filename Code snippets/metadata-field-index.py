'''
This is a function to determine the edge placement number index in jplace file metadata
'''

    edge_index = 0
    counter = -1
    fields_handle = data['fields']
    for i in fields_handle:
        counter += 1
        if i == 'edge_num':
            edge_index = counter
