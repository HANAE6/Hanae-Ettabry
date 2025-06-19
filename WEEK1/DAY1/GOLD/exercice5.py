n=input("enter the 1st number:")
y=input("enter the 2nd number:")
x=input("enter the 3nd number:")
if n >= y and n>= x:
    greatest = n
elif y >= n and y >= x:
    greatest = y
else:
    greatest = x
print(greatest)