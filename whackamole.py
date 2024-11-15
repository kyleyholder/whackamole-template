import pygame
import random

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        x = 0
        y = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill("light green")
            for i in range(20):
                pygame.draw.line(screen, "black", (i * 32, 0), (i * 32, 512))
            for i in range(16):
                pygame.draw.line(screen, "black", (0, i * 32), (640, i * 32))
            screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if x - 32 <= event.pos[0] <= x + 32 and y - 32 <= event.pos[1] <= y + 32:
                    x = random.randrange(0, 640, 32)
                    y = random.randrange(0, 512, 32)
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
