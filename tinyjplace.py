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
      '''dictionary contains newick tree information'''
        self._tree = {}
        
    def __str__(self):
        return self._content
        
    def __branch_length__(self, initial_node = 0, leaf = none):
        '''calculates the branch length given the starting node and ending node. default ending node is none, 
        this finds the longest branch length and returns it.'''
    
    def internal_edge(self):
        '''parses a Newick tree and returns all the internal edges stores it as a dictionary. 
        
        key: edge number
        values: edges or nodes it is connected to
        '''
        
    def leaf((self):
        '''parses a Newick tree and returns all leafs, storing them in a dictionary
        
        key: edge number
        values: edge or node it is connected to
        '''
    
    def _content(self):
        """Return the newick tree as a dictionary with key as node and values as everything else?.
        
        :returns: dict
        """
        
    def add_tree_edge(self, tree_node):
        """
        for parsing a tree and storing desirable values
        
        Adds node/edge and its info to the JplaceTree instance. This function can
        be called more than once. Each time the function is called the :class: tinyjplace.NewickTree
        dictionary is extended by the key/value pair provided.
        :param tree_node: dict key/value representing part of a newick formatted tree.
        """
        
    def format_tree_node(self, node_data):
        """iterates over the newick tree found in the jplace file, extracts a single node and formats it as 
        a key/value dictionary pair. Each key contains information connecting it to distal and proximal nodes. 
        These are used when writing out the
        :class: tinyjplace.JplaceRecord over several nodes.
        
        :param node_data: information specific to that node.
        """ 
    
class PlacementRecord(object):
    '''A class representing phylogenetic tree placements'''
    
    class SequenceID(self, _JplaceRecordComponent):
        '''Takes the Sequence IDs associated with n/nm key in a placement dictionary'''
    
    class Placement_Fields(self, _JplaceRecordComponent):
        '''Takes the list associated with the field key in a placement dictionary'''
        
    def jplace_placement_fields(self):
        '''checks jplace file metadata for presence of fields. 
        
        returns: field name and list index number.'''
        
    def field_contains(self, field_name):
        '''checks to see if given field is in metadata
        
        returns list index value'''
        
    def placements_containing(self, field_value):
        '''returns all placements containing a specific field value or sequence ID'''
        
    def placement_add(self, field_value):
        '''adds placement to tinyjplace.JplaceRecord instance.
        
        This function can be called more than once. Each time the function is
        called the :attr:`tinyjplace.placement` is extended by the placement
        provided.
        :param placement: dictionary containing placement info
        '''
_____________________________________________________________________________________________________________
    @staticmethod
    def create(description, sequence):
        """Return a FastaRecord.
        
        :param description: description string
        :param sequence: full sequence string
        :returns: :class:`tinyfasta.FastaRecord`
        """
        fasta_record = FastaRecord(description)
        fasta_record.add_sequence_line(sequence)
        fasta_record.sequence.format_line_length()
        return fasta_record

    def __init__(self, description):
        """Initialise an instance of the :class:`tinyfasta.FastaRecord` class.
        
        :param description: description string
        """
        self.description = FastaRecord.Description(description)
        self.sequence = Sequence()

    def __str__(self):
        """String representation of the :class:`tinyfasta.FastaRecord` instance."""
        lines = [str(self.description),]
        lines.extend(self.sequence._sequences)
        return '\n'.join(lines)

    def __len__(self):
        """Return the length of the biological sequence."""
        return len(self.sequence)

    def add_sequence_line(self, sequence_line):
        """Add a sequence line to the :class:`tinyfasta.FastaRecord` instance.
        This function can be called more than once. Each time the function is
        called the :attr:`tinyfasta.sequence` is extended by the sequence line
        provided.
        :param sequence_line: string representing (part of) a sequence
        """
        self.sequence.add_sequence_line(sequence_line)
____________________________________________________________________________________________    
class JplaceParser(object):
    '''Class for parsing Jplace files'''
