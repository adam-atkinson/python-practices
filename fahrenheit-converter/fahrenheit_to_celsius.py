def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

print("=== Fahrenheit to Celsius Converter ===")

user_input = float(input("Enter temperature in Fahrenheit: "))
converted_temp = fahrenheit_to_celsius(user_input)
print(f"\n{user_input}°F is equal to {converted_temp:.2f}°C")
