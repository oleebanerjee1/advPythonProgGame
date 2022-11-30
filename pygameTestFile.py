import pygame
pygame.init()

displayX = 640
displayY = 640
window = pygame.display.set_mode((displayX, displayY))
pygame.display.set_caption("Continuous Movement Test")
#show instruction screen until user clicks out
end_it = False
rect1 = (255, 0, 0)
rect2 = (255, 0, 0)
while (end_it == False):
    pygame.draw.rect(window, rect1, (240, 180, 160, 80))
    pygame.draw.rect(window, rect2, (240, 280, 160, 80))
    myfont = pygame.font.SysFont("Britannic Bold", 40)
    smallfont = pygame.font.SysFont("Britannic Bold", 35)
    welcome = myfont.render("Welcome!", 1, (255, 0, 0))
    start = myfont.render("Start", 1, (0, 0, 0))
    quit = myfont.render("Quit", 1, (0, 0, 0))
    instruct = myfont.render("Use the arrow keys to control the Pacman", 1, (255, 0, 0))
    extraLife = smallfont.render("Eating this allows you to gain another life:", 1, (255, 0, 0))
    obstacle = smallfont.render("Hitting this obstacle kills you:", 1, (255, 0, 0))
    for event in pygame.event.get():
        rect1 = (255, 0, 0)
        rect2 = (255, 0, 0)
        if pygame.mouse.get_pos()[0] >= 240 and pygame.mouse.get_pos()[0] <= 400 and pygame.mouse.get_pos()[1] >= 180 and pygame.mouse.get_pos()[1] <= 240:
            rect1 = (0, 255, 0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                end_it = True
        elif pygame.mouse.get_pos()[0] >= 240 and pygame.mouse.get_pos()[0] <= 400 and pygame.mouse.get_pos()[1] >= 280 and pygame.mouse.get_pos()[1] <= 340:
            rect2 = (0, 255, 0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
    window.blit(welcome, (250, 50))
    window.blit(instruct, (50, 100))
    window.blit(start, (290, 210))
    window.blit(quit, (290, 310))
    window.blit(obstacle, (10, 500))
    pygame.draw.ellipse(window, (80, 200, 120), (390, 503, 20, 20))
    window.blit(extraLife, (10, 400))
    pygame.draw.ellipse(window, (255, 0, 0), (540, 403, 20, 20))
    pygame.display.flip()
window.fill([0, 0, 0])
width = 40
height = 40
x = 72
y = 72
vel = 4
key = 0
pointArr = [(x + width/2, y + height/2), (x + width, y + height), (x + width, y)]
run = True
pastX = 2*width
pastY = 2*height
lifeColor = [(255, 0, 0), (255, 0, 0), (255, 0, 0)]
numDeaths = 0
died = False
#1 = right, 2 = down, 3 = left, 4 = up
mouthDirection = 1
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
obstacle = pygame.draw.ellipse(window, (80, 200, 120), (7 * 64, 8 * 64, 20, 20))
obstacleX = 7 * 64
obstacleY = 8 * 64
obstacleVelocity = 3

# block = pygame.image.load("C:\Users\olee1\\PycharmProjects\\advPythonProgGame\\block.png").convert()
block = pygame.image.load('block1.png')
lightningBolt = pygame.image.load('lightningBolt.png')
window.blit(lightningBolt, (64, 5*64))

for row in range(0, 10):
    for column in range(0, 10):
        if mazeLayout[row][column:column+1] == "W":
            walls.append([column*64, row*64])
            # print(walls)
        if mazeLayout[row][column:column+1] == "E":
            exit = [column*64, row*64]
            print(exit)

for i in range(0, len(walls)):
    window.blit(block, (walls[i][0], walls[i][1]))
    # print(walls[i][0], walls[i][1])

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

    #depending on the key hit the pacman's mouth switches and he moves that way
    if key == pygame.K_LEFT:
        x -= vel
        pointArr = mouthLeft()
        mouthDirection = 3
    if key == pygame.K_RIGHT:
        x += vel
        pointArr = mouthRight()
        mouthDirection = 1
    if key == pygame.K_UP:
        y -= vel
        pointArr = mouthUp()
        mouthDirection = 4
    if key == pygame.K_DOWN:
        y += vel
        pointArr = mouthDown()
        mouthDirection = 2
    pygame.draw.ellipse(window, (0, 0, 0), (pastX, pastY, width, height)) # past character turns black to user can't see
    pygame.draw.ellipse(window, (255, 234, 0), (x, y, width, height))
    pastX = x
    pastY = y
    pygame.draw.polygon(window, (0, 0, 0), (pointArr[0], pointArr[1], pointArr[2]))
    lives = [pygame.draw.ellipse(window, lifeColor[0], (displayX-20, 10, 10, 10)), pygame.draw.ellipse(window, lifeColor[1], (displayX-35, 10, 10, 10)),pygame.draw.ellipse(window, lifeColor[2], (displayX-50, 10, 10, 10))]

    # for the life that you can eat
    if x + width >= 407 and y + height >= 215:
        if numDeaths == 0:
            died = True
        else:
            numDeaths = numDeaths - 1
            lifeColor[numDeaths] = (255, 0, 0)
            died = True


    if y>=256-height and y <=320 and x>=64 and x<=192:
        numDeaths += 1
        died = True
        if numDeaths <= 3:
            lifeColor[numDeaths - 1] = (0, 0, 0)
    elif y>=320-height and y<=384 and x>= 128- width and x<=192:
        numDeaths += 1
        died = True
        if numDeaths <= 3:
            lifeColor[numDeaths - 1] = (0, 0, 0)

    elif 128 <= (x + width) and x <= 320 and 448 <= (y + height) and y <= 512:
        numDeaths += 1
        died = True
        if numDeaths <= 3:
            lifeColor[numDeaths - 1] = (0, 0, 0)

    elif 256 <= (x + width) and x <= 320 and 256 <= (y + height) and y <= 512:
        numDeaths += 1
        died = True
        if numDeaths <= 3:
            lifeColor[numDeaths - 1] = (0, 0, 0)

    elif 64*6 <= (x+width) and x <= 448 and 64*7 <= y+height:
        numDeaths += 1
        died = True
        if numDeaths <= 3:
            lifeColor[numDeaths - 1] = (0, 0, 0)

    elif 320 <= (x + width) <= 576 and 256 <= (y + height) <= 320:
        numDeaths += 1
        died = True
        if numDeaths <= 3:
            lifeColor[numDeaths - 1] = (0, 0, 0)

    elif 448 <= (x + width) and x <= 512 and 128 <= (y + height) and y <= 384:
        numDeaths += 1
        died = True
        if numDeaths <= 3:
            lifeColor[numDeaths - 1] = (0, 0, 0)

    elif 256 <= (x + width) and 256 <= (y + height) <= 320:
        numDeaths += 1
        died = True
        if numDeaths <= 3:
            lifeColor[numDeaths - 1] = (0, 0, 0)

    elif 384 <= (x + width) <= 448 and 448 <= (y + height):
        numDeaths += 1
        died = True
        if numDeaths <= 3:
            lifeColor[numDeaths - 1] = (0, 0, 0)

    elif 4*64 <= (x + width) <= 5*64 and 64 <= (y + height) <= 2*64:
        numDeaths += 1
        died = True
        if numDeaths <= 3:
            lifeColor[numDeaths - 1] = (0, 0, 0)
    elif x +width > 128 and x<448 and y < 192 and y+ height>128:
        numDeaths += 1
        died = True
        if numDeaths <= 3:
            lifeColor[numDeaths - 1] = (0, 0, 0)

    # adding obstacle
    # if the obstacle hits the edge, its velocity becomes negative
    if obstacleX >= 9 * 64 - 20:
        obstacleVelocity = -3
    elif obstacleX <= 7 * 64:
        obstacleVelocity = 3

    obstacleX += obstacleVelocity
    pygame.draw.ellipse(window, (0, 0, 0), (
    obstacleX - obstacleVelocity, obstacleY, 20, 20))  # past character turns black to user can't see
    pygame.draw.ellipse(window, (80, 200, 120), (obstacleX, obstacleY, 20, 20))

    # if pacman hits the obstacle, he loses a life and moves back to the start
    if x <= obstacleX + 10 <= x + width and y <= obstacleY + 10 <= y + height:
        numDeaths += 1
        died = True
        if numDeaths <= 3:
            lifeColor[numDeaths - 1] = (0, 0, 0)

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
    #if it reaches the end of maze stop moving and print you win
    if (x <= displayX - (64+width) and y >= displayY - height and x > exit[0]):
        vel = 0
        font = pygame.font.Font('freesansbold.ttf', 40)
        text = font.render('YOU WIN', True, (255, 0, 0))
        window.blit(text, (0, 0))
    #else if it reaches the boundaries of the screen set one circle to black and add to numdeaths
    elif x < 64 or y < 64 or x + width >= displayX-64 or y + height >= displayY-64 and (x < exit[0] or x > displayX - (64+width)):
        numDeaths += 1
        died = True
        if numDeaths <= 3:
            lifeColor[numDeaths - 1] = (0, 0, 0)

    if died: #if it has died return to left corner of screen
        x = 72
        y = 72
        key = pygame.K_RIGHT
        died = False

    #if died more than 3 times -> game over
    if numDeaths >= 3:
        vel = 0
        font = pygame.font.Font('freesansbold.ttf', 40)
        text = font.render('GAME OVER', True, (255, 0, 0))
        window.blit(text, (0, 0))

    pygame.draw.ellipse(window, (255, 0, 0), (407, 215, 20, 20)) #extra  life

    pygame.display.update()

pygame.quit()
