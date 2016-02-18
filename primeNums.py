print("This program takes a lower and upper positive boundary, and generates all prime numbers in that range.")
numLow = int(input("Enter your lower boundary: "))
numHigh = int(input("Enter your upper boundary: "))
print("Prime numbers between %d and %d:" %(numLow, numHigh))
for num in range(numLow, numHigh):
    for i in range(2, num):
        if num%i == 0:
            break

    else:
        print("%d is prime" %num)
