a = input("Enter the genetic code sequence of the template strand: ").upper()
b = ''
for base in a:
    if base == "A":
        b += 'U'
    elif base == "C":
        b += 'G'
    elif base == "T":
        b += 'A'
    elif base == "G":
        b += 'C'
#print("Genetic sequence of the Coding Strand is: ", b,'\n')
print("Sequence of the mRNA is:", b,'\n')

c = []
while len(b) >= 3:
    codon = b[:3]
    c.append(codon)
    b = b[3:]
    #print(codon)
print("The codon triplets are:", c,'\n')

aa = []
for codon in c:
    if codon == "AUG":
        aa.append("Met")
    elif codon in ["UUU", "UUC"]:
        aa.append("Phe")
    elif codon in ["UUA", "UUG", "CUU", "CUC", "CUA", "CUG"]:
        aa.append("Leu")
    elif codon in ["AUU", "AUC", "AUA"]:
        aa.append("Ile")
    elif codon in ["GUU", "GUC", "GUA", "GUG"]:
        aa.append("Val")
    elif codon in ["UCU", "UCC", "UCA", "UCG", "AGU", "AGC"]:
        aa.append("Ser")
    elif codon in ["CCU", "CCC", "CCA", "CCG"]:
        aa.append("Pro")
    elif codon in ["ACU", "ACC", "ACA", "ACG"]:
        aa.append("Thr")
    elif codon in ["GCU", "GCC", "GCA", "GCG"]:
        aa.append("Ala")
    elif codon in ["UAU", "UAC"]:
        aa.append("Tyr")
    elif codon in ["CAU", "CAC"]:
        aa.append("His")
    elif codon in ["CAA", "CAG"]:
        aa.append("Gln")
    elif codon in ["AAU", "AAC"]:
        aa.append("Asn")
    elif codon in ["AAA", "AAG"]:
        aa.append("Lys")
    elif codon in ["GAU", "GAC"]:
        aa.append("Asp")
    elif codon in ["GAA", "GAG"]:
        aa.append("Glu")
    elif codon in ["UGU", "UGC"]:
        aa.append("Cys")
    elif codon == "UGG":
        aa.append("Trp")
    elif codon in ["CGU", "CGC", "CGA", "CGG", "AGA", "AGG"]:
        aa.append("Arg")
    elif codon in ["GGU", "GGC", "GGA", "GGG"]:
        aa.append("Gly")
    elif codon in ["UAA", "UAG", "UGA"]:
        aa.append("*")

print(" Raw sequence is:", ", ".join(aa),'\n')
f=1
temp=[]
tt= aa

'''for i in aa:
    if i == 'Met':
        start = +1
    if i == '*':
        stop= +1
if start == stop or start<=stop or start>=stop:'''

for i in range(0,len(tt)):
        if tt[i]== 'Met':            
            j=i+1
            for n in range(j, len(tt)):
                if aa[n] != "*":
                    temp.append(tt[n])
                else :
                    break                    
            print("The",f,"amino acid sequence is","-".join(temp)  )
            temp=[]
            f=f+1           