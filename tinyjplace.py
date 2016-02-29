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
      '''dictionary contains newick tree information3'''
        self._tree = {}
        
    def __str__(self):
        return self._content
        
    def __node__(self, nodes = total):
        """standalone function. returns number of internal, external, and total nodes. Should it be nodes or edges?"""
        
    def __branch__(self, initial_node = 0, leaf = none):
        '''calculates the branch length given the starting node and ending node. default ending node is none, 
        this finds the longest branch length and returns it.'''
        
    def __branch.length)__(self, edge):
        '''returns the branch length for that edge'''

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
