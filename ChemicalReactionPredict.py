import math

def calculate_equilibrium_constant(reactant_concentrations, product_concentrations, reactant_coefficients, product_coefficients):
    equilibrium_constant = 1.0
    for i in range(len(product_concentrations)):
        equilibrium_constant *= product_concentrations[i] ** product_coefficients[i]
    for i in range(len(reactant_concentrations)):
        equilibrium_constant /= reactant_concentrations[i] ** reactant_coefficients[i]
    return equilibrium_constant

def calculate_reaction_index(reactant_concentrations, product_concentrations, reactant_coefficients, product_coefficients):
    reaction_index = 1.0
    for i in range(len(product_concentrations)):
        reaction_index *= product_concentrations[i] ** product_coefficients[i]
    for i in range(len(reactant_concentrations)):
        reaction_index /= reactant_concentrations[i] ** reactant_coefficients[i]
    return reaction_index

def predict_chemical_reaction(equilibrium_constant, reaction_index):
    if reaction_index < equilibrium_constant:
        print("이 반응은 정방향으로 반응한다.")
    elif reaction_index > equilibrium_constant:
        print("이 반응은 역방향으로 반응한다.")
    else:
        print("평형상태임.")

num_reactants = int(input("반응물의 물질 개수: "))
num_products = int(input("생성물의 물질 개수: "))

eq_reactant_concentrations = []
reactant_concentrations = []
reactant_coefficients = []
eq_product_concentrations = []
product_concentrations = []
product_coefficients = []

print("반응물의 평형 농도와 화학 빈응 계수를 입력:")
for i in range(num_reactants):
    eq_concentration = float(input(f"반응물 {i +1}의 평형 농도: "))
    concentration = float(input(f"반응물 {i +1}의 현재 농도: "))
    coefficient = int(input(f"반응물 {i + 1}의 화학 반응 계수: "))
    reactant_concentrations.append(concentration)
    reactant_coefficients.append(coefficient)
    eq_reactant_concentrations.append(eq_concentration)

print("생성물의 평형 농도와 화학 반응 계수를 입력:")
for i in range(num_products):
    eq_concentration = float(input(f"생성물 {i +1}의 평형 농도: "))
    concentration = float(input(f"생성물 {i +1}의 현재 농도: "))
    coefficient = int(input(f"생성물 {i +1}의 화학 반응 계수: "))
    product_concentrations.append(concentration)
    product_coefficients.append(coefficient)
    eq_product_concentrations.append(eq_concentration)

equilibrium_constant = calculate_equilibrium_constant(eq_reactant_concentrations, eq_product_concentrations, reactant_coefficients, product_coefficients)
reaction_index = calculate_reaction_index(reactant_concentrations, product_concentrations, reactant_coefficients, product_coefficients)

print("평형 상수:", equilibrium_constant)
print("반응 지수:", reaction_index)

predict_chemical_reaction(equilibrium_constant, reaction_index)

