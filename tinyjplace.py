"""Package for parsing and generating Jplace files for phylogenetic tree analysis.
Use the :class:`tinyjplace.JplaceParser` class to parse Jplace files. 
"""

import json

class _JplaceRecordComponent(object):
    """Component of a PlacementRecord."""

    def contains(self, search_term):
        """Return True if the component contains the search term.
        
        :param search_term: string or compiled regular expression to search for
        :returns: bool
        """
        if hasattr(search_term, "search"):
            return search_term.search(self._content) is not None
        return self._content.find(search_term) != -1

class NewickTree(_JplaceRecordComponent):
    '''A class representing a phylogenetic tree'''
    
    def __init__(self):
        self._tree = {}
        
    def __str__(self):
        return self._content
        
    @property #what does this decorator do? is it a built in python function?
    def _content(self):
        """Return the newick tree as a dictionary with key as node and values as everything else?.
        
        :returns: dict
        """
        
    def add_tree_edge(self, tree_edge):
        """
        Add an edge to the :class: tinyjplace.NewickTree instance.
        
        Adds edge and its info to the JplaceTree instance. This function can
        be called more than once. Each time the function is called the :class: tinyjplace.NewickTree
        dictionary is extended by the edge key/value pair provided.
        
        :param tree_edge: dict key/value representing part of a newick formatted tree.
        """
        
        self._sequences.append( sequence_line.strip() ) #needs to be a bit more complicated then this. 
        
    def format_tree_edge(self, edge_data):
        """Takes a tree edge and formats it as a key/value dictionary pair.
        The value contains information connecting it to distal and proximal nodes. 
        
        :class: tinyjplace.JplaceRecord over several edges.
        
        :param edge_data: information specific to that edge.
        """ 
        
        def __branch_length__(self, initial_edge = 0, leaf = none):
        '''calculates the branch length given the starting edge and ending edge. default ending edge is none, 
        this finds the longest branch length and returns it.
        
        :param initial_edge: first edge
               leaf: last edge '''
    
    def internal_edge(self):
        '''parses a Newick tree
        
        returns: all the internal edges stores it as a dictionary. 
        
        key: edge number
        values: edges or nodes it is connected to
        '''
        
    def leaf(self):
        '''parses a Newick tree and returns all leaf
        returns: dictionary
        
        key: edge number
        values: edge or node it is connected to
        '''
    
class JplaceRecord(object):
    '''A class representing a Jplace record'''
    
    class SequenceID(self, _JplaceRecordComponent):
        '''Takes the Sequence IDs associated with n/nm key in a placement dictionary'''
        
        #what functions need to go here?
        
          def __init__(self, sequenceID):
            self.update(sequenceID)
    
    class Placement_Fields(self, _JplaceRecordComponent):
        '''Takes the list associated with the field key in a placement dictionary'''
        
        #what functions need to go here?
        def __init__(self, placement_dictionary):
            self.update(placement_dictionary)
        
    def jplace_placement_fields(self):
        '''checks jplace file metadata for presence of fields. 
        
        returns: field name and list index number.'''
        
    def field_contains(self, field_name):
        '''checks to see if given field is in metadata
        
        returns list index value'''
        
    def placements_containing(self, field_value):
        '''returns all placements containing a specific field value or sequence ID'''
        
'''        
    @staticmethod #what the hell is this?
    def create(tree, placements):
        """Return a PlacementRecord.
        
        :param tree: description string
        :param placements: full sequence string
        :returns: :class:`tinyjplace.PlacementRecord`
        """
'''

    def __init__(self, placement_fields):
        """Initialise an instance of the :class:`tinyjplace.Placement_Fields` class.
        
        :param placement_field: list
        """
       
        
    def add_placement(self, field_value):
        '''adds placement to tinyjplace.JplaceRecord instance.
        
        This function can be called more than once. Each time the function is
        called the :attr:`tinyjplace.placement` is extended by the placement
        provided.
        :param placement: dictionary containing placement info
        '''
        
        self.sequence.add_edge(field_value)
        
class JplaceParser(object):
    '''Class for parsing Jplace files'''
    
    def __init__(self, filepath):
        '''initialize an instance of the JplaceParser.
        
        :param filepath: path to the Jplace file to be parsed
        '''
        
        self.filepath = filepath
        
    def __iter__(self):
        '''Yield JplaceRecord instance.'''
        
        jplace_record = None #nothing to see in this empty objectt
        with open(self.filepath, 'r') as fh:
            file_handle = json.load(fh)
            for key in file_handle: #needs to loop across initial keys in a jplace file (enumerate?)
                if key == 'tree':
                    if jplace_record: 
                        yield jplace_record
                    jplace_record = JplaceRecord(tree) #need to think about this more
                elif key == 'placements':
                    jplace_record.add_placement(placement)
                else:
                 #add the remaining dictionaries to jplace_record instance
        yield jplace_record
'''python.json loads jplace as a dictionary. tinyfasta iterates across each line as a string, checking if it starts with a 'p'. 
if so, then that line is a sequence-discription. if not then it is a sequence or a line break. tinyfasta then does
its thing. In a jplace file, there are four dictionary keys: metadata, fields, tree, placements. Each has a unique 
format. If we want to iterate across the jplace file, we need to specify which key. '''
