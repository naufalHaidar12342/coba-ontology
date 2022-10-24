from owlready2 import *

#loads owl file
ontology_file=get_ontology("CKB.owl").load()

print(ontology_file.classes())
print(ontology_file.individuals())