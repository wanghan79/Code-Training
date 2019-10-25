import os

#python3 Executable.py -s /home/liq/zzj/Topo/DMCTOP/DMCTOP/example/4n6h_A.fasta -p /home/liq/zzj/Topo/DMCTOP/DMCTOP/example/4n6h_A.pssm -m /home/liq/zzj/Topo/DMCTOP/DMCTOP/data/model.h5


shFile = open("shDMC.sh","w")

shFile.write("#!/bin/bash\n")

def addSh(tag):
	fastaPath = "DMCdata/"+tag+"_fasta/"
	dataList = os.listdir(fastaPath)
	for data in dataList:
		mark = data.split('.')[0]
		shFile.write("python3 Executable.py -s /home/liq/zzj/Topo/DMCdata/"+tag+"_fasta/"+mark+".fasta -p /home/liq/zzj/Topo/PSSM/"+tag+"/"+mark+".pssm -m /home/liq/zzj/Topo/DMCTOP/DMCTOP/data/model.h5"+" &&\n")


if __name__ == "__main__":
	addSh("test")
	addSh("valid")
	addSh("train")
	shFile.write("echo \"\n**************\n* finished!! *\n**************\"")
