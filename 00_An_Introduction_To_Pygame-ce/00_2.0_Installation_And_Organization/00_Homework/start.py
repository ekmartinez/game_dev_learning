"""
2.1.4 Homework

Please have a look at https://pyga.me/docs/ref/window.html and then try to solve the

following small exercises:

[Done] 1. Set up a working environment for your game programming. Install Python, your
preferred editor, and the latest Pygame-ce version. Open the directory containing
your Pygame source code and try to run start01.py.

[Done] 2. Change the background color of the window. Use RGB values as well as named
colors.

[Done] 3. Change the size of the window.

[Done] 4. Change the position of the window. Use position values and also try WINDOWPOS-
_CENTERED and WINDOWPOS_UNDEFINED .

[Done] 5. Create the window as a resizable window and try to resize it.

[Done] 6. Define a minimum and maximum window size, show the actual size in the title
bar, and try to resize the window to its limits.

[Done] 7. Show the actual window position in the title bar.

[Done] 8. Play a little bit with the opacity attribute of the window.

[Done] 9. Change the title of the window during runtime according to a counter. Shut down
the program if counter is greater 600.

[Done] 10. Create a borderless window.

[Done] 11. Try a fullscreen window.

[Done] 12. Try to arrange three windows in a row. Compute the x-position of the second and
third window based on the window size and a useful gap between them. (Done in start2.py)
"""

import pygame

def main():
    pygame.init()

    window = pygame.Window(
        "Pygame Homework",
        size=(400, 600),
        resizable=True,                            # Requirement 5
        borderless=True,                           # Requirement 10
    )
    window.set_fullscreen(True)                    # Requirement 11

    window.opacity = 0.5                           # Requirement 8 (Doesn't work on x11)

    window.minimum_size = (300, 400)               # Requirement 6
    window.maximum_size = (800, 1000)              # Requirement 6

    screen = window.get_surface()

    #window.position = (10, 50)                    # Requirement 4
    #window.position = pygame.WINDOWPOS_UNDEFINED  # Requirement 4
    window.position = pygame.WINDOWPOS_CENTERED    # Requirement 4

    # screen = pygame.display.set_mode((400,600))
    # pygame.display.set_caption("Window by Display Module")

    running = True
    counter = 0
    while running:                                  
        for event in pygame.event.get():            
            if event.type == pygame.QUIT:           
                running = False


        counter += 1                            # Requirement 9
        window.title = f"Counter: {counter}"    # Requirement 9

        if counter > 600:                       # Requirement 9
            running = False                     # Requirement 9

        #time.sleep(1)
        #width, height = window.size                        # Requirement 6
        #x, y = window.position                             # Requirement 6

        #window.title = f"Window Size: {width} x {height} | Postition ({x}, {y})"  # Requirement 6, 7


        screen = window.get_surface()
        
        screen.fill("green")           # Requirement 2
        # screen.fill((0, 255, 0))     # Requirement 2
        window.flip()
        # pygame.display.flip()
    pygame.quit()                                   

if __name__ == "__main__":
    main()

