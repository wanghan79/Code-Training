import os

#tag = "test"
#tag = "valid"
tag = "train"

fastaFile = open(tag+"_data/"+tag+".fasta","r")
outPath = "DMCdata/"+tag+"_fasta/"
for line in fastaFile:
    if line.startswith('>'):
        a = line.split('>')[-1].split('\n')[0]
        tempOut = open(outPath+a+".fasta","w")
        tempOut.write(line)
    else:
        tempOut.write(line.upper())
		
	
