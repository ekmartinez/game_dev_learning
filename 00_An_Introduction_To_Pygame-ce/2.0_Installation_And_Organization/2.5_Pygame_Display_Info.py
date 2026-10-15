import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode([200, 200])
    info = pygame.display.Info() # pygame.display.get_wm_info()
    pygame.display.message_box("Window System Information", repr(info), "info")
    pygame.quit()

if __name__ == "__main__":
    main()

# Creating the window with pygame.Window (the newer API in pygame-ce).
# This is the approach the textbook uses in its first examples. The
# author later added pygame.display.set_mode() because some readers
# had problems with it on Linux systems running Wayland.
#
# pygame.Window(size=(600, 400)) creates the window. We set the title
# and position as properties, and window.get_surface() returns the
# Surface we draw on.
#

