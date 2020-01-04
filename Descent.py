import turtle
import winsound

# Creating level list
levels = [[[]]]*50

# Defining the levels. 0's are empty spaces, 1's are obstacles, A is the starting point, B is the endpoint, (if it exists) K is the location of the key)
levels[1] = ["01010B1","1010010","0100101","1001010","A010101"]
levels[2] = ["001010B","0100010","1001000","1000000","A001101"]
levels[3] = ["111100B","0001000","0001000","0001000","A001111"]
levels[4] = ["1001001","0000001","0101010","001K000","A00B101"]
levels[5] = ["110001A","0000010","1000000","001K000","0001100","1000000","B000001"]
levels[6] = ["00001B0","1000100","00010A0","K010001","0100100","0010000","0000010"]
levels[7] = ["A000100","0010000","0001000","1000000","B010000","0000011","010001K"]
levels[8] = ["100000B","0000010","0010000","0000100","0100001","0K01000","A001001"]
levels[9] = ["010000100","100100001","A010K100B","000010000","000000010"]
levels[10] = ["001001000","100000001","000010010","0100001K0","A001B0000"]
    
# Setting up the screen
win = turtle.Screen()
win.bgcolor("black")
win.setup(1000,1000)
win.title("Descent")

# Adding custom shapes
win.addshape("key.gif")
win.addshape("door.gif")
win.addshape("lock.gif")
win.addshape("star.gif")

# Creating the pen
pen = turtle.Turtle()
pen.hideturtle()

# Creating tile pen
tile = turtle.Turtle()
tile.hideturtle()
tile.color("white")
tile.speed(0)
tile.penup()

# Creating key pen
key = turtle.Turtle()
key.hideturtle()
key.penup()
key.speed(0)
key.shape("key.gif")

# Creating door pen
door = turtle.Turtle()
door.hideturtle()
door.penup()
door.speed(0)
door.shape("door.gif")

# Creating lock pen
lock = turtle.Turtle()
lock.hideturtle()
lock.penup()
lock.speed(0)
lock.shape("lock.gif")

# Creating move pen
pencil = turtle.Turtle()
pencil.hideturtle()
pencil.penup()
pencil.speed(0)
pencil.color("White")

# Creating level pen
levelpen = turtle.Turtle()
levelpen.hideturtle()
levelpen.penup()
levelpen.speed(0)
levelpen.color("White")

# Creating star pen
starpen = turtle.Turtle()
starpen.hideturtle()
starpen.penup()
starpen.speed(0)
starpen.color("White")
starpen.shape("star.gif")

# Creating a pen wrriting the least number of moves possible
best = turtle.Turtle()
best.hideturtle()
best.penup()
best.speed(0)
best.color("White")


# Creating the necessary lists
obstacles = [""] # The x, y location of every obstacles for a given level
start = [""] # The starting location of each level
finish = [""] # The location of the doors for every level
keys = [0]*50 # (If it exists) the location of the keys in the level
moves = ["", 9, 6, 4, 5, 9, 6, 8, 10, 9,8,0,0,0,0,0,0] # The amount of moves it takes to earn 3 stars for a given level

# Declaring necessary variables
currentLvl = 1 # The current level
size = 72 # The size of each square in pixels
gap = 8 # The length of the gap between each square in pixels
stamp = size/2 - gap/2 # The size of the white squares
hasKey = 0 # is 1 if the player has key or no key in the level
move = 0 # The number of moves the player has made in the level
star = 0 # The stars earned by the player
xlen = len(levels[currentLvl][0]) # The number of squares per row for each level
ylen = len(levels[currentLvl]) # The number of squares per column for each level


# Tile drawing function
def drawLevel(level):
    
    drawBorder(level)
    
    win.addshape("tile", ((-stamp,-stamp), (-stamp,stamp), (stamp,stamp), (stamp,-stamp)))
    tile.shape("tile")
    
    for y in range(ylen):
        for x in range(xlen):
            value = level[y][x]
            
            xCor = -xlen*(size/2) + (x*size) + size/2
            yCor = ylen*(size/2) - (y*size) -size/2
            if value != '1':
                tile.goto(xCor, yCor)
                tile.stamp()
            if value == '1':
                obstacles.append((xCor, yCor))
            if value == 'A':
                start.append((xCor, yCor))
            if value == 'B':
                finish.append((xCor, yCor))
                door.goto(xCor, yCor)
                door.stamp()
            if value == 'K':
                key.goto(xCor, yCor)
                key.stamp()
                keys[currentLvl] = (xCor, yCor)
                
    if keys[currentLvl] != 0:
        lock.goto(finish[currentLvl])
        lock.stamp()
        obstacles.append(finish[currentLvl])
    
    levelpen.setposition(0,size*((ylen + 1)/2))
    levelpen.write("LEVEL " + str(currentLvl),align="center", font=("Courier New", 36, "normal"))
    
    pencil.setposition(-size*(xlen /2),-size*((ylen + 2)/2))
    pencil.write("MOVE: " + str(move), align="left", font=("Courier New", 24, "bold"))
    
    starpen.setposition(size*((xlen -0.5 )/2),-size*((ylen + 1.5)/2) + 6)
    starpen.stamp()
    starpen.goto(size*(xlen /2) - 48,-size*((ylen + 2)/2))
    starpen.write(str(star), align="right", font=("Courier New", 24, "bold"))
    
    best.setposition(0,-size*((ylen + 4)/2))
    best.write("TO GET 3 STARS COMPLETE THE LEVEL IN " + str(moves[currentLvl]) + " MOVES OR LESS!", align="center", font=("Courier New", 16, "normal"))
    
    
                    
                
# border drawing function
def drawBorder(level):
    xlen = len(level[0])
    ylen = len(level)
    
    pen.penup()
    pen.speed(0)
    pen.pensize(2)
    pen.color("white")
    pen.setposition(-(size*xlen/2 + gap),-(size*ylen/2 + gap)) # Setting the start position to bottom left
    pen.pendown()
    for i in range(2):
        pen.forward((size*xlen + 2*gap))
        pen.left(90)
        pen.forward((size*ylen + 2*gap))
        pen.left(90)
                
def moveLeft():
    player.hideturtle()
    while True:
        if player.xcor() - size == -size*((xlen + 1)/2) and (player.xcor() + (xlen - 1)*size, player.ycor()) not in obstacles:
            nextStepX = player.xcor() + (xlen - 1)*size
        elif player.xcor() - size == -size*((xlen + 1)/2) and (player.xcor() + (xlen - 1)*size, player.ycor()) in obstacles:
            break
        else:
            nextStepX = player.xcor() - size
        nextStepY = player.ycor()
        if (nextStepX, nextStepY) not in obstacles:
            player.goto(nextStepX, nextStepY)
        else:
            break
    player.showturtle()
    moveCounter()
    
def moveRight():
    player.hideturtle()
    while True:
        if player.xcor() + size == size*((xlen + 1)/2) and (player.xcor() - (xlen - 1)*size, player.ycor()) not in obstacles:
            nextStepX = player.xcor() - (xlen - 1)*size
        elif player.xcor() + size == size*((xlen + 1)/2) and (player.xcor() - (xlen - 1)*size, player.ycor()) in obstacles:
            break
        else:
            nextStepX = player.xcor() + size
        nextStepY = player.ycor()
        if (nextStepX, nextStepY) not in obstacles:
            player.goto(nextStepX, nextStepY)
        else:
            break
    player.showturtle()
    moveCounter()

def moveUp():
    player.hideturtle()
    while True:
        if player.ycor() + size == size*((ylen + 1)/2) and (player.xcor(), player.ycor() - (ylen - 1)*size) not in obstacles:
            nextStepY = player.ycor() - (ylen - 1)*size
        elif player.ycor() + size == size*((ylen + 1)/2) and (player.xcor(), player.ycor() - (ylen - 1)*size) in obstacles:
            nextStepY = player.ycor()
            break
        else:
            nextStepY = player.ycor() + size
        nextStepX = player.xcor()
        if (nextStepX, nextStepY) not in obstacles:
            player.goto(nextStepX, nextStepY)
        else:
            break
    player.showturtle()
    moveCounter()
   
def moveDown():
    player.hideturtle()
    while True:
        if player.ycor() - size == -size*((ylen + 1)/2) and (player.xcor(), player.ycor() + (ylen - 1)*size) not in obstacles:
            nextStepY = player.ycor() + (ylen - 1)*size
        elif player.ycor() - size == -size*((ylen + 1)/2) and (player.xcor(), player.ycor() + (ylen - 1)*size) in obstacles:
            nextStepY = player.ycor()
            break
        else:
            nextStepY = player.ycor() - size
        nextStepX = player.xcor()
        if (nextStepX, nextStepY) not in obstacles:
            player.goto(nextStepX, nextStepY)
        else:
            break
    player.showturtle()
    moveCounter()
    
def restartLevel():
    global hasKey
    hasKey = 0
    global move
    move = 0
    pencil.clear()
    pencil.write("MOVE: " + str(move), align="left", font=("Courier New", 24, "bold"))
    player.setposition(start[currentLvl])
    if keys[currentLvl] != 0:
        key.goto(keys[currentLvl])
        key.stamp()
        lock.goto(finish[currentLvl])
        lock.stamp()
        obstacles.append(finish[currentLvl])
        
def moveCounter():
    global move
    move += 1
    winsound.PlaySound("move.wav", winsound.SND_ALIAS)
    pencil.clear()
    pencil.write("MOVE: " + str(move), align="left", font=("Courier New", 24, "bold"))

        
drawLevel(levels[currentLvl])

# Creating player turtle      
player = turtle.Turtle()
player.hideturtle()
player.penup()
player.speed(0)
player.shape("square")
player.color("black")
player.setposition(start[currentLvl])
player.showturtle()

turtle.listen()
turtle.onkey(moveLeft, "Left")
turtle.onkey(moveRight, "Right")
turtle.onkey(moveUp, "Up")
turtle.onkey(moveDown, "Down")
turtle.onkey(restartLevel, "r")

win.tracer(0)

# Main game loop
while True:
    if keys[currentLvl] == 0:
        hasKey = 1
    elif (player.xcor(), player.ycor()) == (keys[currentLvl]):
        hasKey = 1
        key.clearstamps() 
        lock.clearstamps()
        if finish[currentLvl] in obstacles:
            obstacles.remove(finish[currentLvl])
        
        
    if (player.xcor(), player.ycor()) == (finish[currentLvl]) and hasKey == 1:
        if move <= moves[currentLvl]:
            star += 3
        elif move <= 2*moves[currentLvl]:
            star += 2
        else:
            star += 1
        currentLvl += 1
        xlen = len(levels[currentLvl][0])
        ylen = len(levels[currentLvl])
        tile.clearstamps()
        door.clearstamps()
        starpen.clearstamps()
        starpen.clear()
        pen.clear()
        pencil.clear()
        best.clear()
        levelpen.clear()
        obstacles = [""]
        hasKey = 0
        move = 0
        if currentLvl == 11:
            winsound.PlaySound("theend.wav", winsound.SND_ALIAS)
            pencil.goto(0,50)
            pencil.write("THE END", align="center", font=("Courier New", 48, "bold"))
            pencil.goto(0,-50)
            pencil.write("Your Score: " + str(star), align="center", font=("Courier New", 24, "bold"))
            break
        drawLevel(levels[currentLvl])
        player.setposition(start[currentLvl])
        winsound.PlaySound("end.wav", winsound.SND_ALIAS)
    
    win.update()
