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

from __future__ import division
from sympy import *

send_msg = [1,0,0,1,0,0,1,0,0,1,1,0,1,1,0,1,1,0,0,1,0,0,1,0,0,1,1,0] #σταλμένο μήνυμα
stream_rec = [1,0,1,1,1,1,0,0,0,0,1,1,0,0,0,1,0,0,1,0,1,0,1,1,0,0,0,1] #κρυπτογραφημένο μήνυμα
xor_res = [] #μία κενή λίστα όπου θα βάλουμε την απαντηση της XOR στην αντιστοίχηση των στοιχείων από τις λίστες

smlen = len(send_msg) # το μήκος της λίστας
srlen = len(stream_rec) #το μήκος της λίστας

if smlen == srlen: #αν οι λίστες έχουν το ίδιο μήκος
    zipped = zip(send_msg,stream_rec) #τις ζιπάρουμε το αποτέλεσμα που έχουμε είναι 
#print zipped
"""
[(1, 1), (0, 0), (0, 1), (1, 1), (0, 1), (0, 1), (1, 0), (0, 0),
(0, 0), (1, 0), (1, 1), (0, 1), (1, 0), (1, 0), (0, 0), (1, 1), 
(1, 0), (0, 0), (0, 1), (1, 0), (0, 1), (0, 0), (1, 1), (0, 1),
(0, 0), (1, 0), (1, 0), (0, 1)]
δηλαδή 28 ζεύγη 
"""


#η XOR μαθηματικά έιχαμε δει στο μάθημα ότι έιναι (x+y)%2. Το κάνουμε αυτό για κάθε ζεύγος 
#και το αποτέλεσμα το βάζουμε στην xor_res
for item in zipped:
    xor_l_res = (item[0]+item[1])%2
    xor_res.append(xor_l_res)
#print xor_res
"""
και έχουμε μία λίστα με τα αποτελέσματα της XOR
[0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1]
"""


"""
πρέπει να δουμε σπάζοντας σε ισόποσα κομμάτια την λίστα με τα XOR σε πιο σπάσιμο θα έχουμε
ακριβώς τις ίδιες ακολουθίες. Ξέρουμε ότι το μεγαλύτερο σπάσιμο της LFSR είναι το 7
η chunks σπάει σε ισόποσα τμήματα ίσα με n
"""
def chunks(l, n):
    if n < 1:
        n = 1
    return [l[i:i + n] for i in range(0, len(l), n)]

"""
οπότε αφού το μεγαλύτερο σπάσιμο είναι το 7 κάνουμε ένα iteration από 1 εως 8 <η python μετράει 
μέχρι n-1 στην range>
"""
for i in range(1,8):
    newl = chunks(xor_res,i) #βάζουμε σε μία νέα λίστα τα αποτελέσματα από κάθε σπάσιμο
    if all(x==newl[0] for x in newl)==True: # και ελέγχουμε αν τα κομμάτια είναι ίδια
        meter = i #αν είναι ίδια, έχουμε μέτρο και το επιστρέφουμε στη μεταβλητή meter

print meter
"""
Εδώ λύνω τη συνάρτηση 2**m-1=meter
το solve της SumPy υποθέτει ότι το αποτέλεσμα είναι πάντα 0 , οπότε 
μετατρέπω τη συνάρτηση σε 2**m-1-meter=0

"""
x = Symbol('x')
print solve(2**x - 1-meter, x)

"""
έχω απάντηση οτι το μέτρο είναι 7 
και το μήκος 3
7
[3]
"""
