

import pygame

def main():
    pygame.init()

    first_window = pygame.Window(
        "First Window",
        size=(400, 600),
        position=(100, 50)
    )
    second_window = pygame.Window(
        "Second Window",
        size=(400, 600),
        position=(525, 50)
    )

    third_window = pygame.Window(
        "Third Window",
        size=(400, 600),
        position=(950, 50)
    )
    first_screen = first_window.get_surface()
    second_screen = second_window.get_surface()
    third_screen = third_window.get_surface()

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.WINDOWCLOSE:
                running = False
                event.window.destroy()
        if running:
            first_screen.fill("red")
            first_window.flip()
            second_screen.fill("green")
            second_window.flip()
            third_screen.fill("blue")
            third_window.flip()

            clock.tick(60)
    pygame.quit()

if __name__ == "__main__":
    main()
