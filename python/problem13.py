 
with open("problem13.in") as file:
    bigNumbers = file.readlines()

sum=long(0)
for x in bigNumbers:
    sum+=long(x.strip()) 
 
print str(sum)[:10]