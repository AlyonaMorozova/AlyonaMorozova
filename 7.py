__author__ = 'student'
import turtle as tu

tu.color ('red')
tu.shape('turtle')
f=0.5
for i in range(1,500):
    tu.forward(f)
    tu.left(5)
    f+=0.05