import pygame
pygame.init()

displayX = 500
displayY = 500
window = pygame.display.set_mode((displayX, displayY))
pygame.display.set_caption("Continuous Movement Test")

x = 230
y = 230
width = 20
height = 20
vel = 5
key = 0
pointArr = [(x + width/2, y + height/2), (x + width, y + height), (x + width, y)]
run = True
time = 0
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

block = pygame.image.load("C:\\Users\\olee1\\Pictures\\block.png").convert()

# Using blit to copy content from one surface to other
window.blit(block, (0, 0))

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
    window.fill((0, 0, 0))  # Fills the screen with black
    pygame.draw.ellipse(window, (255, 234, 0), (x, y, width, height))
    pygame.draw.polygon(window, (0, 0, 0), (pointArr[0], pointArr[1], pointArr[2]))
    # quick blurb of instructions for a short amount of time
    time += 1
    if time < 50:
        font = pygame.font.Font('freesansbold.ttf', 19)
        text = font.render('Use the arrow keys to move your avatar up and down.', True, (255, 0, 0))
        window.blit(text, (0, 0))
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
    # If it reaches the boundaries of the screen stop and print game over
    if x < 0 or y < 0 or x+width == displayX or y+height == displayY:
        vel = 0
        font = pygame.font.Font('freesansbold.ttf', 50)
        text = font.render('Game Over', True, (255, 0, 0))
        window.blit(text, (0, 0))
    pygame.display.update()

pygame.quit()