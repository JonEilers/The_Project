import json

class _JplaceRecordComponent(object):
    """Component of a JplaceRecord."""

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
      '''dictionary contains newick tree information3'''
        self._tree = {}
        
    def __str__(self):
        return self._content
        
    def __node__(self, nodes = total):
        """standalone function. returns number of internal, external, and total nodes. Should it be nodes or edges?"""
        
    def __branch__(self, initial_node = 0, leaf = none):
        '''calculates the branch length given the starting node and ending node. default ending node is none, 
        this finds the longest branch length and returns it.'''

    def _content(self):
        """Return the newick tree as a dictionary with key as node and values as everything else?.
        
        :returns: dict
        """
        
    def add_tree_edge(self, tree_node):
        """
        Adds node/edge and its info to the JplaceTree instance. This function can
        be called more than once. Each time the function is called the :class: tinyjplace.NewickTree
        dictionary is extended by the key/value pair provided.
        :param tree_node: dict key/value representing part of a newick formatted tree.
        """
        
    def format_line_length(self, node_data):
        """iterates over the newick tree found in the jplace file, extracts a single node and formats it as 
        a key/value dictionary pair. Each key contains information connecting it to distal and proximal nodes. 
        These are used when writing out the
        :class: tinyjplace.JplaceRecord over several nodes.
        
        :param node_data: information specific to that node.
        """ 
    
class JplaceRecord(object):
    '''A class representing phylogenetic tree placement'''
    
class JplaceParser(object):
    '''Class for parsing Jplace files'''