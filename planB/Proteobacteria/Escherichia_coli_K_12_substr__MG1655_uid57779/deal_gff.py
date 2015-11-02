import re

f=open('NC000913.gff','w')

for i in open('NC_000913.gff','r').readlines():
    if 'NC_000913.3' in i:
        if 'RefSeq	gene' in i:
            r1=re.findall('(ID=.*?)\n',i)
            r2=re.findall('RefSeq	gene	([0-9]*?)	',i)
            r3=re.findall('	([0-9]*?)	\.	',i);print(r3[0])
            f.write(r1[0]+'	'+r2[0]+'	'+r3[0]+"\n")
        elif 'RefSeq	exon' in i:
            r1=re.findall('(ID=.*?)\n',i)
            r2=re.findall('RefSeq	exon	([0-9]*?)	',i)
            r3=re.findall('	([0-9]*?)	\.	',i)
            f.write(r1[0]+'	'+r2[0]+'	'+r3[0]+"\n")