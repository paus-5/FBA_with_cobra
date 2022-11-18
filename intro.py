import cobra
from cobra.io import load_model, read_sbml_model
model = load_model("textbook")


######## Explore model size
print(len(model.reactions))
print(len(model.metabolites))
print(len(model.genes))

##### Solve model, explore constraints

solution = model.optimize()

## Load local sbml file
path = "data/"
xml_file = "Salmonella_FBA.xml"
model2 = cobra.io.read_sbml_model(f"{path}{xml_file}")


