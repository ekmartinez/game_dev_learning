import pygame # Pygame Module (also for pygame-ce!)

def main():
    pygame.init()                                     # Starts subsystem
    window = pygame.Window(size=(600, 400))           # Create Window
    window.title = "My first Pygame Program"          # Set window title
    window.position = (10, 50)                        # Set window position
    screen = window.get_surface()                     # Get the window's bitmap surface
    clock = pygame.time.Clock()

    running = True
    while running:                                    # Main program loop: start
        for event in pygame.event.get():              # Retrieve events
            if event.type == pygame.QUIT:             # Window X clicked?
                running = False
        screen.fill((0, 255, 0))                      # Fill playground
        window.flip()                                 # Swap double buffer
        clock.tick(60)

    pygame.quit()                                     # Shut down subsystem

if __name__ == "__main__":
    main()

# Result after adding a frame limit:
# clock = pygame.time.Clock() and clock.tick(60) in the loop.
# htop now shows about 9-10% CPU, down from about 100%.
# The loop still runs 60 times per second, so some CPU is used for
# redrawing and event handling.
