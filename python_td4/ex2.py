# lecture ligne par ligne

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


ch=seq
ch_size=len(ch)
a=ch.count('a')/(ch_size*1.0)
c=ch.count('c')/(ch_size*1.0)
g=ch.count('g')/(ch_size*1.0)
t=ch.count('t')/(ch_size*1.0)
x=(ch_size -a -c -g -t)/(ch_size*1.0)

print a,"% de a",c,"% de c",g,"% de g",t,"% de t","\n il y a aussi ",x,"%de bouse"

nom2=raw_input("entrer une grande chaine de char ")
fic=open(nom2,"w")
fic.write(str(a)+"% de a"+str(c)+"% de c"+str(g)+"% de g"+str(t)+"% de t"+"\n il y a aussi "+str(x)+"%de bouse")

