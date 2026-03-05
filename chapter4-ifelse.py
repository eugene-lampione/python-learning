x = 41
if x == 42:
	print("X does in fact equal 41!")
else:
	print("X does NOT equal 41!")

print("-----")

name = "John"
if name == "Bob" or name == "John":
	print("Hi there Bob or John!")

print("-----")

name = input("Enter your Name:")
print(f"The name {name} has {len(name)} characters.")
