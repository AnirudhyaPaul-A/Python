# 3. Program to change temperature from Fahrenheit to Celsius

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9
fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = fahrenheit_to_celsius(fahrenheit)
print(f"{fahrenheit} Fahrenheit is equal to {celsius:.2f} Celsius.")
