# PROJECT 2 

# _______________________________________PYTHON SNAKE GAME__________________________________________

#IMPORTING SOME LIBRARIES

import turtle
import random
import time


#CREATING SCREEN 

screen = turtle.Screen()
screen.title('SNAKE-GAME-USING-PYTHONA')
screen.setup(width = 700, height = 700)
screen.tracer(0)
turtle.bgcolor('#93c5fd')



## CREATING BORDER FOR SNAKE

turtle.speed(6)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310,250)
turtle.pendown()
turtle.color('black')
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.penup()
turtle.hideturtle()

#SCORE

score = 0
delay = 0.1


#SNAKE-FOOD
Food = turtle.Turtle()
Food.speed(0)
Food.shape('circle')
Food.color('red')
Food.penup()
Food.goto(30,30)


#CREATING SNAKE
snake = turtle.Turtle()
snake.speed(0)
snake.shape('square')
snake.color("black")
snake.penup()
snake.goto(0,0)
snake.direction = 'stop'

old_food=[]

#User score

scoring = turtle.Turtle()
scoring.speed(0)
scoring.color("black")
scoring.penup()
scoring.hideturtle()
scoring.goto(0,300)
scoring.write("Score :",align="center",font=("Courier",24,"bold"))


#DEFINING THE DIRECTIONS

def snake_go_up():
    if snake.direction != "down":
        snake.direction = "up"

def snake_go_down():
    if snake.direction != "up":
        snake.direction = "down"

def snake_go_left():
    if snake.direction != "right":
        snake.direction = "left"

def snake_go_right():
    if snake.direction != "left":
        snake.direction = "right"

#HOW SNAKE IS MOVING TOWARDS DIRECTIONS  

def snake_move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)

    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)

    if snake.direction == "left":                   
        x = snake.xcor()
        snake.setx(x - 20)

    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)

# Keyboard bindings

screen.listen()     #It detects that when user has hit certain keys on the keyboard or moved/clicked the mouse

screen.onkeypress(snake_go_up, "Up")      #MOVES UP BY HITING UP KEY IN KEYBOARD
screen.onkeypress(snake_go_down, "Down")    #MOVES DOWN BY HITING DOWN(ARROW) KEY IN KEYBOARD
screen.onkeypress(snake_go_left, "Left")    #MOVES LEFT BY HITING LEFT(ARROW) KEY IN KEYBOARD
screen.onkeypress(snake_go_right, "Right")  #MOVES RIGHT BY HITING RIGHT(ARROW) KEY IN KEYBOARD

# MAIN LOOP

while True:
        screen.update()
            #snake and snkae-food crash
        if snake.distance(Food)< 20:
                x = random.randint(-290,270)
                y = random.randint(-240,240)
                Food.goto(x,y)
                scoring.clear()
                score+=1
                scoring.write("Score:{}".format(score),align="center",font=("Courier",24,"bold"))
                delay-=0.001
                
                ## creating new_ball
                new_food = turtle.Turtle()
                new_food.speed(0)
                new_food.shape('square')
                new_food.color('red')
                new_food.penup()
                old_food.append(new_food)
                

        #ADDING FOOD TO SNAKE
        
        for index in range(len(old_food)-1,0,-1):
                a = old_food[index-1].xcor()
                b = old_food[index-1].ycor()

                old_food[index].goto(a,b)
                                     
        if len(old_food)>0:
                a= snake.xcor()
                b = snake.ycor()
                old_food[0].goto(a,b)
        snake_move()

        ##SNAKE AND BORDER COLLISION
        if snake.xcor()>280 or snake.xcor()< -300 or snake.ycor()>240 or snake.ycor()<-240:
                time.sleep(1)
                screen.clear()
                screen.bgcolor('#c4b5fd')
                scoring.goto(0,0)
                scoring.write("   GAME OVER \n Your Score is {}".format(score),align="center",font=("Courier",30,"bold"))


        ## SNKAE CLASH
        for food in old_food:
                if food.distance(snake) < 20:
                        time.sleep(1)
                        screen.clear()
                        screen.bgcolor('#d8b4fe')
                        scoring.goto(0,0)
                        scoring.write("    GAME OVER \n Your Score is {}".format(score),align="center",font=("Courier",30,"bold"))
        
        time.sleep(delay)
        
turtle.Terminator()




