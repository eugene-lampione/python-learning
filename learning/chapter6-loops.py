#while loops
#num = 0
#while num < 10:
#	num += 1
#	if num == 5:
#		continue
	#print(num)

#for loops
#for num in range(6):
#	print("I LOVE CHEESE!")

#names = ["John","Mary","Tim"]
#for name in names:
#	print(name)
#	for x in name:
#		print(x)

for x in range(1,101):
	if x % 3 == 0 and x % 5 == 0:
		print(f"{x} FIZZ BUZZ!")
	elif x % 3 == 0:
		print(f"{x} FIZZ")
	elif x % 5 == 0:
		print(f"{x} BUZZ")
	else:
		print(x)