import math

def calculate_equilibrium_constant(concentrations, stoichiometric_coefficients):
    equilibrium_constant = 1.0
    for i in range(len(concentrations)):
        equilibrium_constant *= concentrations[i] ** stoichiometric_coefficients[i]
    return equilibrium_constant

def calculate_reaction_index(concentrations, stoichiometric_coefficients):
    reaction_index = 0.0
    for i in range(len(concentrations)):
        reaction_index += stoichiometric_coefficients[i] * math.log(concentrations[i])
    return reaction_index

def predict_chemical_reaction(equilibrium_constant, reaction_index):
    if reaction_index > 0:
        print("The reaction is spontaneous and will proceed to the right.")
    elif reaction_index < 0:
        print("The reaction is non-spontaneous and will proceed to the left.")
    else:
        print("The reaction is at equilibrium.")

def main():
    num_species = int(input("Enter the number of reactants and products: "))

    concentrations = []
    stoichiometric_coefficients = []

    print("Enter the concentrations and stoichiometric coefficients for each species:")
    for i in range(num_species):
        concentration = float(input(f"Concentration of species {i + 1}: "))
        coefficient = int(input(f"Stoichiometric coefficient of species {i + 1}: "))
        concentrations.append(concentration)
        stoichiometric_coefficients.append(coefficient)

    equilibrium_constant = calculate_equilibrium_constant(concentrations, stoichiometric_coefficients)
    reaction_index = calculate_reaction_index(concentrations, stoichiometric_coefficients)

    print("Equilibrium constant:", equilibrium_constant)
    print("Reaction index:", reaction_index)

    predict_chemical_reaction(equilibrium_constant, reaction_index)

if __name__ == "__main__":
    main()
