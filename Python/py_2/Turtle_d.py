#绘制叠边形
import turtle as tt

tt.setup(400,400,0,0)
tt.penup()
tt.fd(-120)
tt.pensize(3)
tt.pendown()
tt.left(15)
for i in range(9):
    tt.fd(100)
    tt.right(80)
tt.done()
