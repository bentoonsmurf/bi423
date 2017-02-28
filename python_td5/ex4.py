nom="txt"
f=open(nom,"r")
ligne_actuel=f.readline()
seq=ligne_actuel
while ligne_actuel != "":
	ligne_actuel=f.readline()
	seq=seq +ligne_actuel
seq=seq.replace('\n','')
seq=seq.lower()
f.close()
i=0

i=0
transcrit=""
while i<len(seq):
	if seq[i]=='a':
		transcrit='t'+transcrit
	elif seq[i]=='t':
		transcrit='a'+transcrit
	elif seq[i]=='c':
		transcrit='g'+transcrit
	elif seq[i]=='g':
		transcrit='c'+transcrit
	else:
		print "x"
		#print "x"
		#transcrit='x'+transcrit
	i=i+1
	







fichier2=open("save","w")

somme=""
i=1
while i<len(seq) :
	somme=somme+seq[i:i+3]+" "
	i=i+3
print "texte", somme
fichier2.write("chaine + 1\n"+somme+" ")
somme=""
i=2
while i<len(seq) :
	somme=somme+seq[i:i+3]+ " "
	i=i+3
print "texte", somme
fichier2.write("\nchaine + 2\n"+somme+" ")
somme=""
i=3
while i<len(seq) :
	somme=somme+seq[i:i+3]+" "
	i=i+3
print "texte", somme
fichier2.write("\nchaine + 3\n"+somme+" ")

inverse=""
i=1
while i<len(seq) :
	inverse=inverse+transcrit[i:i+3]+ " "
	i=i+3
fichier2.write("\ninverse complentaire +1\n"+transcrit+"\n")
print inverse
inverse=""
i=2
while i<len(seq) :
	inverse=inverse+transcrit[i:i+3]+" "
	i=i+3
fichier2.write("\ninverse complentaire +2\n"+transcrit+"\n")
inverse=""
i=3
while i<len(seq) :
	inverse=inverse+transcrit[i:i+3]+" "
	i=i+3
fichier2.write("\ninverse complentaire +3\n"+transcrit+"\n")


fichier2.close()









