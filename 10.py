__author__ = 'student'
import turtle as tu
import math
tu.color ('red')
tu.shape('turtle')
n=100
f=10
for i in range(1,f+1):
    for i in range (1,n+1):
        tu.forward(100*math.sin(math.pi/n))
        tu.left(360/n)
    tu.left(60)