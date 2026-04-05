print("== Contact Card ==\n")

name = input("Enter your name: ").strip().title()
phone = input("Enter your phone number: ").strip()
email = input("Enter your email address: ").strip()
address = input("Enter your address: ").strip()

print("\n--- Your Contact Card ---")
print(f"Name:    {name}")
print(f"Phone:   {phone}")
print(f"Email:   {email}")
print(f"Address: {address}")
print("-------------------------")