num = 12345
sum = 0



while num:
    
    reamin = num%10
    sum += reamin
    
    num = int(num/10)

print(sum)


