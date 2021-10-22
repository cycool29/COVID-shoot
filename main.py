# Import modules
import math
import random

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

covid = []
covid_x = []
covid_y = []
covid_y_move = []
covid_x_move = []
covid_num = 6

for each in range(covid_num):
    # Create enemy (COVID)
    covid.append(pygame.image.load("covid_icon.bmp"))

    # Position
    # y -= number (up), y += number (down)
    # x -= number (left), y += number (right)
    covid_x.append(random.randint(10, 800))
    covid_y.append(random.randint(50, 150))

    # Movement of sanitizer to be added to sanitizer_x and sanitizer_y
    covid_x_move.append(random.randint(5, 10))
    covid_y_move.append(random.uniform(0.1, 0.5))

# Create enemy (COVID)
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

# Score
score_value = 0
font = pygame.font.Font('Quicksand-SemiBold.ttf', 32)

text_x = 10
text_y = 10

help_x = 150
help_y = 100

hover_x = 20
hover_y = 10


def tooltips(x, y):
    tooltip = font.render(f"Use RIGHT and LEFT to move right and left the hand sanitizer. \nPress SPACE to shoot a "
                          f"droplet.\n Press Q to exit he game.\n", True, (0, 255, 0))
    screen.blit(tooltip, (x, y))


def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (0, 255, 0))
    screen.blit(score, (x, y))


# Define function to show and control sanitizer
def sanitizer_control(x, y):
    screen.blit(sanitizer, (x, y))


# Define function to show and control COVID
def covid_control(x, y, img):
    screen.blit(covid[img], (x, y))


def collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt((math.pow(enemy_x - bullet_x, 2)) + (math.pow(enemy_y - bullet_y, 2)))
    if distance < 27:
        return True
    else:
        return False


def shoot(x, y):
    global droplets_state
    droplets_state = "shoot"
    screen.blit(droplets, (x, y))


# Create simple game loop
def main_loop():  # Red Green Blue
    running = True
    while running:
        global screen_size
        global screen
        global sanitizer
        global sanitizer_x
        global sanitizer_y
        global sanitizer_x_move
        global sanitizer_y_move
        global covid
        global covid_x
        global covid_y
        global covid_y_move
        global covid_x_move
        global covid_num
        global droplets
        global droplets_x
        global droplets_y
        global droplets_state
        global droplets_x_move
        global droplets_y_move
        global score_value
        global font
        global text_y
        global text_x

        screen.fill((0, 0, 0))
        # Check if use click x button of the window. If true, exit game.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # User control to the sanitizer
            # When user pressing key, check what key that user pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    sanitizer_x_move -= 15
                if event.key == pygame.K_RIGHT:
                    sanitizer_x_move += 15
                if event.key == pygame.K_SPACE:
                    if droplets_state is "ready":
                        droplets_x = sanitizer_x
                        shoot(droplets_x, droplets_y)
                if event.key == pygame.K_q:
                    running = False

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

        for i in range(covid_num):

            covid_x[i] += covid_x_move[i]
            covid_y[i] += covid_y_move[i]

            if covid_x[i] <= -10:
                covid_x_move[i] = 10
                covid_y[i] += covid_y_move[i]
            elif covid_x[i] >= 750:
                covid_x_move[i] = -10
                covid_y[i] += covid_y_move[i]

            is_collision = collision(covid_x[i], covid_y[i], droplets_x, droplets_y)
            if is_collision:
                droplets_y = 480
                droplets_state = "ready"
                score_value += 1
                covid_x[i] = random.randint(0, 800)
                covid_y[i] = random.randint(50, 150)

            covid_control(covid_x[i], covid_y[i], i)

        if droplets_y <= 0:
            droplets_state = "ready"
            droplets_y = 480

        if droplets_state == "shoot":
            shoot(droplets_x, droplets_y)
            droplets_y -= droplets_y_move

        sanitizer_control(sanitizer_x, sanitizer_y)
        show_score(text_x, text_y)
        pygame.display.update()
