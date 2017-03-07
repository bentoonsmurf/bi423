import colors;

motif=raw_input(colors.ao("entrer le motif "))
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
somme_des_places=""

i=0

while i<(len(seq)-len(motif)):
	if seq[i:i+len(motif)] ==motif[0:] :
		somme_des_places=somme_des_places+" "+str(i+1)
	i=i+1




if somme_des_places == "" :
	print "pas de",motif,"dans la chaine "
else :
	print motif,"est aux places",somme_des_places


fichier2=open("save","w")
if somme_des_places =="" :
	fichier2.write("erreur")
else:
	fichier2.write(motif+" est aux places"+somme_des_places)
fichier2.close()
