import pygame
import pygame_menu

import main

# Initialize pygame
pygame.init()
surface = pygame.display.set_mode((800, 600))

window_icon = pygame.image.load("covid_icon.bmp")
pygame.display.set_icon(window_icon)

# Create background image
background = pygame_menu.baseimage.BaseImage(
    image_path="covid-background.jpg",
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_SIMPLE
)


# main function
def play():
    # Add 321 countdown
    window = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('Quicksand-SemiBold.ttf', 100)
    counter = 3
    text = font.render(str(counter), True, (255, 0, 0))
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
                text = font.render(str(counter), True, (255, 0, 0))
                if counter == 0:
                    pygame.time.set_timer(timer_event, 0)
                    run = False
                    main.main_loop()
                    # run = False
        # Fill screen in black
        window.fill((0, 0, 0))
        text_rect = text.get_rect(center=window.get_rect().center)
        window.blit(text, text_rect)
        pygame.display.flip()


# Create theme
theme = pygame_menu.themes.THEME_DARK.copy()
theme.title_font = pygame_menu.font.FONT_NEVIS
theme.widget_font = pygame_menu.font.FONT_OPEN_SANS_BOLD
theme.background_color = background
theme.title_background_color = (255, 0, 0)
theme.title_font_size = 40

items = [('Default', "Default"),
         ('Fast', "Fast"),
         ('Slow', "Slow"),
         ('Very fast', "Very fast")]


def settings_menu():
    settings_page = pygame_menu.Menu('Game settings', 800, 600, theme=theme)
    settings_page.add.selector(
        title="Choose COVID's speed: ",
        items=items,
        style=pygame_menu.widgets.SELECTOR_STYLE_FANCY,
        style_fancy_bgcolor=(255, 0, 0),
        default=main.covid_speed_default,
        onchange=main.set_covid_speed
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
    about_text_2 = "I have chosen Python as the language to use in this project because it is much more friendly to a " \
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
