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

place_du_motif=seq.find(motif,0)

while place_du_motif != -1 :
	somme_des_places=somme_des_places+" "+str(place_du_motif+1)
	place_du_motif=seq.find(motif,place_du_motif+1)

if somme_des_places == "" :
	print "pas de",motif,"dans la chaine"
else :
	print motif,"est aux places",somme_des_places


fichier2=open("save","w")
if somme_des_places =="" :
	fichier2.write("erreur")
else:
	fichier2.write(motif+" est aux places"+somme_des_places)
fichier2.close()
