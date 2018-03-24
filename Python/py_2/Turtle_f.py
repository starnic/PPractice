#绘制四边形
import turtle as tt

tt.setup(400,300,0,0)
tt.penup()
tt.fd(-100)
tt.pendown()
for i in range(4):
    tt.fd(100)
    tt.right(90)
tt.done()
