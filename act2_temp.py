# Name: Jaysep Carlom
# Section: Baet 2101
# Task 4: Temperature Check

celsius = float(input ("Enter temperature in °C:"))

fahrenheit = celsius * 9 / 5 + 32
between = celsius >= 20 and celsius <= 30

print(f"Fahrenheit: {fahrenheit}")
print(f"Between 20 and 30 °C: {20 <= celsius <= 30}")

