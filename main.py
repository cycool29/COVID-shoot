# Import the pygame module
import pygame

# Initialize pygame module
pygame.init()

# Create screen
screen_size = 800, 600
screen = pygame.display.set_mode(screen_size)

# Create window title and icon
pygame.display.set_caption("COVID-shoot")
window_icon = pygame.image.load("covid_icon.bmp")
pygame.display.set_icon(window_icon)

# Create hand sanitizer
sanitizer = pygame.image.load("sanitizer.bmp")

# Position of sanitizer
# y -= number (up), y += number (down)
# x -= number (left), y += number (right)
sanitizer_x = 370
sanitizer_y = 480

# Movement of sanitizer to be added to sanitizer_x and sanitizer_y
sanitizer_x_move = 0
sanitizer_y_move = 0

# Create enemy (COVID)
enemy = pygame.image.load("covid_icon.bmp")
enemy_x = 370
enemy_y = 480

# Movement of sanitizer to be added to sanitizer_x and sanitizer_y
enemy_x_move = 0
enemy_y_move = 0


# Position of enemy

# Define function to show and control sanitizer
def sanitizer_control(x, y):
    screen.blit(sanitizer, (x, y))


# Create simple game loop
running = True
while running:
    # Red Green Blue
    screen.fill((0, 255, 0))
    # Check if use click x button of the window. If true, exit game.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # User control to the sanitizer
        # When user pressing key, check what key that user pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                sanitizer_x_move -= 2
            if event.key == pygame.K_RIGHT:
                sanitizer_x_move += 2
            if event.key == pygame.K_DOWN:
                sanitizer_y_move += 2
            if event.key == pygame.K_UP:
                sanitizer_y_move -= 2

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                sanitizer_x_move = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                sanitizer_y_move = 0

    sanitizer_x += sanitizer_x_move
    sanitizer_y += sanitizer_y_move

    if sanitizer_x <= -10:
        sanitizer_x = -10
    elif sanitizer_x >= 750:
        sanitizer_x = 750
    if sanitizer_y <= 0:
        sanitizer_y = 0
    elif sanitizer_y >= 525:
        sanitizer_y = 525

    sanitizer_control(sanitizer_x, sanitizer_y)
    pygame.display.update()
