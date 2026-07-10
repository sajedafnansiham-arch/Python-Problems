#Program to convert Fahrenheit to Celsius
#Formula: C = (F - 32) * 5/9

Fahrenheit = float(input("Enter temprature in Fahrenheit  : "))

Celsius = (Fahrenheit - 32) * 5/9

print(f"{Fahrenheit}°F = {Celsius:.2f}°C")