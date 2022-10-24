from owlready2 import *

#loads owl file
ontology_file=get_ontology("CKB.owl").load()

ontology_file.classes()