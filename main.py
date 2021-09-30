# Import the pygame module
import pygame
import random

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
covid = pygame.image.load("covid_icon.bmp")

# Position
# y -= number (up), y += number (down)
# x -= number (left), y += number (right)
covid_x = random.randint(10, 800)
covid_y = random.randint(50, 150)

# Movement of sanitizer to be added to sanitizer_x and sanitizer_y
covid_x_move = 3
covid_y_move = 0.1

# Create hand enemy (COVID)
droplets = pygame.image.load("water_drops.bmp")

# Position
# y -= number (up), y += number (down)
# x -= number (left), y += number (right)
droplets_x = 0
droplets_y = 480

# Bullet state - ready = store in sanitizer ( unable to see it)
#                shoot = shooting to COVID ( able to see )
droplets_state = "ready"

# Movement of sanitizer to be added to sanitizer_x and sanitizer_y
droplets_x_move = 0
droplets_y_move = 10


# Define function to show and control sanitizer
def sanitizer_control(x, y):
    screen.blit(sanitizer, (x, y))


# Define function to show and control COVID
def covid_control(x, y):
    screen.blit(covid, (x, y))


def shoot(x, y):
    global droplets_state
    droplets_state = "shoot"
    screen.blit(droplets, (x, y))


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
                sanitizer_x_move -= 10
            if event.key == pygame.K_RIGHT:
                sanitizer_x_move += 10
            if event.key == pygame.K_SPACE:
                if droplets_state is "ready":
                    droplets_x = sanitizer_x
                    shoot(droplets_x, droplets_y)

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

    covid_x += covid_x_move
    covid_y += covid_y_move

    if covid_x <= -10:
        covid_x_move = 3
        covid_y += covid_y_move
    elif covid_x >= 750:
        covid_x_move = -3

    if droplets_y <= 0:
        droplets_state = "ready"
        droplets_y = 480

    if droplets_state == "shoot":
        shoot(droplets_x, droplets_y)
        droplets_y -= droplets_y_move

    sanitizer_control(sanitizer_x, sanitizer_y)
    covid_control(covid_x, covid_y)
    pygame.display.update()
