
nom=raw_input("ecrire nom de fihier ")
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
somme =""
while i<len(seq) :
	somme=somme+seq[i:i+3]+"\n"
	i=i+3
	
fichier2=open("save","w")
fichier2.write("la chaine est\n"+somme[0:]+"\n")
fichier2.close()

