import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 600)) # Create window
    pygame.display.set_caption("Window by Display Module") # Set window title

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("white")
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
