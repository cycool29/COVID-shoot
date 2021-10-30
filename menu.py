import pygame
import pygame_menu
import math
import random
from settings import *

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
sanitizer_y = 500

# Movement of sanitizer to be added to sanitizer_x and sanitizer_y
sanitizer_x_move = 0
sanitizer_y_move = 0

covid = []
covid_x = []
covid_y = []
covid_y_move = []
covid_x_move = []
covid_num = 6

# Covid settings
# noinspection PyUnboundLocalVariable
if covid_speed_type == "Default":
    covid_speed_default = 0
    covid_x_speed_between_a = 2
    covid_x_speed_between_b = 5
    covid_y_speed_between_a = 0.05
    covid_y_speed_between_b = 0.1
elif covid_speed_type == "Fast":
    covid_speed_default = 1
    covid_x_speed_between_a = 4
    covid_x_speed_between_b = 7
    covid_y_speed_between_a = 0.1
    covid_y_speed_between_b = 0.15
elif covid_speed_type == "Slow":
    covid_speed_default = 2
    covid_x_speed_between_a = 1
    covid_x_speed_between_b = 4
    covid_y_speed_between_a = 0.01
    covid_y_speed_between_b = 0.05
elif covid_speed_type == "Very fast":
    covid_speed_default = 3
    covid_x_speed_between_a = 6
    covid_x_speed_between_b = 9
    covid_y_speed_between_a = 0.2
    covid_y_speed_between_b = 0.25

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

over_font = pygame.font.Font('Quicksand-SemiBold.ttf', 64)


def set_settings(speed):
    f = open("settings.py", "w")
    f.write(f"covid_speed_type = '{speed}'")
    f.close()


def set_covid_speed(selected_item, kwargs):
    global covid_x_speed_between_a
    global covid_x_speed_between_b
    global covid_y_speed_between_a
    global covid_y_speed_between_b
    global covid_y_move
    global covid_speed_default
    global covid_speed_type

    covid_speed_default = selected_item[1]

    set_settings(speed=kwargs)

    if kwargs == "Default":
        covid_speed_type = "Default"
        covid_speed_default = 0
        covid_x_speed_between_a = 2
        covid_x_speed_between_b = 5
        covid_y_speed_between_a = 0.05
        covid_y_speed_between_b = 0.1
    elif kwargs == "Fast":
        covid_speed_type = "Fast"
        covid_speed_default = 1
        covid_x_speed_between_a = 4
        covid_x_speed_between_b = 7
        covid_y_speed_between_a = 0.1
        covid_y_speed_between_b = 0.15
    elif kwargs == "Slow":
        covid_speed_type = "Slow"
        covid_speed_default = 2
        covid_x_speed_between_a = 1
        covid_x_speed_between_b = 4
        covid_y_speed_between_a = 0.01
        covid_y_speed_between_b = 0.05
    elif kwargs == "Very fast":
        covid_speed_type = "Very fast"
        covid_speed_default = 3
        covid_x_speed_between_a = 6
        covid_x_speed_between_b = 9
        covid_y_speed_between_a = 0.2
        covid_y_speed_between_b = 0.25

    reset_covid()


def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (0, 255, 0))
    screen.blit(score, (x, y))


def game_over():
    over_text = over_font.render("GAME OVER ...", True, (255, 0, 0))
    over_caption = font.render("Press Esc to exit.", True, (255, 0, 0))
    screen.blit(over_text, (200, 200))
    screen.blit(over_caption, (270, 280))


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


def reset_covid():  # Reset covid stats after game over and exit
    global covid
    global covid_x
    global covid_y
    global covid_y_move
    global covid_x_move
    covid = []
    covid_x = []
    covid_y = []
    covid_y_move = []
    covid_x_move = []
    for _ in range(covid_num):
        # Create enemy (COVID)
        covid.append(pygame.image.load("covid_icon.bmp"))

        # Position
        # y -= number (up), y += number (down)
        # x -= number (left), y += number (right)
        covid_x.append(random.randint(10, 800))
        covid_y.append(random.randint(50, 150))

        # Movement of sanitizer to be added to sanitizer_x and sanitizer_y
        covid_x_move.append(random.randint(covid_x_speed_between_a, covid_x_speed_between_b))
        covid_y_move.append(random.uniform(covid_y_speed_between_a, covid_y_speed_between_b))


reset_covid()


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

        background = pygame.image.load("background.png")

        screen.blit(background, (0, 0))
        # Check if use click x button of the window. If true, exit game.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                reset_covid()
                score_value = 0
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
                if event.key == pygame.K_ESCAPE:
                    reset_covid()
                    score_value = 0
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
            if covid_y[i] > 445:
                for j in range(covid_num):
                    covid_y[j] = 4000
                game_over()
                break

            covid_x[i] += covid_x_move[i]
            covid_y[i] += covid_y_move[i]

            if covid_x[i] <= -10:
                covid_x_move[i] = covid_x_move[i] * -1
                covid_y[i] += covid_y_move[i]
                covid_x[i] += covid_x_move[i]
            elif covid_x[i] >= 800:
                covid_x_move[i] = covid_x_move[i] * -1
                covid_y[i] += covid_y_move[i]
                covid_x[i] += covid_x_move[i]

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


# Initialize pygame
surface = pygame.display.set_mode((800, 600))

window_icon = pygame.image.load("covid_icon.bmp")
pygame.display.set_icon(window_icon)

# Create background image
menu_background = pygame_menu.baseimage.BaseImage(
    image_path="covid-background.jpg",
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_SIMPLE
)


# main function
def play():
    # Add 321 countdown
    window = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    counter = 3
    text = over_font.render(str(counter), True, (255, 0, 0))
    timer_event = pygame.USEREVENT + 1
    pygame.time.set_timer(timer_event, 1000)
    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == timer_event:
                counter -= 1
                text = over_font.render(str(counter), True, (255, 0, 0))
                if counter == 0:
                    pygame.time.set_timer(timer_event, 0)
                    run = False
                    main_loop()
        # Fill screen in black
        import settings
        window.fill((0, 0, 0))
        text_rect = text.get_rect(center=window.get_rect().center)
        window.blit(text, text_rect)
        pygame.display.flip()


# Create theme
theme = pygame_menu.themes.THEME_DARK.copy()
theme.title_font = pygame_menu.font.FONT_NEVIS
theme.widget_font = pygame_menu.font.FONT_OPEN_SANS_BOLD
theme.background_color = menu_background
theme.title_background_color = (255, 0, 0)
theme.title_font_size = 40

covid_speeds = [('Default', "Default"),
                ('Fast', "Fast"),
                ('Slow', "Slow"),
                ('Very fast', "Very fast")]


def settings_menu():
    settings_page = pygame_menu.Menu('Game settings', 800, 600, theme=theme)
    settings_page.add.selector(
        title="Choose COVID's speed: ",
        items=covid_speeds,
        style=pygame_menu.widgets.SELECTOR_STYLE_FANCY,
        style_fancy_bgcolor=(255, 0, 0),
        default=covid_speed_default,
        onchange=set_covid_speed
    )
    settings_page.add.button('Return to Main menu', action=main_menu)
    settings_page.mainloop(surface)


# Simple help section
def help_menu():
    help_page = pygame_menu.Menu('How to play', 800, 600, theme=theme)
    about_text = f"Use RIGHT key and LEFT key to move the hand sanitizer right and left. \nPress SPACE to shoot a " \
                 f"droplet.\n" \
                 f"Don't let the COVIDs hit the red line! "
    help_page.add.label(about_text, max_char=-1, font_size=20)
    help_page.add.button('Return to Main menu', action=main_menu)
    help_page.mainloop(surface)


def about():
    help_page = pygame_menu.Menu('About this project', 800, 600, theme=theme)
    about_text_1 = "This is my project for Coolest Project Malaysia competition.\n"
    about_text_2 = "I have chosen Python as the language to use in this project because it is much more friendly to a "\
                   "newbie to programming world than Unity or any other else programming languages or game engine. \n"
    about_text_3 = "I believe that Pygame module is capable to build a perfect 2D game in more simple way. "
    about_text_4 = "Project Github link: https://github.com/cycool29/COVID-shoot\n"

    help_page.add.label(about_text_1, max_char=-1, font_size=20)
    help_page.add.label(about_text_2, max_char=-1, font_size=20)
    help_page.add.label(about_text_3, max_char=-1, font_size=20)
    help_page.add.label(about_text_4, max_char=-1, font_size=20)
    help_page.add.button('Return to Main menu', action=main_menu)
    help_page.mainloop(surface)


def main_menu():
    menu = pygame_menu.Menu('COVID-shoot', 800, 600, theme=theme)
    menu.add.button('Play', action=play)
    menu.add.button('Settings', action=settings_menu)
    menu.add.button('Help', action=help_menu)
    menu.add.button("About", action=about)
    menu.add.button('Quit', action=pygame_menu.events.EXIT)
    menu.mainloop(surface)


# Run the program
main_menu()
