weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K/L): ")

if unit == 'K':
    weight *= 2.205
    unit = "Lb."
elif unit == 'L':
    weight /= 2.205
    unit = "Kg"
else:
    print("Invalid unit!")
    exit()

print(f"Your weight is {round(weight, 1)} {unit}")
