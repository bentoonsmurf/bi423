class bcolors:
	fail= '\033[91m'
	end= '\033[0m'
	vert ='\033[92m'
	
	



seq2=raw_input(bcolors.vert +'entrer une chaine de char ' + bcolors.end)
n2=input("N = ")

print "si vous voulez extraire les n premiers char entrer 1 "
print " si vous voulez extraire les dernier taper 2"

choix = input("choix = ")


if choix==1:
	

	print seq2[0:n2]#extract 0 a n exclu

elif choix==2:
	
	if len(seq2)>n2:
		print seq2[len(seq2)-n2:]#extract 0 a n exclu
	else:
		print seq2[len(seq2)-n2:]
else:
	print (" pour aprendre a lire veuiller vous refferer aux cours de CP CE1")	



