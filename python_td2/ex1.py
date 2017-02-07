
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
i=0
while i<len(seq):
	print bcolors.red + seq[i] + bcolors.end
	i=i+1
	print "a la position ", i
	






