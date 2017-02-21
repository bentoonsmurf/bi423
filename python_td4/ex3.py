
choix=input("entrer un choix \n 1 pour transcrit \n 2 pour calcul differenciel avec prise en compte des irregularite \n 3 pour danser\n")

while choix !=3:
	choix=input("entrer un choix \n 1 pour transcrit \n 2 pour calcul differenciel avec prise en compte des irregularite \n 3 pour danser\n")

	if choix ==2:
		
		
		nom = raw_input(" saisir nom du fichier  ")
		f=open(nom,"r")
		line=f.readline().rstrip("\n")
		seq=""
		while line != "":
			seq=seq+line
			line=f.readline().rstrip("\n")
		# [0:4] de 0 a 4 exclu
		#line=f.readline.rstrip("\n")
		f.close()
		print seq
		seq=seq.lower()
	## inverse complementaire
		i=0
		transcrit=""
		while i<len(seq):
			if seq[i]=='a':
				transcrit='t'+transcrit
			elif seq[i]=='t':
				transcrit='a'+transcrit
			elif seq[i]=='c':
				transcrit='g'+transcrit
			elif seq[i]=='g':
				transcrit='c'+transcrit
			else:
				print "x"
				#transcrit='x'+transcrit
			i=i+1
		nom=raw_input("entrer le nom du fichier ou sauvgarder ")
		f=open(	nom,"w")
		f.write(transcrit[0:len(transcrit)])
		f.close()
			
		

	elif choix ==1:
		nom = raw_input(" saisir nom du fichier  ")
		f=open(nom,"r")
		line=f.readline().rstrip("\n")
		seq=""
		while line != "":
			seq=seq+line
			line=f.readline().rstrip("\n")
		# [0:4] de 0 a 4 exclu
		#line=f.readline.rstrip("\n")
		f.close()
		print seq
		seq=seq.lower()
		transcrit=seq
		transcrit=transcrit.replace("t","u")
		
		nom=raw_input("entrer le nom du fichier ou sauvgarder ")
		f=open(	nom,"w")
		f.write(transcrit[0:len(transcrit)])
		f.close()
		
		
		
	else:
		print ""
