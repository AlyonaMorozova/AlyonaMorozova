__author__ = 'student'
import turtle as tu
import math
tu.color ('red')
tu.shape('turtle')
n=100
f=6
for u in range (f+1):

   for i in range (1,n+1):
        tu.forward((50+n*u)*math.sin(math.pi/n))
        tu.left(360/n)
   for i in range (1,n+1):
        tu.forward((50+n*u)*math.sin(math.pi/n))
        tu.right(360/n)


