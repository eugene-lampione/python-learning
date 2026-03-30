#fizz buzz
for x in range(1,101):
	printvar = "";
	if x % 3 == 0:
		printvar += "FIZZ"
	if x%5 == 0:
		if x%3==0: printvar+= " "
		printvar += "BUZZ"
	print(f"{x} {printvar}")

print("-----")

#multi-dimensional list
people = []
people.append(["Eugene","123 Main","5163161718"])
people.append(["Laura","123 Main","5162637467"])
people.append(["Cindy","456 Main","5163161548"])
people.append(["Lou","456 Main","5163160944"])

for person in people:
	print(person[2])

print("-----")
num = 0
for person in people:
	if (num+1)%2 == 0:
		print(person)

	num += 1