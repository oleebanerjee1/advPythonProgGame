import pygame
pygame.init()

window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Continuous Movement Test")

x = 0
y = 0
width = 40
height = 40
vel = 5
key = 0
pointArr = [(x + 20, y + 20), (x + 40, y + 40), (x + 40, y)]
run = True

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
    #printing the mouth in different directions
    def mouthDown():
        point1 = (x + 20, y + 20)
        point2 = (x, y + 40)
        point3 = (x + 40, y + 40)
        arr = [point1, point2, point3]
        return arr
    def mouthRight():
        point1 = (x + 20, y + 20)
        point2 = (x + 40, y + 40)
        point3 = (x + 40, y)
        arr = [point1, point2, point3]
        return arr
    def mouthUp():
        point1 = (x + 20, y + 20)
        point2 = (x, y)
        point3 = (x + 40, y)
        arr = [point1, point2, point3]
        return arr
    def mouthLeft():
        point1 = (x + 20, y + 20)
        point2 = (x, y + 40)
        point3 = (x, y)
        arr = [point1, point2, point3]
        return arr
    #if it reaches the boundaries of the screen stop and print game over
    if x < 0 or y < 0 or x+40 == 500 or y+40 == 500:
        vel = 0
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('Game Over', True, (255, 0, 0))
        window.blit(text, (0,0))
    pygame.display.update()

pygame.quit()
