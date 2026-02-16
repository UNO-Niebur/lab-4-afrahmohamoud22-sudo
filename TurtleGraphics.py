#TurtleGraphics.py
#Name: Afrah Mohamoud 
#Date: 02/15/2026
#Assignment: Lab 4 


import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)


def main():
    myTurtle = turtle.Turtle() 
    # drawPolygon(myTurtle, 5) #draws a pentagon
    # drawPolygon(myTurtle, 8) #draws an octogon
  
  import turtle

def squaresInSquares(myTurtle, num):
    
    # Save starting position
    start_x = myTurtle.xcor()
    start_y = myTurtle.ycor()
    
    # Initial square size
    square_size = 300
    
    # Size decrease for each inner square
    size_decrease = square_size / (num + 1)
    
    # Draw num squares
    for i in range(num):
        current_size = square_size - (i * size_decrease)
        half_size = current_size / 2
        
        # Move to starting corner of current square (top-left)
        myTurtle.penup()
        myTurtle.goto(start_x - half_size, start_y + half_size)
        myTurtle.pendown()
        
        # Draw the square
        for side in range(4):
            myTurtle.forward(current_size)
            myTurtle.right(90)
    
    # Return to center
    myTurtle.penup()
    myTurtle.goto(start_x, start_y)


# Create the turtle
myTurtle = turtle.Turtle()
myTurtle.speed(0.10)  # speed

# The function
squaresInSquares(myTurtle, 3)  # write 5 or 3 squares in squares

    # fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    # fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

def drawSquare(myTurtle, size):
    for side in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def fillCorner(joy, corner):
    square_size = 120
    half_size = square_size / 2
    
    start_x = joy.xcor()
    start_y = joy.ycor()
    joy.penup()
    joy.goto(start_x - half_size, start_y + half_size)
    joy.pendown()
    
    drawSquare(joy, square_size)
    
    # Logic for Quadrants Formula
    if corner == 2:  # Top-Right
        fill_x = start_x 
        fill_y = start_y + half_size
    elif corner == 3:  # Bottom-Left
        fill_x = start_x - half_size
        fill_y = start_y
    else:
        print("Invalid corner number. Use 2 or 3.")
        return
    
    # Starting w/ calculating in the fill in point
    joy.penup()
    joy.goto(fill_x, fill_y)
    joy.pendown()
    
    joy.begin_fill()
    drawSquare(joy, half_size)
    joy.end_fill()
    
    # Return to center
    joy.penup()
    joy.goto(start_x, start_y)
    joy.setheading(0) # Reset heading
    joy.pendown()

def main():
    screen = turtle.Screen()
    joy = turtle.Turtle()
    joy.speed(3)
    
    # Test Corner 2
    fillCorner(joy, 2)
    
    # Move over and test Corner 3
    joy.penup()
    joy.goto(130, 0)
    joy.pendown()
    fillCorner(joy, 3)
   
    # squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares
    import turtle

def squaresInSquares(myTurtle, num):
    
    # Save starting position
    start_x = myTurtle.xcor()
    start_y = myTurtle.ycor()
    
    # Initial square size
    square_size = 300
    
    # Size decrease for each inner square
    size_decrease = square_size / (num + 1)
    
    # Draw num squares
    for i in range(num):
        current_size = square_size - (i * size_decrease)
        half_size = current_size / 2
        
        # Move to starting corner of current square (top-left)
        myTurtle.penup()
        myTurtle.goto(start_x - half_size, start_y + half_size)
        myTurtle.pendown()
        
        # Draw the square
        for side in range(4):
            myTurtle.forward(current_size)
            myTurtle.right(90)
    
    # Return to center
    myTurtle.penup()
    myTurtle.goto(start_x, start_y)


# Create the turtle
myTurtle = turtle.Turtle()
myTurtle.speed(0.10)  # speed

# The function
squaresInSquares(myTurtle, 3)  # write 5 or 3 squares in squares


turtle.done()

main() 