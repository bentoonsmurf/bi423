import colors
import time
from Tkinter import *

#but de l'exercice :
#faire le gc skew 

#debut
path = raw_input(colors.warning("Fichier 1 a ouvrir : "))

#ouverture fichier
f = open(path, "r")

#lecture premiere ligne
#on ne prend pas en compte la premiere ligne du fichier fasta
seq = f.readline().rstrip('\n')
#on commence a rentrer la sequence dans un string
ligne = f.readline().rstrip('\n')
while (ligne != "") :
	seq += ligne
	ligne = f.readline()
f.close()

#uniformisation chaine
seq = seq.lower()
taille = len(seq)
div = 400
stl = 0
endl = int(div)
i =0
delta=1
#canvas 
fenetre = Tk()
canvas = Canvas(fenetre, width = taille/800 * 10, height = 300, background = 'white')

while (stl < taille - div ) :
	if(endl <= taille) :
		cur = seq[stl:endl]
	else :
		cur = seq[stl:]
	nb_g = cur.count('g')
	nb_c = cur.count('c')
	
	C1 = nb_g - nb_c
	C2 = nb_g + nb_c
	operation = (float(C1)/float(C2)) * 100
	if(i==0): 
		operation2=0
	operation2 =operation2 +(float(C1)/float(C2))
	operation = int(operation) 
	operation += 100 
	if(i==0) : 
		op2 = operation
		op22=operation2
	print operation - 100
	q = 250
	
	ligne1= canvas.create_line(i-delta, q-op2, i, q- operation )
	ligne2= canvas.create_line(i-delta, q-op22, i, q- operation2+1 )
	stl += int(div)
	endl += int(div)
	i+=delta
	op2 = operation
	op22=operation2
canvas.pack()
fenetre.mainloop()
