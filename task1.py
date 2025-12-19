import pulp


# model
model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# variables
lemonade = pulp.LpVariable("Lemonade", lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable("Fruit_Juice", lowBound=0, cat='Integer')

# function to the model
model += lemonade + fruit_juice, "Total_Products"

# resource constraints
model += (2 * lemonade + fruit_juice <= 100), "Water_Constraint"
model += (lemonade <= 50), "Sugar_Constraint"
model += (lemonade <= 30), "Lemon_Juice_Constraint"
model += (2 * fruit_juice <= 40), "Fruit_Puree_Constraint"

model.solve()

print("------------Result------------")
print(f"Solution status: {pulp.LpStatus[model.status]}")
print("-" * 30)
print(f"Lemonade quantity: {lemonade.varValue}")
print(f"Fruit Juice quantity: {fruit_juice.varValue}")
print(f"Total products produced: {pulp.value(model.objective)}")
print("-" * 30)
print(f"Water: {2 * lemonade.varValue + fruit_juice.varValue} used out of 100 available")
print(f"Sugar: {lemonade.varValue} used out of 50 available")
print(f"Lemon Juice: {lemonade.varValue} used out of 30 available")
print(f"Fruit Puree: {2 * fruit_juice.varValue} used out of 40 available")
