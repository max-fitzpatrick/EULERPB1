##If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
##Find the sum of all the multiples of 3 or 5 below 1000.

numbersToTest = []
multiplesFound = []

print("The test will use integers from 1 to n, specify n below")
n = int(input())
while True:
    print("\nWhich numbers do you want to find multiples of?\nPress enter to exit")
    divisor = input()
    if divisor == "":
        break
    else:
        numbersToTest.append(divisor)
        continue

for i in range(1,n):
    for j in range(int(len(numbersToTest))):
        if i%int(numbersToTest[j]) == 0:
            multiplesFound.append(i)

uniqueMultiples = set(multiplesFound)
result = sum(uniqueMultiples)

print("\nSUMMARY")
print("Range tested: 1 to " + str(n))
print("Divisors used: " + str(numbersToTest))
print("Multiples found: " + str(uniqueMultiples))
print("The sum of these multiples is: " + str(result))