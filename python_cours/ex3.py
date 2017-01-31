

ch_u=raw_input("entrer une grande chaine de char ")
ch=ch_u.lower()
ch_size=len(ch)
a=ch.count('a')/(ch_size*1.0)
c=ch.count('c')/(ch_size*1.0)
g=ch.count('g')/(ch_size*1.0)
t=ch.count('t')/(ch_size*1.0)
x=(ch_size -a -c -g -t)/(ch_size*1.0)

print a,"% de a",c,"% de c",g,"% de g",t,"% de t","\n il y a aussi ",x,"%de bouse"






