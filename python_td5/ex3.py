


somme=""
cadre_de_lecture=input("ecrire un chiffre entre [ 1 et 3 ]")
while cadre_de_lecture>3 or cadre_de_lecture<1 :
	print "non"
	cadre_de_lecture=input("ecrire un chiffre entre [ 1 et 3 ]")

#nom=raw_input("ecrire nom de fihier ")
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

print seq[:]
print seq[cadre_de_lecture:]
seq=seq[cadre_de_lecture:]
while i<len(seq) :
	somme=somme+seq[i:i+3]+"\n"
	i=i+3

fichier2=open("save","w")
fichier2.write("la chaine est\n"+somme[0:]+"\n")
fichier2.close()

