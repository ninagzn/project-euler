digits = [2]
n = 1000
for i in range(1,n):
    remainder =0 
    for j in range(len(digits)):
        product = digits[j]*2
        digits[j] = product%10 + remainder
        remainder = product/10
    
    if remainder > 0:
        digits.append(1)

    print i+1, digits

sum = 0 
for d in range(digits):
    sum += d

print sum
