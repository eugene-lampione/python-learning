# DICTIONARIES
favorite_pizza = {
	"John":"Pepperoni",
	"Tim":"Mushroom",
	"Mary":"Cheese",
	"Beatrice":"Ham and Onion",
	"Bluto":"Supreme"
}
favorite_pizza["Bob"] = "Tuna"
favorite_pizza.pop("Tim")
print(favorite_pizza)

username = "John";

favorite_pizzas = {
	username: "Pepperoni",
	"Tim":"Mushroom",
	"Mary":"Cheese",
	"Beatrice": "Ham and Onion",
	"Bluto": 41
}

print(favorite_pizzas)
print(favorite_pizzas[username])
print(favorite_pizzas["John"])
print(favorite_pizzas["Bluto"]+3)

print(favorite_pizzas.keys())
print(favorite_pizzas.values())

for x,y in favorite_pizzas.items():
	print(f"Key:{x} | Value:{y}")

favorite_pizzanum = {
	1:"Pepperoni",
	2:"Mushroom",
	3:"cheese",
	4:"Hame and Onion",
	5:"Supreme"
}

print(favorite_pizzanum)