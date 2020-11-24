import turtle

#  向前100像素  画笔旋转90度 再向前100像素 行成第2条  旋转四次

turtle.speed(8)     # 控制速度
turtle.pencolor('red')  # 画笔颜色
turtle.fillcolor('yellow')  # 填充颜色
turtle.begin_fill()    # 开始填充
# turtle.fd(100)
# turtle.left(90)
# turtle.fd(100)
# turtle.left(90)
# turtle.fd(100)
# turtle.left(90)
# turtle.fd(100)
# turtle.left(90)
for z in range(36):      # 需要36个正方形
    for u in range(4):   #一条线画完  转换 角度  4次正方形
        turtle.fd(100)
        turtle.right(90)
    turtle.right(10)   #  每个正方形画完以后 调整角度
turtle.end_fill()  # 填充结束

turtle.mainloop()
