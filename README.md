# shooting-game

A game build with Python using [pygame](https://pygame.org) module to shoot COVID-19 with sanitizer.

## Usage

### Prerequisites

To run, you will need [pygame](https://pygame.org) and [pygame-menu](https://pygame-menu.readthedocs.io/) modules. To install them, run:
``` 
pip3 install pygame pygame-menu
```
### Walk-through

Now clone the repo, and launch `menu.py`.
```
git clone https://github.com/cycool29/shooting-game
cd shooting-game
python3 ./menu.py
```

Now you should be presented with this screen:

![image](https://user-images.githubusercontent.com/88134003/138396670-9c0e85de-b623-48d6-b86e-28265c71aa94.png)

- **Play** - As its name suggests, click this button to start the game.
- **How to play** - Instructions on how to play the game.
- **Quit** - Exit the game.

So, let's click Play, after a 3 secs countdown, the game started and enjoy!

![image](https://user-images.githubusercontent.com/88134003/138398555-8e17dbd0-84d0-42a9-9c89-f99a276e2c5f.png)


## To-do

See the [project page](https://github.com/cycool29/shooting-game/projects/1).


## Known bugs and common fixes

Look here before open an issue.

- `NotImplementedError: font module not available` 

  Install `libsdl2-ttf-2.0-0` using `sudo apt install libsdl2-ttf-2.0-0` in Linux Debian-flavor distros. Please open an issue if you got this error in Windows or   MacOS.

- `ImportError: No module named PIL`

  Install `Pillow` module using `pip3 install Pillow`

- `NotImplementedError: mixer module not available`

  Install PySDL2 using `pip3 install PySDL2`


## Contributing

You may just [run the code](https://github.com/cycool29/shooting-game/new/main?readme=1#usage), and [open a new issue](https://github.com/cycool29/shooting-game/issues/new) to let me know bugs and where to improve !
