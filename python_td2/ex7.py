
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
transcrit=""
while i<len(seq):
	if seq[i]=='a':
		print bcolors.bleu + seq[i] + bcolors.end
		transcrit='t'+transcrit
	elif seq[i]=='t':
		print bcolors.bleu + 'a' + bcolors.end
		transcrit='a'+transcrit
	elif seq[i]=='c':
		print bcolors.bleu + seq[i] + bcolors.end
		transcrit='g'+transcrit
	elif seq[i]=='g':
		print bcolors.bleu + seq[i] + bcolors.end
		transcrit='c'+transcrit
	else:
		print "x"
		#transcrit='x'+transcrit
	i=i+1

print seq[:]
print transcrit[:]
i=0
while seq[i]==transcrit[i]:
	i=i+1
	
if i==len(seq)/2:
	print "c'est un palindrome bizard"
else:
	print "cest pas un palindrome"


