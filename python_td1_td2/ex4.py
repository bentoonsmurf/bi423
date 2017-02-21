#count et in

g_ch=raw_input("entrer une grande chaine de char ")
s_ch=raw_input("entrer une petite chaine de char ")
g=g_ch.lower()
s=s_ch.lower()
if s in g :
	print "tout va bien",s,"est dans",g
else:
	print s,"n'est pas dans",g
	
if g.count(s) !=0:
	print "present"
else:
	print"absent"
	



