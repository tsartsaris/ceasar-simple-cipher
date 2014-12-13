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
import urllib
from bs4 import BeautifulSoup
import re

html = urllib.urlopen('http://shakespeare.mit.edu/merry_wives/full.html').read() #Διαβάζουμε τη σελίδα με το έργο του Shakespeare
soup = BeautifulSoup(html) #και το κάνουμε μία ωραία σούπα 

file = open("merry_wives.txt", "w") #ετοιμάζουμε ένα text αρχείο να το αποθηκεύσουμε


for block in soup.find_all('blockquote'): #βρίσκουμε όλα τα blockquotes αφου εκεί ειναι οι διάλογοι
    if block.get_text().startswith('ENTER'): #αν ξεκινάει με ENTER είναι για να μπουν στη συζήτηση χαρακτήρες του έργου. Δε μας ενδιαφέρει
        pass
    elif 'Enter' in block.get_text(): #το ίδιο με πάνω
        pass
    else:
        file.write(block.get_text()) #όλα τα άλλα τα θέλουμε

file.close()

"""
    Έχουμε ένα ωραίο αρχείο txt το οποίο αργότερα θα σπάσουμε σε 100 κομμάτια για να κάνουμε τα tests 
    που θέλουμε με τυχαίες κρυπτογραφήσεις. Μπορεί να φεύγω κάπως από την τυπική διατύπωση της άσκησης 
    αλλά δε νομίζω ότι έχει και τόση σαφήνεια. 
"""
