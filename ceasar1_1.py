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

    Initial commit of the code at 
"""


"""
	Με τον κώδικα που ακολουθεί εφαρμόζουμε τη μέθοδο του Ceasar για απλή κρυπτογράφηση κειμένου. 
	Η κρυπτογράφηση θα γίνει με μετατόπιση της αρχικής θέσης κάθε γράμματος κατά την αρχική θέση προσθέτοντας 
	το κλειδί και κρατώντας το μόντουλο με 26. Τα comments ή θα είναι πριν από το κομμάτι κώδικα που επεξηγούνε
	ή στην ίδια σειρά μετά από ένα #
"""




"""
	Ένας έυκολος τρόπος να κάνουμε iteration σε γράμματα είναι μέσα από το string module
	έτσι δεν θα πληκτρολογήσουμε τίποτα αλλά θα φτιάξουμε ένα dictionary γρήγορα αντιστοιχώντας
	γράμματα σε αριθμούς πάνω στο iteration
"""
import string




"""
	αυτό είναι το βασικό dictionary και το αρχικοποιούμε σε global 
	θα μπορούσαμε να κάνουμε αρχικοποίηση με 
	numbers_letters = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 
	6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n',
	14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u',
	21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}
	αλλά έτσι δεν θα μπορούσαμε να αλλάξουμε την αρχικοποίηση τιμών
	και το πρόγραμμά μας δεν θα ήταν καθόλου ευέλικτο
"""
numbers_letters = {} 




"""
	αυτό είναι το dictionary με το disposition των γραμμάτων βάση του κλειδιού
	για key=13 θα πάρει τη μορφή  
	numbers_letters = {0: 'n', 1: 'o', 2: 'p', 3: 'q', 4: 'r', 5: 's', 6: 't',
	7: 'u', 8: 'v', 9: 'w', 10: 'x', 11: 'y', 12: 'z', 13: 'a', 14: 'b', 15: 'c',
	16: 'd', 17: 'e', 18: 'f', 19: 'g', 20: 'h', 21: 'i', 22: 'j',
	23: 'k', 24: 'l', 25: 'm'}
"""
numbers_letters_disp = {}



cipher_text = [] #είσοδος από το χρήστη του κειμένου που θέλει να κρυπτογραφηθεί

def create_initial_dict(i = 0): # ο iterator αν αλλάξει σε άλλον αριθμό θα γίνει διαφορετικό ξεκίνημα 
								# για την αντιστοίχηση ex if i=3 then a=3, b=4 ....... z = 29 ή 2 (modulo)
								# οπότε μετά θα αλλάξει λογικά και το modulo για να αποφύγουμε διπλότυπα
	for char in string.ascii_lowercase: #iteration σε όλα τα γράμματα a-z
	    numbers_letters[i]=char #dictionary construction το key είναι το i : value το γράμμα
	    i+=1


"""
	Αφού πάρουμε από το χρήστη το κλειδί κατασκευάζουμε το νέο dictionary στο οποίο θα κάνουμε αντιστοίχηση 
	της θέσης των γραμμάτων ανάλογα με το αρχικό και θα αντικαθιστούμε με το γράμμα απο εδώ.
"""
def create_displacement_dict(key):
	key=key%len(string.ascii_lowercase)
	for char in string.ascii_lowercase: #iteration σε όλα τα γράμματα a-z
	    numbers_letters_disp[key]=char #dictionary construction το key είναι το i : value το γράμμα
	    key = (key+1)%len(string.ascii_lowercase)
	return numbers_letters_disp




"""
	Με την get_text_from_user περιμένουμε από το χρήστη ένα κείμενο για να το κρυπτογραφήσουμε.
	Σημ. έχω κρατήσει απλό τον κώδικα , δεν ελέγχω για αριθμούς και στίξη προσπαθώντας να είναι 
	κατανοητό από όλους. 
"""
def get_text_from_user():
	text = raw_input("Please provide text to encrypt: ").lower()
	return text




"""
	Με την get_key_from_user πέρνουμε έναν αριθμό από τον χρήστη για που θα έιναι το κλειδί για 
	το disposition των γραμμάτων. Επιστρέφουμε το modulo στη return. 
"""
def get_key_from_user():
	while True:
		try:
			key_disp = int(raw_input("Please enter a number for disposition: "))
			break
		except ValueError:
			print "Oops!  That was no valid number.  Try again..."
	return key_disp%len(string.ascii_lowercase) #θα μπορούσαμε να βάλουμε %26 αλλά αν αλλάξει 
						    #το αλφάβητο απο αγγλικό σε ελληνικό?




create_initial_dict() # αν είχαμε κάνει στην αρχή fixed το dictionary αυτό θα το προσπερνούσαμε
text = get_text_from_user() # πέρνουμε το κείμενο από το χρήστη
modulo = get_key_from_user() # πέρνουμε το κλειδί
disposition_dict = create_displacement_dict(modulo) #κατασκευάζουμε το νέο dictionary κάνωντας dispotition 
						    #τα γράμματα με βάση το κλειδί
for char in text: # iterate στο κείμενο του χρήστη
	for key,value in numbers_letters.iteritems(): # iterate και στο αρχικό dictionary
		if value == char: # αν βρούμε το ίδιο γράμμα
			cipher_text.extend(disposition_dict[key]) # τότε προσθέτουμε στη λίστα το γράμμα που αντιστοιχεί στην ίδια θέση από 
							          # το dictionary που έχουν μετακινηθεί τα γράμματα βάση του κλειδιού

print ''.join(cipher_text) # εμφανίζουμε το αποτέλεσμα στο χρήστη μετατρέποντας τη λίστα σε string

"""
Αν θέλαμε να κρατάμε αριθμούς και σύμβολα από το αρχικό κείμενο θα κάναμε 
list.pop(i) "βγάζουμε ένα"
list.insert(i, char) "βάζουμε ένα νέο στην ιδια θέση"
δηλαδή το αρχικό κείμενο θα το μετατρέπαμε σε μία λίστα και θα παίζαμε εκεί πάνω.
"""
