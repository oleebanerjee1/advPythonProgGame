import pygame
pygame.init()

displayX = 640
displayY = 640
window = pygame.display.set_mode((displayX, displayY))
pygame.display.set_caption("Continuous Movement Test")


width = 40
height = 40
x = displayX/2 - width/2
y = displayY/2 - height/2
vel = 5
key = 0
pointArr = [(x + width/2, y + height/2), (x + width, y + height), (x + width, y)]
run = True
pastX = 0
pastY = 0
lifeColor = [(255, 0, 0), (255, 0, 0), (255, 0, 0)]
numDeaths = 0
died = False

walls = []
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

while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_LEFT) or (event.key == pygame.K_RIGHT) or \
                    (event.key == pygame.K_UP) or (event.key == pygame.K_DOWN):
                key = event.key
            #pygame.key.get_pressed()

    if key == pygame.K_LEFT:
        x -= vel
        pointArr = mouthLeft()
    if key == pygame.K_RIGHT:
        x += vel
        pointArr = mouthRight()
    if key == pygame.K_UP:
        y -= vel
        pointArr = mouthUp()
    if key == pygame.K_DOWN:
        y += vel
        pointArr = mouthDown()
    pygame.draw.ellipse(window, (0, 0, 0), (pastX, pastY, width, height)) # past character turns black to user can't see
    pygame.draw.ellipse(window, (255, 234, 0), (x, y, width, height))
    pastX = x
    pastY = y
    pygame.draw.polygon(window, (0, 0, 0), (pointArr[0], pointArr[1], pointArr[2]))
    lives = [pygame.draw.ellipse(window, lifeColor[0], (displayX-20, 10, 10, 10)), pygame.draw.ellipse(window, lifeColor[1], (displayX-35, 10, 10, 10)),pygame.draw.ellipse(window, lifeColor[2], (displayX-50, 10, 10, 10))]

    # Printing the mouth in different directions
    def mouthDown():
        point1 = (x + width/2, y + height/2)
        point2 = (x, y + height)
        point3 = (x + width, y + height)
        arr = [point1, point2, point3]
        return arr
    def mouthRight():
        point1 = (x + width/2, y + height/2)
        point2 = (x + width, y + height)
        point3 = (x + width, y)
        arr = [point1, point2, point3]
        return arr
    def mouthUp():
        point1 = (x + width/2, y + height/2)
        point2 = (x, y)
        point3 = (x + width, y)
        arr = [point1, point2, point3]
        return arr
    def mouthLeft():
        point1 = (x + width/2, y + height/2)
        point2 = (x, y + height)
        point3 = (x, y)
        arr = [point1, point2, point3]
        return arr
    # If it reaches the boundaries of the screen set one circle to black
    if x < 0 or y < 0 or x + width == displayX or y + height == displayY:
        numDeaths += 1
        died = True
        if numDeaths <= 3:
            print("reached")
            print("NumDeaths:", str(numDeaths - 1))
            lifeColor[numDeaths - 1] = (0, 0, 0)
            print(str(lifeColor))

    if died: #if it has died return to center of screen
        x = displayX / 2 - width / 2
        y = displayY / 2 - height / 2
        died = False
    #if died more than 3 times -> game over
    if numDeaths >= 3:
        vel = 0
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('GAME OVER', True, (255, 0, 0))
        window.blit(text, (0, 0))

    pygame.display.update()

pygame.quit()