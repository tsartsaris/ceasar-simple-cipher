#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

    Initial commit of the code at https://github.com/tsartsaris/ceasar-simple-cipher
"""

import os
import random
import string
import collections  # θα χρησιμοποιήσουμε την collections κάνουμε πιο έυκολη τη ζωή μας
from string import ascii_lowercase # αυτό είναι το "a...z"
from string import maketrans
import matplotlib.pyplot as plt

letterGoodness = dict(zip(string.ascii_uppercase,
                        [.0817,.0149,.0278,.0425,.1270,.0223,.0202,
                         .0609,.0697,.0015,.0077,.0402,.0241,.0675,
                         .0751,.0193,.0009,.0599,.0633,.0906,.0276,
                         .0098,.0236,.0015,.0197,.0007]))

trans_tables = [ maketrans(string.ascii_uppercase,
                 string.ascii_uppercase[i:]+string.ascii_uppercase[:i])
                 for i in range(26)]

plot_dict={}
all_plot=()

keys_percentage={}

def goodness(msg):
    return sum(letterGoodness.get(char, 0) for char in msg)

def all_shifts(msg):
    msg = msg.upper()
    i=1
    for trans_table in trans_tables:
        txt = msg.translate(trans_table)
        plot_dict[i]=goodness(txt)
        yield goodness(txt), txt ,i , plot_dict
        i+=1




for root, dirs, files in os.walk("encrypted"): #ανοίγουμε και το φακελο με τα αρχέια
    for file in files:
        i=1
        if file.endswith(".txt"): # αν ειναι τχτ
            f = open(os.path.join(root, file),'r') #διαβάζουμε
            encrypted_text = f.read()
            all_plot = max(all_shifts(encrypted_text))
            keys_percentage[all_plot[2]]=all_plot[0]
            plt.bar(range(len(all_plot[3])), all_plot[3].values(), align='center')
            plt.xticks(range(len(all_plot[3])), all_plot[3].keys())

            #plt.show()
    

print keys_percentage
plt.bar(range(len(keys_percentage)), keys_percentage.values(), align='center')
plt.xticks(range(len(keys_percentage)), keys_percentage.keys())

plt.savefig('allplot.png')

