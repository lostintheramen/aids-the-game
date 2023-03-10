import pygame, sys

pygame.init()

screen_width = 640
screen_height = 480

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

colors = {
    'slate': '#11192A'
}

image = pygame.image.load("assets/aids.png")

pos = image.get_rect()

pos.x = screen_width // 2
pos.y = screen_height // 2

speed = 4

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        pos.y -= speed
    if keys[pygame.K_s]:
        pos.y += speed
    if keys[pygame.K_a]:
        pos.x -= speed
    if keys[pygame.K_d]:
        pos.x += speed

    pygame.display.set_caption("AIDS: The game")
    screen.fill(colors["slate"])

    scaled_image = pygame.transform.scale(image, (image.get_width() * 3, image.get_height() * 3))
    screen.blit(scaled_image, pos)

    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)











