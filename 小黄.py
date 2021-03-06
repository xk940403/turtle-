import turtle

turtle.setup(800,800)      # 设置画布大小

turtle.fillcolor('yellow')     # 头
turtle.begin_fill()
turtle.speed(0)
turtle.up()
turtle.goto(-150,150)
turtle.down()
turtle.right(90)
turtle.circle(150,-180)
turtle.left(180)
turtle.fd(310)              # 身体
turtle.left(180)
turtle.circle(150,-180)
turtle.left(180)
turtle.forward(310)
turtle.end_fill()

# 左画眼睛
turtle.speed(0)
turtle.up()
turtle.right(90)
turtle.goto(-80,150)
turtle.right(90)
turtle.down()
turtle.begin_fill()
turtle.width(5)
turtle.circle(40)
turtle.fillcolor('white')
turtle.end_fill()
turtle.speed(0)   # 右画眼睛
turtle.up()
turtle.goto(0,150)
turtle.down()
turtle.begin_fill()
turtle.width(5)
turtle.circle(40)
turtle.end_fill()

#  画右黑眼
turtle.right(90)
turtle.up()
turtle.setx(50)
turtle.down()
turtle.fillcolor('black')
turtle.right(90)
turtle.begin_fill()
turtle.circle(20)
turtle.right(270)
turtle.end_fill()
#  画右小白眼
turtle.speed(0)
turtle.width(0)
turtle.right(90)
turtle.fillcolor('white')
turtle.begin_fill()
turtle.circle(8)
turtle.end_fill()

#  画左黑眼
turtle.right(90)
turtle.up()
turtle.goto(-30,150)
turtle.right(180)
turtle.down()
turtle.fillcolor('black')
turtle.right(90)
turtle.begin_fill()
turtle.circle(20)
turtle.right(270)
turtle.end_fill()
#  画左小白眼
turtle.speed(0)
turtle.width(0)
turtle.right(90)
turtle.fillcolor('white')
turtle.begin_fill()
turtle.circle(8)
turtle.end_fill()

#  画左眼镜
turtle.up()
turtle.setx(-80)
turtle.left(90)
turtle.down()
turtle.width(20)
turtle.forward(70)
#  画右眼镜
turtle.up()
turtle.setx(80)
turtle.right(180)
turtle.down()
turtle.width(20)
turtle.forward(70)
#  画笑脸
turtle.up()
turtle.goto(-50,50)
turtle.down()
turtle.pencolor('red')
turtle.width(0)
turtle.width(2)
turtle.right(50)
turtle.circle(80,120)

#  画裤子
turtle.up()
turtle.right(70)
turtle.goto(-150,-160)
turtle.down()
turtle.width(0)
turtle.pencolor('black')
turtle.fillcolor('#176185')
turtle.begin_fill()
turtle.forward(50)
turtle.left(90)
turtle.forward(60)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(60)
turtle.left(90)
turtle.forward(50)
turtle.right(270)
turtle.circle(150,-180)
turtle.end_fill()

#  口袋
turtle.width(5)
turtle.up()
turtle.goto(-50,-140)
turtle.down()
turtle.forward(30)
turtle.circle(50,180)
turtle.forward(30)
turtle.left(90)
turtle.forward(100)

# 左裤腰带
turtle.fillcolor('#176185')
turtle.begin_fill()
turtle.width(0)
turtle.up()
turtle.goto(-100,-110)
turtle.down()
turtle.goto(-90,-100)
turtle.goto(-150,-35)
turtle.goto(-150,-50)
turtle.goto(-100,-110)
turtle.end_fill()

# 右裤腰带
turtle.fillcolor('#176185')
turtle.begin_fill()
turtle.width(0)
turtle.up()
turtle.goto(100,-110)
turtle.down()
turtle.goto(90,-100)
turtle.goto(150,-35)
turtle.goto(150,-50)
turtle.goto(100,-110)
turtle.end_fill()

# 头发
turtle.up()
turtle.goto((-30,295))
turtle.down()
turtle.width(2)
turtle.goto((-40,355))
turtle.up()
turtle.goto((-10,295))
turtle.down()
turtle.width(2)
turtle.goto(-16,345)
turtle.up()
turtle.goto(10,295)
turtle.down()
turtle.width(2)
turtle.goto(18,345)
turtle.up()
turtle.goto(30,295)
turtle.down()
turtle.width(2)
turtle.goto(40,355)

turtle.mainloop()
