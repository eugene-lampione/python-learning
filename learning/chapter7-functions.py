#functions
def fizzbuzz(x):
	if x%3 == 0 and x%5 == 0:
		print(f"{x} is FIZZ BUZZ!")
	elif x%3 == 0:
		print(f"{x} is FIZZ")
	elif x%5==0:
		print(f"{x} is BUZZ")
	else:
		print(f"{x} is Boring")

#fizzbuzz(15)

def is_even(x):
	if x%2 == 0:
		return True
	else:
		return False

myvar = is_even(98)
#print(myvar)

def namer(first = "John", last="Elder"):
	print(f"Hello {first} {last}, nice to meet you!")

namer("Tim")

