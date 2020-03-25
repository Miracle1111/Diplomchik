import pygame
import random


carImg = pygame.image.load('racecar.png')

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 200
HEIGHT = 200

# This sets the margin between each cell
MARGIN = 5

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
matrix_value = []
for row in range(3):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    matrix_value.append([])
    for column in range(5):
        grid[row].append(0)  # Append a cell
        matrix_value[row].append(0)
print(matrix_value)
# Set row 1, cell 5 to one. (Remember rows and
# column numbers start at zero.)
a = 0
c = 0
# for i in range(4):
#     for j in range (5):
#         matrix_value[i][j] = 0
# print(matrix_value[c][a])
# matrix_value[c][a] = 0
for i in range(random.randint(1, 3)):
    a = random.randint(0, 4)
    c = random.randint(0, 2)
    if matrix_value[c][a] != 1:
        grid[c][a] = 1
        matrix_value[c][a] = 1
        print(a, c)
    else:
        print('There is no space here!')
# print(matrix_value)
# Initialize pygame
pygame.init()

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [1000, 600]
screen = pygame.display.set_mode(WINDOW_SIZE)


def car(x, y):
    screen.blit(carImg, (x, y))


# Set title of screen
pygame.display.set_caption("Array Backed Grid")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            if matrix_value[row][column] != 1:
                # User clicks the mouse. Get the position
                # pos = pygame.mouse.get_pos()
                # # Change the x/y screen coordinates to grid coordinates
                # column = pos[0] // (WIDTH + MARGIN)
                # row = pos[1] // (HEIGHT + MARGIN)
                # Set that location to one
                grid[row][column] = 1
                matrix_value[row][column] = 1
                # print(matrix_value)
                # print("Click ", pos, "Grid coordinates: ", row, column)
            else:
                print('This place is occupied!')

    # Set the screen background
    screen.fill(BLACK)

    # Draw the grid
    for row in range(3):
        for column in range(5):
            color = BLACK
            if grid[row][column] == 1:
                car((MARGIN + WIDTH)*column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN)


    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()