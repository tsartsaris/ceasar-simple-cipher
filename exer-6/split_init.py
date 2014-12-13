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

"""
	Αυτό που θέλουμε να κάνουμε έιναι να σπάσουμε το αρχικό κείμενο που φτιάξαμε
	σε 100 κομμάτια. Θα μετρήσουμε τις γραμμές που έχουμε στο σύνολο και θα τις διαιρέσουμε 
	με το 100. Στη συνέχεια θα διαβαζουμε κάθε ν γραμμές, όπου ν το ποιλίκο 
	από την προηγούμενη πράξη και όσο θα διαβάζουμε θα δημιουργούμε καινούρια αρχεία
	με όνομα τη σειρά που ξεκινάμε να διαβάζουμε. 
"""



import os

shname = "merry_wives.txt" #	Με αυτό ξεκινάμε

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1  # περνάμε σε έναν enumerator τις γραμμές και στο τέλος προσθέτουμε το ένα 
    			  # μιας και ο enumerator ξεκινάει από το 0

lines = file_len(shname)
divider = abs(lines/100)  # ο divider είναι το πλήθος των γραμμών / 100 = 35


 
# εδώ θα φτιάξουμε την διεργασία κατακερματισμού
def file_splitter(fullfilepath, lines=50): # α έχουμε σαν ορίσματα το αρχείο και κάθε πόσες γραμμές να σπλιτάρουμε 
  path, filename = os.path.split(fullfilepath) #πέρνουμε το path που είναι το αρχείο
  basename, ext = os.path.splitext(filename) #και το όνομα του με ορίσματα
  # print path
  path = path+'splits/' # ορίζουμε ότι θα σώζουμε τα νέα αρχεία σε ένα φακελο splits
  if not os.path.exists(path): # αν δεν υπάρχει ο φάκελος 
    os.makedirs(path) # θα τον φτιάξουμε εμείς
  # print filename
  # ανοίγουμε το αρχέιο
  with open(fullfilepath, 'r') as f_in:
    try:
      # και ετοιμάζουμε το πρώτο αρχέιο που θα γράψουμε
      f_output = os.path.join(path, '{}_{}{}'.format(basename, 0, ext))
      f_out = open(f_output, 'w')
 
      # διαβάζουμε σειρά σειρά
      for i, line in enumerate(f_in):
        # Αν η σειρά που διαβάζουμε μπορεί να διαιρεθεί με τον divider 
        # είναι δηλαδή πολλαπλάσιο στην περίπτωσή μας του 35
        # κλείνουμε το αρχείο και πάμε στο επ´ομενο
        if i % lines == 0:
          f_out.close()
          f_output = os.path.join(path, '{}_{}{}'.format(basename, i, ext))
          f_out = open(f_output, 'w')
 
        # βάζουμε την εκάστοτε σειρά στο αρχείο
        f_out.write(line)
 
    finally:
      # και το κλεινουμε 
      f_out.close()
 
# καλούμε τη file_splitter δίνοντας το αρχέιο που θα κάνουμε split και τον divider
file_splitter('merry_wives.txt', divider)

"""
	Τελικά θα έχουμε στο φάκελο του αρχείου έναν νέο φάκελο με το όνομα splits
	και εκεί μέσα 100 νέα πιο μικρά αρχεία με 35 γραμμές το καθένα. Με αυτά θα κάνουμε τα tests 
"""
