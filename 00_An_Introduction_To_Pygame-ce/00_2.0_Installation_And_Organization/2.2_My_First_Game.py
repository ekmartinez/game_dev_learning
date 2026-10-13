import pygame # Pygame Module (also for pygame-ce!)

def main():
    pygame.init()                                     # Starts subsystem
    window = pygame.Window(size=(600, 400))           # Create Window
    window.title = "My first Pygame Program"          # Set window title
    window.position = (10, 50)                        # Set window position
    screen = window.get_surface()                     # Get the window's bitmap surface

    running = True
    while running:                                    # Main program loop: start
        for event in pygame.event.get():              # Retrieve events
            if event.type == pygame.QUIT:             # Window X clicked?
                running = False
        screen.fill((0, 255, 0))                      # Fill playground
        window.flip()                                 # Swap double buffer

    pygame.quit()                                     # Shut down subsystem

if __name__ == "__main__":
    main()

# Lesson: Resource usage of a loop with no frame limit
# Date: 2026-10-13
# Observation: The main loop has no frame limit, so it runs as fast as
# the CPU allows. htop showed CPU usage near 100%.
# This is the baseline for the next lesson, which adds a frame limit
# with pygame.time.Clock().tick(60) to reduce CPU use.
