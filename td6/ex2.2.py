import colors;

motif=raw_input(colors.ao("entrer le motif "))
taux_erreur=input(colors.error("entrer un taux d erreur , par ex 0.1 "))
while taux_erreur>0.5:
	taux_erreur=input(colors.error("entrer un taux d erreur <0.5   "))
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
i2=0
car_vrai=0.0
car_faux=0.0
pcent_faux=0.0
pcent_vrai=0.0
while (i<len(seq)-len(motif)):
	i2=0
	while i2<len(motif):
		if (motif[i2]==seq[i2+i]):
			car_vrai=car_vrai+1
		else:
			car_faux=car_faux+1
		i2=i2+1
	if car_faux/(car_faux+car_vrai) <taux_erreur:
		somme_des_places=somme_des_places+": "+str(i+1)
	car_vrai=0.0
	car_faux=0.0
	i=i+1

if somme_des_places == "" :
	print "pas de",motif,"dans la chaine"
else :
	print motif,"est aux places",somme_des_places












fichier2=open("save_comparaison","w")
if somme_des_places =="" :
	fichier2.write("erreur")
else:
	fichier2.write(motif+" est aux places "+somme_des_places)
	fichier2.write("\navec un taux d'erreur acepte de "+str(taux_erreur))
fichier2.close()
