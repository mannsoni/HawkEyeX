import turtle
#import pillow


# Initialize the turtle and set up the screen
screen = turtle.Screen()
screen.setup(width=500, height=500)
screen.screensize(bgcolor="black")

# Create a new turtle
t = turtle()

# Draw something on the screen
t.color("white")
t.begin_fill()
t.circle(100)
t.end_fill()

# Check for a white-colored part in the output
image = getImage('glass.jpg')
pixels = image.load()
width, height = image.size
for x in range(width):
    for y in range(height):
        if pixels[x, y] == (255, 255, 255):
            print("True")
            turtle.done()
            exit()

# If no white-colored part is found, print "False"
print("False")
turtle.done()