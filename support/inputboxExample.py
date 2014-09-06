#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

# by Timothy Downs, inputbox written for my map editor

# Edited to be python3 compatible by @SteveClement on Twitter
# Example version is with additional comments

# This program needs a little cleaning up
# It ignores the shift key
# And, for reasons of my own, this program converts "-" to "_"

# A program to get user input, allowing backspace etc
# shown in a box in the middle of the screen
#
# Called by:
#
# import inputboxExample
# answer = inputbox.ask(screen, "Your name")
#
# Only near the center of the screen is blitted to
#
# Obviously inputboxExample.py needs to be in the same directory you started you python from

import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *

def get_key():
  while True:
    event = pygame.event.poll()
    if event.type == KEYDOWN:
      return event.key
    else:
      pass

def display_box(screen, message):
  "Print a message in a box in the middle of the screen, no font selected, no fancy colors"
  fontobject = pygame.font.Font(None,18)
  # Draw a RED (r255,g0,b0) rectangle
  pygame.draw.rect(screen, (255,0,0),
                   ((screen.get_width() / 2) - 100,
                    (screen.get_height() / 2) - 10,
                    200,20), 0)
  # Draw a GREEN (r0,g255,b0) rectangle
  pygame.draw.rect(screen, (0,255,0),
                   ((screen.get_width() / 2) - 102,
                    (screen.get_height() / 2) - 12,
                    204,24), 1)
  if len(message) != 0:
  	# blit a WHITE (r255,g255,b255) fontobject with the contents of the message variable to the screen where we can enter Text
    screen.blit(fontobject.render(message, 1, (255,255,255)),
                ((screen.get_width() / 2) - 100, (screen.get_height() / 2) - 10))
  pygame.display.flip()

def ask(screen, question):
  "ask(screen, question) -> answer"
  # Init font engine
  pygame.font.init()
  current_string = []
  # call display_box() function
  display_box(screen, question + ": " + "".join(current_string))
  # Main endless loop untill we press the Return/Enter key (K_RETURN)
  while True:
  	# Get pressed key
    inkey = get_key()
    # Check what key was pressed
    if inkey == K_BACKSPACE:
      # remove one character from current_string
      current_string = current_string[0:-1]
    elif inkey == K_RETURN:
      break
    elif inkey == K_MINUS:
      # appent an underscore if minus (-) entered
      current_string.append("_")
    elif inkey <= 127:
      # All other characters get appended to current_string
      current_string.append(chr(inkey))
    # Add characters to current_string and display them on the screen  
    display_box(screen, question + ": " + "".join(current_string))
  # Once enter pressed return the contents of current string
  return "".join(current_string)

def main():
  # set the screen size to 320x240
  screen = pygame.display.set_mode((320,240))
  # Print the return value of the function ask()
  print((ask(screen, "Please type your Name") + " was entered"))

if __name__ == '__main__': main()
