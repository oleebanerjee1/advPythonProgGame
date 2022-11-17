import pygame
pygame.init()

walls = []
displayX = 640
displayY = 640
window = pygame.display.set_mode((displayX, displayY))
pygame.display.set_caption("Maze Test")

x = 230
y = 230
width = 20
height = 20
run = True

mazeLayout = """
WWWWWWWWWW
W   W    W
W WWWWWW W
W      W W
WWW WWWWWW
W W W  W W
W   W    W
W WWW W  W
W     W  W
WWWWWWWWEW
""".splitlines()[1:]
print(mazeLayout)

block = pygame.image.load("C:\\Users\\olee1\\Pictures\\block.png").convert()

# Using blit to copy content from one surface to other
window.blit(block, (0, 0))



for row in range(0, 10):
    for column in range(0, 10):
        if mazeLayout[row][column:column+1] == "W":
            walls.append([column*64, row*64])
            print(walls)
        if mazeLayout[row][column:column+1] == "E":
            exit = [column*64, row*64]
            print(exit)

for i in range(0, len(walls)):
    window.blit(block, (walls[i][0], walls[i][1]))
    print(walls[i][0], walls[i][1])

# paint screen one time
pygame.display.flip()

while (run):
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


