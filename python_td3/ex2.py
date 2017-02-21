
class bcolors:
	red= '\033[91m'
	end= '\033[0m'
	vert ='\033[92m'
	bleu ='\033[94m'
	violet = '\033[95m'
	bleu_clair = '\033[96m'
	#test = '\033[95m'
	#test = '\033[95m'

#remplacer t en u

seq=raw_input(bcolors.bleu +'entrer une chaine de char ' + bcolors.end)

seq=seq.lower()
i=0
transcrit=""
while i<len(seq):
	if seq[i]=='a':
		print bcolors.bleu + seq[i] + bcolors.end
		transcrit=transcrit+seq[i]
	elif seq[i]=='t':
		print bcolors.red + 'u' + bcolors.end
		transcrit=transcrit+'u'
	elif seq[i]=='c':
		print bcolors.bleu + seq[i] + bcolors.end
		transcrit=transcrit+seq[i]
	else:
		print bcolors.bleu + seq[i] + bcolors.end
		transcrit=transcrit+seq[i]
	
	i=i+1
	
print transcrit[:]
	
	
	
