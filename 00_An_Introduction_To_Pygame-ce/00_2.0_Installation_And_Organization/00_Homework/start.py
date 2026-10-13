"""
2.1.4 Homework

Please have a look at https://pyga.me/docs/ref/window.html and then try to solve the
following small exercises:

1. Set up a working environment for your game programming. Install Python, your
preferred editor, and the latest Pygame-ce version. Open the directory containing
your Pygame source code and try to run start01.py.

2. Change the background color of the window. Use RGB values as well as named
colors.

3. Change the size of the window.

4. Change the position of the window. Use position values and also try WINDOWPOS-
_CENTERED and WINDOWPOS_UNDEFINED .

5. Create the window as a resizable window and try to resize it.

6. Define a minimum and maximum window size, show the actual size in the title
bar, and try to resize the window to its limits.

7. Show the actual window position in the title bar.

8. Play a little bit with the opacity attribute of the window.

9. Change the title of the window during runtime according to a counter. Shut down
the program if counter is greater 600.

10. Create a borderless window.

11. Try a fullscreen window.

12. Try to arrange three windows in a row. Compute the x-position of the second and
third window based on the window size and a useful gap between them.
"""

import pygame

def main():
    pygame.init()                                   
    screen = pygame.display.set_mode((400,600))     # Create window§\label{srcStart0501}§
    pygame.display.set_caption("Window by Display Module") # Set window title§\label{srcStart0502}§

    running = True
    while running:                                  
        for event in pygame.event.get():            
            if event.type == pygame.QUIT:           
                running = False
        
        screen.fill("white")                        # Fill background with white§\label{srcStart0503}§
        pygame.display.flip()                       # Update display§\label{srcStart0504}§

    pygame.quit()                                   


if __name__ == "__main__":
    main()

