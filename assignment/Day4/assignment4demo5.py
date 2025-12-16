 # List of lambda functions for weight conversions
conversions = [
    lambda t: t * 1000,                 # tonnes to kilograms
    lambda kg: kg * 1000,               # kilograms to grams
    lambda g: g * 1000,                 # grams to milligrams
    lambda mg: mg * 0.00000220462       # milligrams to pounds
]

# Input from user (in tonnes)
tonnes = float(input("Enter weight in tonnes: "))

# Perform conversions step by step
kg = conversions[0](tonnes)
gm = conversions[1](kg)
mg = conversions[2](gm)
lbs = conversions[3](mg)

# Output results
print("\n--- Weight Conversions ---")
print(f"{tonnes} tonnes = {kg} kg")
print(f"{kg} kg = {gm} gm")
print(f"{gm} gm = {mg} mg")
print(f"{mg} mg = {lbs} lbs")