import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up the display
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Towers of Hanoi")

# Set up the font
font = pygame.font.Font(None, 30)

# Set up the disks
n = 4
disks = []
for i in range(n, 0, -1):
    disks.append({"width": 100 - (n - i) * 20, "height": 20, "x": 150 - (100 - (n - i) * 20) / 2, "y": HEIGHT - 50 - (n - i) * 25, "pole": 1})

# Set up the poles
poles = [{"x": 150, "y": HEIGHT - 50}, {"x": WIDTH / 2, "y": HEIGHT - 50}, {"x": WIDTH - 150, "y": HEIGHT - 50}]

# Set up the selected disk
selected_disk = None

# Game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for disk in disks:
                if disk["x"] < event.pos[0] < disk["x"] + disk["width"] and disk["y"] < event.pos[1] < disk["y"] + disk["height"]:
                    selected_disk = disk
        elif event.type == pygame.MOUSEBUTTONUP:
            if selected_disk:
                for pole in poles:
                    if pole["x"] - 50 < event.pos[0] < pole["x"] + 50 and pole["y"] - 100 < event.pos[1] < pole["y"]:
                        selected_disk["pole"] = poles.index(pole) + 1
                        selected_disk["x"] = pole["x"] - selected_disk["width"] / 2
                        selected_disk["y"] = pole["y"] - 25
                        for disk in disks:
                            if disk != selected_disk and disk["pole"] == selected_disk["pole"]:
                                if disk["y"] < selected_disk["y"]:
                                    disk["y"] += 25
                        disks.sort(key=lambda x: (x["pole"], -x["width"]))
                        for i, disk in enumerate(disks):
                            disk["y"] = HEIGHT - 50 - i * 25
                selected_disk = None

    # Draw everything
    win.fill(WHITE)
    for pole in poles:
        pygame.draw.line(win, BLACK, (pole["x"], pole["y"]), (pole["x"], pole["y"] - 200), 5)
    for disk in disks:
        pygame.draw.rect(win, RED, (disk["x"], disk["y"], disk["width"], disk["height"]))
    text = font.render("Towers of Hanoi", True, BLACK)
    win.blit(text, (WIDTH / 2 - text.get_width() / 2, 20))

    # Update the display
    pygame.display.update()

    # Cap the frame rate
    pygame.time.delay(1000 // 60)