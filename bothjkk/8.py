__author__ = 'student'
import turtle as tu

tu.color ('green')
tu.shape('turtle')
f=5
for i in range(1,500):
    tu.forward(25+f)
    tu.left(90)
    f+=5