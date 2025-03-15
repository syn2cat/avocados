# BBQ Game Jam 2 game: The Mushy Tales of Avo The Cado

## tags: colored, voodoo, avocat, clicker, lawyer

## GameJam Keywords (based on which we chose the theme of the game): colored, voodoo, avocat (French for avocado and Lawyer, double entendre)

## Language: python3+pygame

## Tools and Hardware used: <a href="https://en.wikipedia.org/wiki/Wacom_(company)#Intuos" target="_blank">Wacom </a><a href="http://www.wacom.com/en/de/creative/intuos-pro-m">Tablet</a>/<a href="https://www.adobe.com/lu_en/products/photoshop.html" target="_blank">Photoshop CC</a>, <a href="https://en.wikipedia.org/wiki/Ableton_Live" target="_blank">Ableton Live</a><a href="https://www.ableton.com/en/push/" target="_blank">Push</a>, <a href="https://en.wikipedia.org/wiki/Sublime_Text" target="_blank">Sublime</a>, <a href="https://en.wikipedia.org/wiki/Canon_EOS_6D" target="_blank">Canon 6D</a>

## Team: <a href="https://twitter.com/kwisarts" target="_blank">@kwisarts</a>, <a href="https://twitter.com/rafi0t" target="_blank">@rafi0t</a>, <a href="https://twitter.com/SteveClement" target="_blank">@SteveClement</a> (Twitter)

## Plot
Imagine a world where Avo Cado could be free. A world where mushing around would be a thing of the past.
To the greater chagrin of our protagonist Avo The Cado the evil Voodoo Lawyers are behind her.
The Lawyers try to pin down every Avo Cado in existence, especially the pink ones.
Your mission, should you decide to accept it, is to be this bastard evil Voodoo lawyer and just end the life of all Avo Cado People around.

As every good Avo Cado hunter you have a Boss. Your Boss, Dr. Dredd, tells you what color of Avo Cado to go after.

Because of a stagnating economy you are ill equipped and can only afford hair pins to make a painful point on the Cado people.
Some would argue it even hurts more, but we are not here to discuss that.

Do not let the coloured guys go their way, or you will lose.

Make it past level3 and enter the evil psycho mode where Dr. Dredd wants to test your brain skills.
The only thing that changes is, READ the Color -> Click the Color…

<a href="https://www.youtube.com/watch?v=JfUM5xHUY4M" target="_blank">moua mouaahah mouahahahaha</a>

# Launch

Main launcher: game.py

# Requirements

## Installing py-game for python3

### OSX

* http://florian-berger.de/en/articles/installing-pygame-for-python-3-on-os-x/

#### Install HomeBrew

```
ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"
```

#### Install dependencies

```
brew install python3 mercurial git sdl sdl_image sdl_mixer sdl_ttf portmidi
brew tap homebrew/headonly
brew install --HEAD smpeg
/usr/local/bin/pip3 install hg+http://bitbucket.org/pygame/pygame
```

### Linux 

```bash
sudo apt-get install mercurial
sudo apt-get install python3-dev python3-numpy libsdl-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev libportmidi-dev libavformat-dev libswscale-dev libjpeg-dev libfreetype6-dev
hg clone https://bitbucket.org/pygame/pygame
cd pygame
python3 setup.py build
sudo python3 setup.py install
```

#### using pip (currently not working due to C90 non-compliance)
```bash
sudo apt-get install mercurial
sudo apt-get install python3-dev python3-numpy libsdl-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev libportmidi-dev libavformat-dev libswscale-dev libjpeg-dev libfreetype6-dev
pip install hg+https://bitbucket.org/pygame/pygame
```


### Windows (Currently failing on Windows 8.x numpy error)

* https://www.python.org/downloads/ (3.4.x)
* http://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame (3.4 compatible)

## Testing it all out

```
python3
>>> import pygame
>>> pygame.init()
(6, 0)
>>> pygame.display.set_mode((800, 600))
<Surface(800x600x32 SW)>
>>> raise SystemExit
```

## IDE (Integrated Development Environments)

* https://www.eclipse.org/downloads/ (Standard)
* http://pydev.org/download.html (Copy Paste Install plugin URL)

OR a standalone py-dev version called LiClipse (Beta as of August 2014)

* http://brainwy.github.io/liclipse/

## CodeEditors

* http://www.sublimetext.com
