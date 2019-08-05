import turtle

turtle.screensize(200, 200, bg="#FFFFFF")
myPen = turtle.Turtle()
myPen.color("#000000")
myPen.speed(0)
boxSize = 10
turtle.tracer(1,0)

def goto_origin(myPen):
    myPen.home()

# This function draws a box by drawing each side of the square and using the fill function
def box(intDim):
    # Can also be done with a for loop - Can you rewrite thise function as such?
    myPen.begin_fill()
    # 0 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 90 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 180 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 270 deg.
    myPen.forward(intDim)
    myPen.left(90)
    myPen.end_fill()


def load_art(file_name):
    file = open(file_name)
    file_list = []
    for i in file:
        if i[-1] == '\n':
            line = i[:-1]
        line_list = line.split(",")
        file_list.append(line_list)
    return file_list[0], file_list[1:]

def draw(pallet, pixels):
    for line in pixels:
        for element in line:
            myPen.color(pallet[int(element)])
            box(boxSize)
            myPen.forward(boxSize)
        myPen.left(180)
        myPen.forward(len(line)*boxSize)
        myPen.left(90)
        myPen.forward(boxSize)
        myPen.left(90)

if __name__ == '__main__':
    # sample for loading art and calling draw
    pallet_1, pixels_1 = load_art("art/" + input("please enter the name of the file you want drawn > "))
    draw(pallet_1, pixels_1)
    #You need this to prevent the window from closing after drawing
turtle.done()
