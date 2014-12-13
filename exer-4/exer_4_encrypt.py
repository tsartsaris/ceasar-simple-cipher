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
	Με τον κώδικα που ακολουθέι εφαρμόζουμε κρυπτογράφηση με τον τύπο
	Ci = (ai+bMi+g)(ModN)
	και αποκρυπτογράφηση με τον τύπο
	Mi = b^-1(Mi-ai-g)(ModN)
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

decipher_text = [] # εδώ θα αποθηκεύσουμε το αποκρυπτογραφημένο κείμενο
cipher_text = [] #είσοδος από το χρήστη του κειμένου που θέλει να κρυπτογραφηθεί

def create_initial_dict(i = 0): # ο iterator αν αλλάξει σε άλλον αριθμό θα γίνει διαφορετικό ξεκίνημα 
								# για την αντιστοίχηση ex if i=3 then a=3, b=4 ....... z = 29 ή 2 (modulo)
								# οπότε μετά θα αλλάξει λογικά και το modulo για να αποφύγουμε διπλότυπα
	for char in string.ascii_lowercase: #iteration σε όλα τα γράμματα a-z
	    numbers_letters[i]=char #dictionary construction το key είναι το i : value το γράμμα
	    i+=1


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
	Το κάννουμε 3 φορές
"""
def get_key1():
	while True:
		try:
			key_disp = int(raw_input("Please enter a number for key1: "))
			break
		except ValueError:
			print "Oops!  That was no valid number.  Try again..."
	return key_disp%len(string.ascii_lowercase) #θα μπορούσαμε να βάλουμε %26 αλλά αν αλλάξει το αλφάβητο απο αγγλικό σε ελληνικό?

def get_key2():
	while True:
		try:
			key_disp = int(raw_input("Please enter a number for key2: "))
			break
		except ValueError:
			print "Oops!  That was no valid number.  Try again..."
	return key_disp%len(string.ascii_lowercase) #θα μπορούσαμε να βάλουμε %26 αλλά αν αλλάξει το αλφάβητο απο αγγλικό σε ελληνικό?

def get_key3():
	while True:
		try:
			key_disp = int(raw_input("Please enter a number for key3: "))
			break
		except ValueError:
			print "Oops!  That was no valid number.  Try again..."
	return key_disp%len(string.ascii_lowercase) #θα μπορούσαμε να βάλουμε %26 αλλά αν αλλάξει το αλφάβητο απο αγγλικό σε ελληνικό?



"""
	Με τις 2 παρακάτω υπολογίζουμε τον αντίστροφο με το διευρημένο αλγόριθμο του Ευκλείδη
"""
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m


create_initial_dict() # αν είχαμε κάνει στην αρχή fixed το dictionary αυτό θα το προσπερνούσαμε

key1 = get_key1()
key2 = get_key2()
key3 = get_key3()

text = get_text_from_user() # πέρνουμε το κείμενο από το χρήστη

for char in text: # iterate στο κείμενο του χρήστη
	i=1
	for key,value in numbers_letters.iteritems(): # iterate και στο αρχικό dictionary
		if value == char: # αν βρούμε το ίδιο γράμμα
			fkey = ((key1*i)+(key2*key) + key3)%26 # τότε η θέση του νέου γράμματος θα είναι από τον τύπο
			cipher_text.extend(numbers_letters[fkey]) # τότε προσθέτουμε στη λίστα το γράμμα που αντιστοιχεί στην ίδια θέση από 
			i+=1											  # το αρχικό dictionary, μετατόπιση δηλαδή

print ''.join(cipher_text) # εμφανίζουμε το αποτέλεσμα στο χρήστη μετατρέποντας τη λίστα σε string

euklidian = modinv(key2,26)
print euklidian # Ο αντίστροφος του β, του key2 δηλαδή

for char in cipher_text: #για κάθε χαρακτήρα του κρυπτογραφημένου πλέον κειμένου
	i=1 
	for key,value in numbers_letters.iteritems(): #για κάθε ζεύγος στην αντιστοίχηση γραμμάτων αριθμών
		if value == char: # αν υπάρχει ο χαρακτήρας
			fkey = (euklidian*(key-(key1*i)-key3))%26 #εφαρμόζουμε τον τύπο με τον αντίστροφο
			decipher_text.extend(numbers_letters[fkey]) #αντιστοιχίζουμε τον νεό αριθμό με το γράμμα στο dictionary <αντίστροφη μετατόπιση>
			i+=1
print ''.join(decipher_text) #τέλος εμφανίζουμε το decrypted μήνυμα στο χρήστη

"""
Αποτέλεσμα
Please enter a number for key1: 3
Please enter a number for key2: 7
Please enter a number for key3: 9
Please provide text to encrypt: I am a data nerd
qmsmhmpmzobh
15
iamadatanerd
"""
