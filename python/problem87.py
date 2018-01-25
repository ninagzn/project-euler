from problemEuler import ProblemEuler
from math import sqrt

class Problem87(ProblemEuler):
    def getSolution(self):
        maxNumber = 5*(10**7)
        maxPrime= int(sqrt(maxNumber-24))

        primes = self.getPrimes(maxPrime)
        powerTriples=set()
        for i in primes:
            for j in primes:
                n=i**2+j**3
                if n>maxNumber:
                    break;
                for k in primes:
                    m=n+k**4
                    if m>maxNumber:
                        break
                    powerTriples.add(m)
                
        return len(powerTriples)
    

    def getPrimes(self, maxPrime):
        primes = []
        for i in range (2,maxPrime+1):
            isPrime = True
            for j in primes:
                if i%j == 0:
                    isPrime = False
                    break
            
            if (isPrime):
                primes.append(i)
        
        return primes


p = Problem87()
print (p.getSolution())

