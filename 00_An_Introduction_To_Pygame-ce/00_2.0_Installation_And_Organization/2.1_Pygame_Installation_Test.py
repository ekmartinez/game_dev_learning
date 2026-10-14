import pygame

def main():
    pygame.init()
    window = pygame.Window(size=(400, 100))
    window.title = "Pygame test"
    screen = window.get_surface()
    clock = pygame.time.Clock()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill("white")
        window.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
