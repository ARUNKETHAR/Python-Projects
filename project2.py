# project 2 Breakout Game
# import necessary libraries(graphics, random, time, math)
from graphics import*
from math import*
from random import*
from time import*

# Initializes the Floor graphics window
# Name: ‘Floor’
# Size: 400 x 400 pixels
# Background Color: light green
# Coordinates system: Floor.setCoords(0,0,400,400)
Floor = GraphWin('Floor', 400, 400)
Floor.setBackground('light green')
Floor.setCoords(0, 0, 400, 400)



# Initializes the bar at the bottom middle of Floor
# Size: 100 x 20 pixel
# Color: Black
Bob = Rectangle(Point(150, 0), Point(250, 20))
Bob.setFill('black')
Bob.draw(Floor)



# Initializes the Control window
# Name: ‘Control’
# Size: 200 x 150 pixels
# Coordinates system: Control.setCoords(0,0,200,150)
Control = GraphWin('Control', 200, 150)
Control.setCoords(0, 0, 200, 150)
Control.setBackground('white')




# Name: controPanel
# Parameter: empty
# Purpose: draw the buttons in the Control window to represent the movements “Left”, & “Right”.
# Return value: return a list contains(left square object, right square object)
def controlPanel():
    # creates the squares that will go in the control window
    # using Point(27,60), Point(57,90) for left square, Point(142,60), Point(172,90)for right square
    P1 = Point(27, 60)
    P2 = Point(57, 90)
    P3 = Point(142, 60)
    P4 = Point(172, 90)
    Lbutton = Rectangle(P1, P2)
    Rbutton = Rectangle(P3, P4)
    
    
    # puts the squares in a list for easy access
    a = []
    a.append(Lbutton)
    a.append(Rbutton)
    
    # sets the color of each square to blue
    Lbutton.setFill('blue')
    Rbutton.setFill('blue')

    # draws each of the squares in the control window
    Lbutton.draw(Control)
    Rbutton.draw(Control)
	
    # return the list(e.g: [left square object, right square object])
    return (a)


        
# Name: checkButton
# Parameter: the point object(which is the point the user click on the control windows)
# Purpose: check for a mouse click in either the Floor or the Control graphics window.
# Return values: return the movement distance of Bob along x axis. (datatype: list)
#e.g: click left button, return (-30,0)
#e.g: click right button, return (30,0)
def checkButton(point):
    if(point !=  None):
        xvalue = point.getX()
        yvalue = point.getY()
            # see if click was on LEFT BUTTON
        if(xvalue >= 27 and xvalue <= 57):
            if(yvalue >= 60 and yvalue <= 90):
                return [-30, 0]
            
    

            # see if click was on RIGHT BUTTON
        if(xvalue >= 142 and xvalue <= 172):
            if(yvalue >= 60 and yvalue <= 90):
                return [30, 0]


# Name: makeCircles
# Parameter: empty
# Purpose: create the bouncing ball.  
# Return value: a list contains [circle object,2,3](datatype: list).
def makeCircles():
    b1 = randint(100, 300)
    b2 = randint(100, 300)
    bb = Circle(Point(b1, b2), 10)
    bb.setFill('yellow')
    bb.draw(Floor)

    circlelist = [bb, 2, 3]
    return circlelist
    


# Name: circleBounceY
# Parameter: coord, speed
# Purpose: for checking the y coord of the ball
# If the first integer is greater than 395,
# the function should return the inverse value of the 2nd integer,
# Otherwise, the function should return the 2nd integer unmodified.
# Return value: return the updated speed(datatype: integer)
def circleBounceY(coord, speed):
    if(coord > 395):
        speed = (-1) * speed
        return speed
    return speed
    
# Name: circleBounceX
# Parameter: coord, speed
# Purpose: for checking the x coord of the ball
# If the first integer is either less than 5 or greater than 395,
# the function should return the inverse value of the 2nd integer,
# Otherwise, the function should return the 2nd integer unmodified.
# Return value: return the updated speed(datatype: integer)
def circleBounceX(coord, speed):
    if(coord < 5 or coord > 395):
        speed = (-1) * speed
        return speed
    return speed
               
    

    

#This function generates a random color
#Parameters: None
#Returns RGB color object(created by function: color_rgb)
def generateRandomColor():
    R = randint(0, 225)
    G = randint(0, 225)
    B = randint(0, 225)
    return(color_rgb(R, G, B))



# main function
def main():
    # draw necessary shapes on Control window and Floor window
    scoretracker = 0
    controlPanel()
    ball = makeCircles()           

    scoretext = Text(Point(30, 387), 'Score: ')
    scoreresult = Text(Point(65, 384), scoretracker)
    scoretext.draw(Floor)
    scoreresult.draw(Floor)

    ball[1] = 2
    ball[2] = 3
    # game starts from here
    if(Floor.getMouse() != None):
        while(True):
        
        #update the message for score
            scoreresult.setText(str(scoretracker))

        #get the center coordinates of bob x, y
            centerBob = Bob.getCenter()
            
            centerCircle = ball[0].getCenter()


        #get the center coordinates of circle
            if(fabs(centerBob.x - centerCircle.x) <= 50 and centerCircle.y - 10 and centerCircle.y - 10  < centerBob.y + 10):
                ball[2] = ball[2] * -1.2
                ball[1] = ball[1] * 1.2
                ball[0].setFill(generateRandomColor())
                ball[0].move(ball[1], ball[2])
                scoretracker += 1
                
            if(centerCircle.y <= -10):
                break
            
                
     
        #checks if circles are hitting the bounds; if so, returns negative of velocity
            
            centerCircle.x = centerCircle.x + ball[1]
            centerCircle.y = centerCircle.y + ball[2]
            #ball[1] = circleBounceX(centerCircle.x, ball[1])
            #ball[2] = circleBounceY(centerCircle.y, ball[2])
        
        #moves the circles according to the value returned by the circleBounce functions
            ball[0].move(ball[1], ball[2])
            ball[1] = circleBounceX(centerCircle.x, ball[1])
            ball[2] = circleBounceY(centerCircle.y, ball[2])
        #checks to see which button was clicked in the control window
            point = Control.checkMouse()
            button = checkButton(point)

        #movs Bob based on the button that was clicked
            if(button != None):
                Bob.move(button[0], button[1])
        

        #getting bob's location to see if he's trying to sneak out of the Floor
            if(centerBob.x <= 25) or (centerBob.x >= 375):
                Bob.move(button[1], button[0])

        #don't allow Bob to move outside of the window. He should move back to his previous position
            
        #call sleep(1/50) for animation.
            sleep(1/50)
                 
        # close windows
        Floor.close()
        Control.close()

main()

