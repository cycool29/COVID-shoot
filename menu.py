import main
import pygame
import pygame_menu

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


# Create theme and use covid as background
theme = pygame_menu.themes.THEME_DARK.copy()
theme.background_color = background


# Simple help section
def help_menu():
    help_page = pygame_menu.Menu('Help', 800, 600, theme=theme)
    help_text = f"Use RIGHT key and LEFT key to move the hand sanitizer right and left. \nPress SPACE to shoot a " \
                f"droplet.\n "
    help_page.add.label(help_text, max_char=-1, font_size=20)
    help_page.add.button('Return to Main menu', action=main_menu)
    help_page.mainloop(surface)


def main_menu():
    menu = pygame_menu.Menu('Covid-shoot', 800, 600, theme=theme)
    menu.add.button('Play', action=play)
    menu.add.button('How to play?', action=help_menu)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(surface)


# Run the program
main_menu()
