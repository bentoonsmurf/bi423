import colors
import time
#on prend les choix et on met le resultat de l'operation dans un fichier 
#init
choice = 0
#boucle qui contient le prgm
lis = raw_input(colors.warning("Fichier a ouvrir : "))
f = open(lis, "r")
seq = 0
taille = 0
ligne = f.readline().rstrip('\n')
while( ligne != "") :
	seq += 1
	taille += len(ligne) 
	ligne = f.readline().rstrip('\n')
	
nom_fic = time.strftime("%c").replace(" ","-") + ".datas"
f2 = open(nom_fic, "w")
f2.write( "Il y a " + str(seq) + " sequences \n")
f2.write( "La moyenne de la taille est de " + str(float(taille)/float(seq)))
f.close()
f2.close()	
