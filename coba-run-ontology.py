from owlready2 import *

#loads owl file
ontology_file=get_ontology("CKB.owl").load(reload=True)

print(ontology_file.classes())
list_of_classes=list(ontology_file.individuals())
print(list_of_classes)
print(ontology_file.individuals())
print(ontology_file.object_properties())
# print(ontology_file.SchoolSubject.Geography)
for c in list_of_classes: print(c.name)