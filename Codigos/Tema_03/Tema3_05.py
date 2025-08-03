#Tema3_05
import turtle
def tree(length,n):
    
    if length < (length/n):
           return
    turtle.forward(length)
    turtle.left(45)
    tree(length * 0.5,length/n)
    turtle.left(20)
    tree(length * 0.5,length/n)
    turtle.right(75)
    tree(length * 0.5,length/n)
    turtle.right(20)
    tree(length * 0.5,length/n)
    turtle.left(30)
    turtle.backward(length)
    return
turtle.left(90)
turtle.backward(30)
turtle.color("green")
tree(200,4)