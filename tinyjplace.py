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
        
    @property
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
    
class PlacementRecord(object):
    '''A class representing phylogenetic tree placements'''
    
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
        
        
    @staticmethod
    def create(tree, placements):
        """Return a PlacementRecord.
        
        :param tree: description string
        :param placements: full sequence string
        :returns: :class:`tinyjplace.PlacementRecord`
        """
        
    def __init__(self, placement_fields):
        """Initialise an instance of the :class:`tinyjplace.Placement_Fields` class.
        
        :param placement_field: list
        """
       
        
    def placement_add(self, field_value):
        '''adds placement to tinyjplace.JplaceRecord instance.
        
        This function can be called more than once. Each time the function is
        called the :attr:`tinyjplace.placement` is extended by the placement
        provided.
        :param placement: dictionary containing placement info
        '''
        
class JplaceParser(object):
    '''Class for parsing Jplace files'''
    
    def __init__(self, filepath):
        '''initialize an instance of the JplaceParser.
        
        :param filepath: path to the Jplace file to be parsed
        '''
        
    def __iter__(self):
        '''Yield PlacementRecord instance.'''
