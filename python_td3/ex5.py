alphabet='atcg'


class bcolors:
	red= '\033[91m'
	end= '\033[0m'
	vert ='\033[92m'
	bleu ='\033[94m'
	violet = '\033[95m'
	bleu_clair = '\033[96m'
	#test = '\033[95m'
	#test = '\033[95m'
	
seq=raw_input(bcolors.bleu +'entrer une chaine de char ' + bcolors.end)
seq=seq.lower()
tolerence=input( 'combien d erreur vous acceptez ? ')
i=0
n=0
t=''
while i<len(seq) and n<=tolerence:
	if seq[i] not in alphabet:
		print seq[i],"a la position ",i+1
		n+=1
		t=t+seq[i]
	else:
		if seq[i]=='a':
			t=t+'A'
		elif seq[i]=='t':
			t=t+'T'
		elif seq[i]=='c':
			t=t+'C'
		else:
			t=t+'G'
	i+=1
	
if n>tolerence:
	print "il y a trop d'erreur"
else:
	print "il y a ",n,"erreur"
	print t[:]







