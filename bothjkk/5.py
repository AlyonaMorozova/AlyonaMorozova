author__ = 'student'
import turtle as tu

tu.color ('red')
tu.shape('classic')
i=1
n=1
for n in range(10):
    for i in range(4):
        tu.forward(20*n)
        tu.right(90)
    tu.penup()
    tu.left(90)
    tu.forward(10)
    tu.left(90)
    tu.forward(10)
    tu.left(180)
    tu.pendown()

