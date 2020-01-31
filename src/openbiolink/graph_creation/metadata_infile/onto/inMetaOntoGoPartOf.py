from openbiolink.edgeType import EdgeType
from openbiolink.graph_creation.metadata_infile.infileMetadata import InfileMetadata
from openbiolink.graph_creation.types.infileType import InfileType
from openbiolink.nodeType import NodeType
from openbiolink.namespace import *

class InMetaOntoGoPartOf(InfileMetadata):

    CSV_NAME = "DB_ONTO_GO_PART_OF_ontology.csv"
    USE_COLS = ['ID', 'PART_OF']
    NODE1_COL = 0
    NODE2_COL = 1
    QSCORE_COL = None
    NODE1_TYPE = NodeType.GO
    NODE1_NAMESPACE = Namespace(Namespaces.GO)
    NODE2_TYPE = NodeType.GO
    NODE2_NAMESPACE = Namespace(Namespaces.GO)
    EDGE_TYPE = EdgeType.PART_OF
    MAPPING_SEP = ';'
    INFILE_TYPE = InfileType.IN_ONTO_GO_PART_OF


    def __init__(self):
        super().__init__(csv_name=self.CSV_NAME,
                         cols=self.USE_COLS,
                         infileType=self.INFILE_TYPE)
