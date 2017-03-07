
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

place_du_motif=seq.find("atg",0)
if place_du_motif == -1 :
	print "pas dans la chaine"
else :
	print "la premiere ocurence est a la place",place_du_motif,"dans la chaine"
	



