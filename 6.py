print('vvedite kolichestvo lap')
n=int(input())
import turtle as tu

tu.color ('red')
tu.shape('turtle')
for i in range(1,n+1):
    tu.forward(100)
    tu.stamp()
    tu.goto(0,0)
    tu.left(360/n)
