""" Module for holding colour code values. """

import os
import re
import sys

try:
    # pylint: disable=F0401
    from colorama import Fore, Style
    has_colorama = True

except ImportError:
    has_colorama = False


mswin = os.name == "nt"

if mswin and has_colorama:
    white = Style.RESET_ALL
    ul = Style.DIM + Fore.YELLOW
    red, green, yellow = Fore.RED, Fore.GREEN, Fore.YELLOW
    blue, pink = Fore.CYAN, Fore.MAGENTA

elif mswin:
    ul = red = green = yellow = blue = pink = white = ""

elif sys.stdout.isatty():
    white = "\x1b[%sm" % 0
    ul = "\x1b[%sm" * 3 % (2, 4, 33)
    cols = ["\x1b[%sm" % n for n in range(91, 96)]
    red, green, yellow, blue, pink = cols
else:
    ul = red = green = yellow = blue = pink = white = ""

r, g, y, b, p, w = red, green, yellow, blue, pink, white

ansirx = re.compile(r'\x1b\[\d*m', re.UNICODE)

def c(colour, text):
    """ Return coloured text. """
    colours = {'r': r, 'g': g, 'y': y, 'b':b, 'p':p}
    return colours[colour] + text + w

def charcount(s):
    """ Return number of characters in string, with ANSI color codes excluded. """
    return len(ansirx.sub('', s))
