# Sum of interger upto n

n = int(input("Enter the number : "))

sum = 0
for i in range(1,n+1):
    sum +=i 

print(f"sum of numbers from 1 to {n} is: {sum}")