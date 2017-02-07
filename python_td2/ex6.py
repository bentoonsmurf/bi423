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
i=0
seq=seq.replace(" ","")
while seq[i]==seq[len(seq)-1-i]and i<len(seq)/2:
	i=i+1

if i==len(seq)/2:
	print "c'est un palindrome"
else:
	print "cest pas un palindrome"



