number = int(input("Enter a natural number: "))

n = number
factorial = number


while n - 1 > 0:
   factorial = factorial * (n - 1)
   n = n - 1
   
print(factorial)