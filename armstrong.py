number = int(input("Enter a number: "))

digits = len(str(number))
total = 0
temp = number

while temp > 0:
    digit = temp % 10
    total += digit ** digits
    temp //= 10

if total == number:
    print(number, "is an Armstrong Number")
else:
    print(number, "is Not an Armstrong Number")
