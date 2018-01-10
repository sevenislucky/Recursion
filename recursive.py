def factual(n):
	print("I am working with " + str(n) + " and saving it behind the scene")
	if n == 0:
		print("I've now reached my base case 0")
		return 1

	else:
		answer =  n * factual(n - 1)
		print("All gravy..so the answer to factual(" + str(n)+ ")" + " = " + str(answer))
		return answer
	
print(factual(5))

# simplest form
#def fact(n):
#	if n == 0:
#		return 1
#	else:
#		return n * fact(n-1) #calling it self, minus 1
#	
#print(fact(5))