import pygame
pygame.init()

window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Continuous Movement Test")

x = 50
y = 50
width = 40
height = 40
vel = 5
key = 0
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
    if key == pygame.K_RIGHT:
        x += vel
    if key == pygame.K_UP:
        y -= vel
    if key == pygame.K_DOWN:
        y += vel

    window.fill((0, 0, 0))  # Fills the screen with black
    pygame.draw.ellipse(window, (255, 234, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()
