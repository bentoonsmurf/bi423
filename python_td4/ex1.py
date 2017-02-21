# lecture ligne par ligne

nom = raw_input(" saisir nom du fichier  ")

f=open(nom,"r")
line=f.readline()
concat_line=""
while line != "":
	print line
	concat_line=concat_line+line[0:len(line)-1]
	line=f.readline()
# [0:4] de 0 a 4 exclu
#line=f.readline.rstrip("\n")
f.close()
print concat_line







