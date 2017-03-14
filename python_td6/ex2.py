import colors;

chaine1=raw_input(colors.ao("entrer premiere chaine "))
chaine2=raw_input(colors.ao("entrer deuxiemme chaine "))

i=0
car_vrai=0.0
car_faux=0.0
pcent_faux=0.0
pcent_vrai=0.0

while i<len(chaine1) and i<len(chaine2):
	if (chaine1[i]==chaine2[i]):
		car_vrai=car_vrai+1
	else:
		car_faux=car_faux+1
	i=i+1
reste=len(chaine1)+len(chaine2)-((car_faux+car_vrai)*2)
max_char=(len(chaine1)+len(chaine2)+reste)/2
pcent_faux=(car_faux+reste)/max_char*1.0
pcent_vrai=car_vrai/max_char*1.0



print " il y a ",pcent_faux," d'erreur"
print " il y a ",pcent_vrai," de lettres correspondantes"

fichier2=open("save_comparaison","w")

fichier2.write("pourcent faux : "+str(pcent_faux*100)+"\n pourcent vrai"+str(pcent_vrai*100))
fichier2.close()
