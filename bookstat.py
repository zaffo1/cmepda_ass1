#!/usr/bin/env python
# Copyright (C) 2022 luca.baldini@pi.infn.it
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""First assignment for the CMEPDA course, 2022/23.

--- Goal
Write a Python program that prints the relative frequence of each letter
of the alphabet (without distinguishing between lower and upper case) in the
book.

--- Specifications
- ---the program should have a --help option summarizing the usage
- ---the program should accept the path to the input file from the command line
- ---the program should print out the total elapsed time
- the program should have an option to display a histogram of the frequences
- [optional] the program should have an option to skip the parts of the text
  that do not pertain to the book (e.g., preamble and license)
- [optional] the program should have an option to print out the basic book
  stats (e.g., number of characters, number of words, number of lines, etc.)
"""

import time
import argparse

start_time = time.time() #time when the program is starting

def process(file_path):
    """
    """
    print(f'Opening input file {file_path}...')
    with open(file_path, 'r') as input_file:
        text = input_file.read()
    print(text)
    print('Done.')
    #words = text.split()
    #print('Number of words in text file :', len(words))
    #char='A'
    #print(f'The character {char} occurs {text.count(char)} time(s)')
    d = dict()
    print(d)
    for c in text:
        if c in d:
            d[c] = d[c] + 1
        else:
           d[c] = 1
    print(d)
 

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Print some book statistics')
    parser.add_argument('infile', type=str, help='path to the input file')
    args = parser.parse_args()
    process(args.infile)

    elapsed_time = time.time() - start_time
    print(f'Elapsed time: {elapsed_time} seconds') #prints execution time% (time.time() - start_time)