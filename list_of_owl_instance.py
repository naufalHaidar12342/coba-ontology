from owlready2 import *

#loads owl file
ontology_file=get_ontology("CKB.owl").load(reload=True)
print("\n")

#check classses available from CKB.owl
# geography_IRI=get_ontology("http://www.semanticweb.org/caressesOntology#Geography").load(only_local=True)
# print(geography_IRI.classes())\


print(list(ontology_file.Geography.subclasses()))