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

storing_f_k = {} #εδω θα αποθηκεύσουμε τα ονόματα των αρχείων με το κλειδί που χρησιμοποιήσαμε κάθε φορά για να κάνουμε το encryption
numbers_letters = {} #βλέπε ceasar1_1.py
numbers_letters_disp = {} #βλέπε ceasar1_1.py

def create_key():
	return random.randint(1, 1000)%26+1  #με ένα τυχαίο αριθμό από το 1 μεχρι το 1000 πέρνουμε το modulo και έχουμε το κλειδι 

def create_initial_dict(i = 0): # ο iterator αν αλλάξει σε άλλον αριθμό θα γίνει διαφορετικό ξεκίνημα 
								# για την αντιστοίχηση ex if i=3 then a=3, b=4 ....... z = 29 ή 2 (modulo)
								# οπότε μετά θα αλλάξει λογικά και το modulo για να αποφύγουμε διπλότυπα
	for char in string.ascii_lowercase: #iteration σε όλα τα γράμματα a-z
	    numbers_letters[i]=char #dictionary construction το key είναι το i : value το γράμμα
	    i+=1

def create_displacement_dict(key):
	key=key%len(string.ascii_lowercase)
	for char in string.ascii_lowercase: #iteration σε όλα τα γράμματα a-z
	    numbers_letters_disp[key]=char #dictionary construction το key είναι το i : value το γράμμα
	    key = (key+1)%len(string.ascii_lowercase)
	return numbers_letters_disp

for root, dirs, files in os.walk("splits"): #ανοίγουμε και το φακελο με τα αρχέια
    for file in files:
        if file.endswith(".txt"): # αν ειναι τχτ
        	f = open(os.path.join(root, file),'r') #διαβάζουμε
        	fNewList=list(f.read()) #και φτιάχνουμε μία λίστα θα είναι της μορφής
        	encryption_key = create_key() #δημιουργούμε ένα τυχαίο κλειδί
        	create_initial_dict() #βλέπε ceasar1_1.py
        	disposition_dict = create_displacement_dict(encryption_key)#βλέπε ceasar1_1.py
        	for index,item in enumerate(fNewList): #για κάθε χαρακτήρα μέσα στη λίστα
        		for key,value in numbers_letters.iteritems(): #για κάθε στοιχείο μέσα στο dictionary
        			if item==value: #αν είναι ίδιο 
        				fNewList.pop(index) #αφαιρούμε το στοιχείο
        				fNewList.insert(index,disposition_dict[key]) #και βάζουμε το αντίστοιχο από το dictionary με τους encrypted χαρακτήρες
        	#print fNewList
        	newpath ='encrypted/' # ορίζουμε ότι θα σώζουμε τα νέα αρχεία σε ένα φακελο encrypted
        	if not os.path.exists(newpath): # αν δεν υπάρχει ο φάκελος 
				os.makedirs(newpath) #τον φτιάχνουμε
        	newfile = open(newpath+file, "w") #καινουριο txt 
        	newfile.write(''.join(fNewList)) #γράφουμε το αποτέλεσμα
        	newfile.close() #κλείνουμε
        	storing_f_k[file]=encryption_key #εδώ βάζω κάθε αρχείο το κλειδί με το οποίο το έκανα encryption

with open ('encryption_keys.txt', 'w') as fp:
    for p in storing_f_k.items():
        fp.write("%s:%s\n" % p) #και το αποθηκεύω σε ένα txt



"""
το encrypted αρχειο είναι κάπως έτσι
Sfo Hrde, mboprxab jb klq; I tfii jxhb x Sqxo-
zexjybo jxqqbo lc fq: fc eb tbob qtbkqv Sfo Jlek
Fxipqxccp, eb pexii klq xyrpb Rlyboq Sexiilt, bpnrfob.

Ik qeb zlrkqv lc Gilrzbpqbo, grpqfzb lc mbxzb xka
'Cloxj.'

Av, zlrpfk Sibkabo, xka 'Crpqxilrorj.

Av, xka 'Rxql-ilorj' qll; xka x dbkqibjxk ylok,
jxpqbo mxoplk; tel tofqbp efjpbic 'Aojfdbol,' fk xkv
yfii, txooxkq, nrfqqxkzb, lo lyifdxqflk, 'Aojfdbol.'

Av, qexq I al; xka exsb alkb xkv qfjb qebpb qeobb
erkaoba vbxop.

Aii efp przzbpplop dlkb ybclob efj exqe alkb'q; xka
xii efp xkzbpqlop qexq zljb xcqbo efj jxv: qebv jxv
dfsb qeb alwbk tefqb irzbp fk qebfo zlxq.

Iq fp xk lia zlxq.

Teb alwbk tefqb ilrpbp al ybzljb xk lia zlxq tbii;
fq xdobbp tbii, mxppxkq; fq fp x cxjfifxo ybxpq ql
jxk, xka pfdkfcfbp ilsb.

Teb irzb fp qeb cobpe cfpe; qeb pxiq cfpe fp xk lia zlxq.

I jxv nrxoqbo, zlw.

Ylr jxv, yv jxoovfkd.

Iq fp jxoofkd fkabba, fc eb nrxoqbo fq.
"""


"""
και το αρχείο αντιστοίχησης αρχειων με κλειδια κάπως έτσι

merry_wives_1295.txt:19
merry_wives_595.txt:18
merry_wives_3395.txt:24
merry_wives_1330.txt:1
merry_wives_1750.txt:23
merry_wives_3430.txt:8
merry_wives_3010.txt:18
merry_wives_2520.txt:18
merry_wives_2800.txt:13
merry_wives_1015.txt:20
merry_wives_2415.txt:6
merry_wives_0.txt:3
merry_wives_1645.txt:7
merry_wives_2030.txt:25
merry_wives_35.txt:6
merry_wives_3220.txt:25
merry_wives_1785.txt:23
merry_wives_770.txt:22
merry_wives_1960.txt:3
merry_wives_385.txt:20
merry_wives_1155.txt:21
........................
"""
