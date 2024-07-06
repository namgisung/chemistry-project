import math

def calculate_equilibrium_constant(reactant_concentrations, product_concentrations, reactant_coefficients, product_coefficients):
    equilibrium_constant = 1.0
    for i in range(len(product_concentrations)):
        equilibrium_constant *= product_concentrations[i] ** product_coefficients[i]
    for i in range(len(reactant_concentrations)):
        equilibrium_constant /= reactant_concentrations[i] ** reactant_coefficients[i]
    return equilibrium_constant

def calculate_reaction_index(reactant_concentrations, product_concentrations, reactant_coefficients, product_coefficients):
    reaction_index = 0.0
    for i in range(len(product_concentrations)):
        reaction_index += product_coefficients[i] * math.log(product_concentrations[i])
    for i in range(len(reactant_concentrations)):
        reaction_index -= reactant_coefficients[i] * math.log(reactant_concentrations[i])
    return reaction_index

def predict_chemical_reaction(equilibrium_constant, reaction_index):
    if reaction_index > 0:
        print("The reaction is spontaneous and will proceed to the right.")
    elif reaction_index < 0:
        print("The reaction is non-spontaneous and will proceed to the left.")
    else:
        print("The reaction is at equilibrium.")

def main():
    num_reactants = int(input("Enter the number of reactants: "))
    num_products = int(input("Enter the number of products: "))

    reactant_concentrations = []
    reactant_coefficients = []
    product_concentrations = []
    product_coefficients = []

    print("Enter the concentrations and stoichiometric coefficients for reactants:")
    for i in range(num_reactants):
        concentration = float(input(f"Concentration of reactant {i + 1}: "))
        coefficient = int(input(f"Stoichiometric coefficient of reactant {i + 1}: "))
        reactant_concentrations.append(concentration)
        reactant_coefficients.append(coefficient)

    print("Enter the concentrations and stoichiometric coefficients for products:")
    for i in range(num_products):
        concentration = float(input(f"Concentration of product {i + 1}: "))
        coefficient = int(input(f"Stoichiometric coefficient of product {i + 1}: "))
        product_concentrations.append(concentration)
        product_coefficients.append(coefficient)

    equilibrium_constant = calculate_equilibrium_constant(reactant_concentrations, product_concentrations, reactant_coefficients, product_coefficients)
    reaction_index = calculate_reaction_index(reactant_concentrations, product_concentrations, reactant_coefficients, product_coefficients)

    print("Equilibrium constant:", equilibrium_constant)
    print("Reaction index:", reaction_index)

    predict_chemical_reaction(equilibrium_constant, reaction_index)

if __name__ == "__main__":
    main()
