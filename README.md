# RetroPie Scripting Fun

The RetroPie is pretty awesome on it's own...

But when it's tossed into a gameboy case, all sorts of fun takes off!

I started this as a way of adding scripts tot the RetroPie installation for the `Circuit Sword`.


## Adding a `scripts` GUI entry to the RetroPie

I losely followed these directions: https://retropie.org.uk/docs/Add-a-New-System-in-EmulationStation/

Copy `es_systems.cfg` OUT of `/etc/` first (And remember to update it when you update retropie!):

```
sudo cp /etc/emulationstation/es_systems.cfg /opt/retropie/configs/all/emulationstation/es_systems.cfg.
```

Add something like this to `es_systems.cfg`

```
  <system>
    <name>Scripts</name>
    <fullname>Custom Scripts</fullname>
    <path>/home/pi/RetroPie/scripts</path>
    <extension>.sh .py</extension>
    <command>%ROM%</command>
    <platform/>
    <theme>system</theme>
  </system>
```

Then, after a reboot (or restarting EmulationStation itself) any `.sh` or `.py` scripts in the 
`/home/pi/RetroPie/scripts` directory will be listed as "games" under the `Scripts` emulator entry in the GUI!


## Installing the scripts

Start with following the directions further down on getting the GUI menu setup first...

Then, move the scripts all (or some) of the scripts in this repo into the right place for Emulation station to pick em 
up:

```
mkdir ~/RetroPie/scripts
cp ./scripts/* ~/RetroPie/scripts/
```

Then reboot RetroPie (Note: EmulationStation ONLY starts correctly ON THE DEVICE! Don't run `kill emulationstation`. 
Just reboot the thing.)


## Writing your own scripts:

You'll probably want to install pip on the machine before you get too far:

```
sudo apt-get install python-pip
pip install pysdl2
```

And it's worth knowing that scripts MUST have the correct hash-bang at the beginning of the file in order to work 
correctly:

```
#!/usr/bin/python
```

### Quiting gracefully: The Joystick and Button Example

The first thing you'll want your script to do is be able to exit cleanly! Either you can just let the script run until it finishes... Or you can hook into the standard controller inputs and do something reasonable from there.

*Note: I do not know how the buttons work on other RetroPie's! I only have the Circuit Sword to test with!*

```

```

### SDL Example

Here is a `main.py` that draws an sdl window (I put it in `/home/pi/RetroPie/scripts/main.py`). Use `chmod +x main.py` 
to make sure you can run it...

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

from sdl2 import *

X = SDL_WINDOWPOS_UNDEFINED
Y = SDL_WINDOWPOS_UNDEFINED
W = 960
H = 540
FLAGS = SDL_WINDOW_SHOWN

# There are more pythonic ways of doing this, by using the sdl2.ext module.

def main():
    SDL_Init(SDL_INIT_VIDEO)

    win = SDL_CreateWindow(b"Hello World!", X, Y, W, H, FLAGS)
    ren = SDL_CreateRenderer(win, -1, SDL_RENDERER_ACCELERATED | SDL_RENDERER_PRESENTVSYNC)
    bmp = SDL_LoadBMP(b"../img/boxes.bmp")
    tex = SDL_CreateTextureFromSurface(ren, bmp)
    SDL_FreeSurface(bmp)

    for i in range(20):
        SDL_RenderClear(ren)
        SDL_RenderCopy(ren, tex, None, None)
        SDL_RenderPresent(ren)
        SDL_Delay(100)

    SDL_DestroyTexture(tex)
    SDL_DestroyRenderer(ren)
    SDL_DestroyWindow(win)
    SDL_Quit()

if __name__ == "__main__":
    main()
```



