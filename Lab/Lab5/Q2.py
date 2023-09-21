import turtle

N = int(input("Input N: "))
tb = 100/N
count = 0

sq = turtle.Turtle()
window = turtle.Screen()

sq.speed(10)
# for i in range(N):
#     for j in range(N):
#         if (i + j) % 2 == 0:
#             for x in range(4):
#                 sq.forward(tb)
#                 sq.right(90)
#         sq.forward(tb)
#     sq.backward(tb * N)
#     sq.right(90)
#     sq.forward(tb)
#     sq.left(90)

# for i in range(N):
#     for j in range(N):
#         for k in range(4):
#             sq.forward(tb)
#             sq.right(90)
#     sq.backward(tb*N)
#     sq.right(90)
#     sq.forward(tb)
#     sq.left(90)
colors = ["white", "black"]
for i in range(N): 
    for j in range(N):
        sq.fillcolor(colors[(i + j) % 2])
        sq.begin_fill()
        for k in range(4):
            sq.forward(tb)
            sq.right(90)
        sq.end_fill()
        sq.forward(tb)
    sq.goto(0,0 - i*(tb))

    sq.right(90)
    sq.forward(tb)
    sq.left(90)

sq.right(90)

turtle.done()
