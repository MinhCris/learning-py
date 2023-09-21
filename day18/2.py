import turtle

# Khởi tạo turtle
t = turtle.Turtle()

# Vẽ một đường thẳng dài 100 pixel
t.pendown()
t.forward(100)

# Di chuyển turtle mà không vẽ
t.penup()
t.backward(50)

# Vẽ một đường thẳng khác dài 50 pixel
t.pendown()
t.forward(50)

# Kết thúc chương trình
turtle.done()
