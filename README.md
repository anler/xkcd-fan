## About
---
This is a little program that when invoked with a given directory path as its parameter, it fetchs a random comic from xkcd's website and saves it into that directory.
I use it in my Mac in conjunction with GeekTool and Automator to set a random comic as my desktop's background each time I do a system reboot.

![My desktop](http://f.cl.ly/items/3k2E1s0F1Z1I1H1a3746/xkcd-mydesktop.png)

## Installation
---
1. Install [GeekTool](http://projects.tynsoe.org/en/geektool/) 
2. Download xkcd_fan.py script
3. Open GeekTool and create an Image Geeklet in your desktop. Set __URL__ to the directory where you will save the comics and check __Pick random image in directory__

With that in place, all that's left to do is create an __Automator__ application:

1. Open Automator and choose new Application workflow
2. Drag a "Run Shell Script" action to the workflow area in the right
3. Set the __Shell__ drop-down to __/bin/bash__ and the __Pass Input__ drop-down to __as arguments__
4. Clear the text in the text box and write something like this (but using your own paths): __/path/to/python3 /path/to/xkcd_fan.py /destination/directory__
5. __Save__ it and test it running it clicking in the _play_ button in the up-right corner
6. Then, from the __System Preferences__ >> __User & Groups__ >> __Login Items__ click in the __+__ button and navigate to and select your new Automator application.

## TODO
---
Only compatible with Python 3 right now but is not particulary hard adapt it so that works in Python 2 too.