# COVID-shoot

A game build with Python using [pygame](https://pygame.org) module to shoot COVID-19 with sanitizer.

## Usage

### Prerequisites

To run, you will need [pygame](https://pygame.org) and [pygame-menu](https://pygame-menu.readthedocs.io/) modules. To install them, run:
``` 
pip3 install pygame pygame-menu
```

### Install

On Windows, [Download the zip](https://github.com/cycool29/COVID-shoot/archive/refs/heads/main.zip) and extract it.

On Linux, clone the repo:
```
git clone https://github.com/cycool29/COVID-shoot
cd COVID-shoot
```

Launch `menu.py` by double click it or in command-line:
```
python3 ./menu.py
```

Now you should be presented with this screen:

![image](https://user-images.githubusercontent.com/88134003/139528488-c7c2c91c-3f85-4691-be25-a8f18fedca6c.png)

- **Play** - As its name suggests, click this button to start the game.
- **Settings** - Control game settings there. Currently only COVID moving speed.
- **Help** - Instructions on how to play the game.
- **Quit** - Exit the game.

When you click Play, after a 3 secs countdown, the game started and enjoy!

![image](https://user-images.githubusercontent.com/88134003/139528562-e500e048-f13c-460b-90bf-f7ed86054580.png)


Don't let the COVIDs hit the red line! 

![image](https://user-images.githubusercontent.com/88134003/139528575-09b3fac3-a8cf-4874-9735-909782f8117b.png)


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
