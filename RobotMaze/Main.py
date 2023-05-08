#   a115_robot_maze.py
import turtle as trtl


######ALL THE CHALLANGES ARE AT THE BOTTOM######

#----- maze and turtle config variables
screen_h = 400
screen_w = 420
startx = -100
starty = -100
turtle_scale = 1.5

#------ robot commands
def move():
  robot.dot(10)
  robot.fd(50)


def turn_left():
  robot.speed(0)
  robot.lt(90)
  robot.speed(2)
  
  
def moveUp():
  robot.setheading(90)
  
  
def moveDown():
  robot.setheading(270)
  
  
def moveLeft():
  robot.setheading(180)
  
  
def moveRight():
  robot.setheading(0)
  
  
#----- init screen
wn = trtl.Screen()
wn.setup(width=screen_w, height=screen_h)
robot_image = "robot.gif"
wn.addshape(robot_image)

#----- init robot
robot = trtl.Turtle(shape=robot_image)
robot.hideturtle()
robot.color("darkorchid")
robot.pencolor("darkorchid")
robot.penup()
robot.setheading(90)
robot.turtlesize(turtle_scale, turtle_scale)
robot.goto(startx, starty)
robot.speed(2)
robot.showturtle()

#---- TODO: change maze here
wn.bgpic("maze4.png") # other file names should be maze2.png, maze3.png

#---- TODO: begin robot movement here
# move robot forward with move()
# turn robot left with turn_left()
# sample for loop:

##############################################################################################################################
##############################################################################################################################
##############################################################################################################################

#code for maze 1
def maze1():
  for i in range(4):
    move()
    for i in range(3):
      turn_left()
    move()
    turn_left()
#code for maze 2
def maze2():
  for i in range(3):
    move()
    
  for i in range(3):
      turn_left()
      
  for i in range(2):
        move()
  robot.goto(startx,starty)
  for i in range(3):
    move()
  turn_left()
  for i in range(3):
    move()
  turn_left()
  for i in range(1):
    move()
#code for maze 3
def maze3():
  for i in range(1):
    move()
  for i in range(3):
    turn_left()
  for i in range(1):
    move()
  for i in range(1):
    turn_left()
  move()
  for i in range(3):
    turn_left()
  for i in range(1):
    move()
  for i in range(1):
    turn_left()
  for i in range(1):
    move()
  for i in range(3):
    turn_left()
  for i in range(1):
    move()
  for i in range(1):
    turn_left()
  for i in range(1):
    move()
  for i in range(3):
    turn_left()
  for i in range(1):
    move()
#code for maze 4
def maze4():
  for i in range(1):
    move()
  for i in range(3):
    turn_left()
  for i in range(1):
    move()
  for i in range(1):
    turn_left()
  for i in range(2):
    move()
  for i in range(3):
    turn_left()
  for i in range(3):
    move()
  for i in range(1):
    turn_left()
  for i in range(1):
    move()
    

#functions for maze1, maze2, and maze3
'''
maze1()
maze2()
maze3()
maze4()
'''
#functions for maze1, maze2, and maze3


#Bander Second Challange
def secondchallange():
  loop = 0
  while loop != 1:
    wn.bgpic("maze1.png")
    robot.goto(startx,starty)
    maze1()
    robot.clear()
    wn.bgpic("maze2.png")
    robot.goto(startx,starty)
    maze2()
    robot.clear()
    wn.bgpic("maze3.png")
    robot.goto(startx,starty)
    for i in range(3):
      turn_left()
    maze3()
    robot.clear()
    wn.bgpic("maze4.png")
    robot.goto(startx,starty)
    for i in range(1):
      turn_left()
      #####THIRD CHALLANGE#####
    maze4()
    robot.clear()
    #####THIRD CHALLANGE#####
'''
secondchallange()
'''
#Bander Second Challange


###THIRD CHALLANGE IS IN SECOND CHALLANGE###


#not important code for assignment
def forthchallange():
  x1 = -150
  y1 = -100

  ui=input("w,a,s,d")
  actions={"w":moveUp(),
          "a":moveLeft(),
          "s":moveDown(),
          "d":moveRight()}

  ####### BLACK BLOCKS ARE A LITTLE BUGGY, AT FIRST THEY WONT BLOCK YOU BUT AFTER A FEW SECONDS, IT WILL #############
  while True:
    ui = input("w,a,s,d,stop")
    if robot.xcor() <= -150 or robot.ycor() <=-150 or robot.xcor() == -100 and robot.ycor() == 0 or robot.xcor() == 0 and robot.ycor() == -100 or robot.xcor() == 0 and robot.ycor() == -50 or robot.xcor() == 0 and robot.ycor() == 0 or robot.xcor() == -50 and robot.ycor() == 100 or robot.xcor() == 0 and robot.ycor() == 100 or robot.xcor() == 50 and robot.ycor() == 0 or robot.xcor() == 100 and robot.ycor() == 0 or robot.xcor() == 150 and robot.ycor() == 0:
      robot.goto(startx,starty)
      print("WORKED")
    else:
          if ui=="w":
            moveUp()
            move()
            print(robot.pos())
            
          elif ui=="a":
            moveLeft()
            move()
            print(robot.pos())
          elif ui=="s":
            moveDown()
            move()
            print(robot.pos())
          elif ui=="d":
            moveRight()
            move()
            print(robot.pos())
          elif ui =="stop":
            exit()
          else:
            print("worked")
  
    
    
#obviously, check for user input

#################################################################################################################################
#################################################################################################################################
#################################################################################################################################






#---- end robot movement 

wn.mainloop()


