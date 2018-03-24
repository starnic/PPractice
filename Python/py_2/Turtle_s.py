#绘制六边形
import turtle as tt

tt.setup(400,400,0,0)
tt.penup()
tt.fd(-100)
tt.pendown()
for i in range(6):
    tt.fd(100)
    tt.right(60)
tt.done()
