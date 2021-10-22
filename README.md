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

***Note: if you get `NotImplementedError: font module not available (ImportError: libSDL2_ttf-2.0.so.0: cannot open shared object file: No such file or directory)` error, install `libsdl2-ttf-2.0-0` using `sudo apt install libsdl2-ttf-2.0-0`***

***Note again: if you get `ImportError: No module named PIL` error, install `Pillow` module using `pip3 install Pillow`***


Now you should be presented with this screen:

![image](https://user-images.githubusercontent.com/88134003/138396670-9c0e85de-b623-48d6-b86e-28265c71aa94.png)

- **Play** - As its name suggests, click this button to start the game.
- **How to play** - Instructions on how to play the game.
- **Quit** - Exit the game.

So, let's click Play, after a 3 secs countdown, the game started and enjoy!

![image](https://user-images.githubusercontent.com/88134003/138398555-8e17dbd0-84d0-42a9-9c89-f99a276e2c5f.png)

## To-do

See the [project page](https://github.com/cycool29/shooting-game/projects/1).


## Contributing

You may just [run the code](https://github.com/cycool29/shooting-game/new/main?readme=1#usage), and [open a new issue](https://github.com/cycool29/shooting-game/issues/new) to let me know bugs and where to improve !
