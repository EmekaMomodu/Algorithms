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
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the font
font = pygame.font.Font(None, 36)

# Set up the clock
clock = pygame.time.Clock()

# Set up the disks
n = 4
disks = [i for i in range(n, 0, -1)]

# Set up the towers
towers = {
    'A': disks[:],
    'B': [],
    'C': []
}

# Set up the selected disk and tower
selected_disk = None
selected_tower = None

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the position of the mouse click
            pos = pygame.mouse.get_pos()

            # Check if a disk was clicked
            for tower, disks in towers.items():
                for i, disk in enumerate(disks):
                    # Calculate the position of the disk
                    disk_x = (WIDTH // 3) * (ord(tower) - ord('A')) + (WIDTH // 6)
                    disk_y = HEIGHT - (i + 1) * 50

                    # Check if the mouse click was within the disk
                    if (disk_x - 25 < pos[0] < disk_x + 25) and (disk_y - 25 < pos[1] < disk_y + 25):
                        # Select the disk and tower
                        selected_disk = disk
                        selected_tower = tower

            # Check if a tower was clicked
            for i, tower in enumerate(towers.keys()):
                # Calculate the position of the tower
                tower_x = (WIDTH // 3) * i + (WIDTH // 6)
                tower_y = HEIGHT - 50

                # Check if the mouse click was within the tower
                if (tower_x - 25 < pos[0] < tower_x + 25) and (tower_y - 25 < pos[1] < tower_y + 25):
                    # Move the selected disk to the tower
                    if selected_disk is not None and selected_tower is not None:
                        # Check if the move is valid
                        if selected_tower != tower and (not towers[tower] or selected_disk < towers[tower][-1]):
                            # Move the disk
                            towers[selected_tower].remove(selected_disk)
                            towers[tower].append(selected_disk)

                            # Reset the selected disk and tower
                            selected_disk = None
                            selected_tower = None

    # Draw the background
    screen.fill(WHITE)

    # Draw the towers
    for i, tower in enumerate(towers.keys()):
        # Calculate the position of the tower
        tower_x = (WIDTH // 3) * i + (WIDTH // 6)
        tower_y = HEIGHT - 50

        # Draw the tower
        pygame.draw.rect(screen, BLACK, (tower_x - 25, tower_y - 25, 50, 50))

        # Draw the disks
        for j, disk in enumerate(towers[tower]):
            # Calculate the position of the disk
            disk_x = tower_x
            disk_y = tower_y - (j + 1) * 50

            # Draw the disk
            pygame.draw.rect(screen, RED, (disk_x - 25, disk_y - 25, 50, 50))

            # Draw the disk number
            text = font.render(str(disk), True, BLACK)
            screen.blit(text, (disk_x - 10, disk_y - 10))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)