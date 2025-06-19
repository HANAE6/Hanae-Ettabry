number=int(input("enter a number:"))
length=int(input("enter a length:"))
multiples = []
for i in range(1, length + 1):
    multiples.append(number * i)
    print("The list of multiples is:", multiples)