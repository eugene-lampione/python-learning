def fizzbuzz(x):
	if x % 3 == 0 and x % 5 == 0:
		return f"{x}: FIZZ BUZZ"
	elif x % 3 == 0:
		return f"{x}: FIZZ"
	elif x % 5 == 0:
		return f"{x}: BUZZ"
	else:
		return x

checknum = input("Enter a number: ")
result = fizzbuzz(int(checknum))
print(result)
print("-----")
for x in range(1,101):
	fbresult = fizzbuzz(x)
	print(fbresult)
print("-----")
def sevenitems(a,b,c,d,e,f,g):
	print(f"a: {a}")
	print(f"b: {b}")
	print(f"c: {c}")
	print(f"d: {d}")
	print(f"e: {e}")
	print(f"f: {f}")
	print(f"g: {g}")

sevenitems("Hi","there","you",3,"how",2,5)
print("-----")

def welcome():
	name = input("What is you name?")
	print(f"Welcome {name}! This is my python program.")

welcome()