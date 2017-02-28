
nom=raw_input("ecrire nom de fihier ")
f=open(nom,"r")
x=0
i=0
pos=0
ligne_actuel=f.readline().rstrip("\n")
ligne=ligne_actuel
while ligne_actuel != "":
	i=i+1
	if x <len(ligne) :
		x= len (ligne)
		pos=i
		ligne=ligne_actuel
	ligne_actuel=f.readline().rstrip("\n")
f.close()
fichier2=open("save","w")
fichier2.write("la sequance la plus longue est "+ligne[0:len(ligne)]+"\n")
fichier2.write("sa longueur est "+str(len(ligne))+"\n")
fichier2.write("sa pos est "+str(pos)+"\n")
fichier2.close()






