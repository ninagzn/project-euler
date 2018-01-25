from problemEuler import ProblemEuler
from math import sqrt

class Problem91(ProblemEuler):
    def getSolution(self):
        n=50
        count=0
        for x1 in range(0,n+1):
            for y1 in range(0,n+1):
                for x2 in range(x1, n+1):
                    for y2 in range(0,y1+1):
                        if self.isRightTriangle(x1, y1, x2, y2):
                           count+=1
                

        return count
        
    def isRightTriangle(self, x1, y1, x2, y2):
       a=self.getSegmentSquareLength(0,0,x1,y1)
       b=self.getSegmentSquareLength(0,0,x2,y2)
       c=self.getSegmentSquareLength(x1,y1,x2,y2)

       if a==0 or b==0 or c==0:
           return False

       return a==b+c or b==a+c or c==a+b

    def getSegmentSquareLength(self,x1,y1,x2,y2):
        return (x2-x1)**2+(y2-y1)**2

p = Problem91()
print (p.getSolution())