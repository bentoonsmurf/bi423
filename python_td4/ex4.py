# nb seq 
#longueur moyenne
nb=0
longueur_total=0
name=raw_input("enter file namme")
f=open(name,"r")
line=f.readline().rstrip("\n")
seq=""
while line != "":
	line=f.readline().rstrip("\n")
	nb=nb+1
	longueur_total=longueur_total+len(line)
		# [0:4] de 0 a 4 exclu
		#line=f.readline.rstrip("\n")
f.close()

moy=longueur_total/nb*1.0
print "la moyenne est de", moy,"il y a ",nb,"sequances"
