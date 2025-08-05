def check_prime(n):
    if n == 1:
        return True
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

n = int(input("Enter Value of N:"))
val = n
prime_factors = []
while True:
    if (check_prime(val)):
        prime_factors.append(val)
        break
    for i in range(2,n//2):
        while(val%i == 0):
            val = int(val/i)
            if i not in prime_factors:
                prime_factors.append(i)

print(prime_factors)
print(sum(prime_factors))
