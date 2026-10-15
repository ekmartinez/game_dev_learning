import pygame

class Circle:                                              # Very helpful
    def __init__(self, pos) -> None:
        self.posx = pos[0]
        self.posy = pos[1]
        self.radius = 20
        self.color = "blue"

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, self.color, (self.posx, self.posy), self.radius)

def main():
    size = (300, 600)                                     # Screen size
    pygame.init()
    window = pygame.Window(
        size=size,
        title = "Particle Swarm",
        position = (10, 50))
    screen = window.get_surface()

    clock = pygame.time.Clock()
    circles = []                                         # Container for circles

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if pygame.mouse.get_pressed()[0]:           # Left mouse button?
                circles.append(Circle(pygame.mouse.get_pos()))

            screen.fill("white")
            for p in circles:
                p.draw(screen)

            window.flip()
            clock.tick(60)
    pygame.quit()

if __name__ == "__main__":
    main()
