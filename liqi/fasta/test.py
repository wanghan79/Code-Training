def read_fasta(fp):
    name, seq = None, []
    for line in fp:
        line = line.rstrip()
        if line.startswith(">", 0):
            if name:
                yield (name,name1,name2, ''.join(seq))
            name = line[1:]
            name = name.split(' ')
            name1 = name[0]
            if len(name) == 1:
                name2 = "NULL"
            else:
                name2 = name[1]
        else:
            seq.append(line)
    if name:
        yield (name,name1,name2, ''.join(seq))
fo = open("data.txt", "w")
with open('test.fasta') as fp:
    for name,name1,name2, seq in read_fasta(fp):
        fo.write(name1)
        fo.write("\n")
        fo.write(" ")
        fo.write("\n")
        fo.write(name2)
        fo.write("\n")
        fo.write(" ")
        fo.write("\n")
        fo.write(seq)
        fo.write("\n")
        print("name ",name1,"\n"," ","INFO ",name2,"\n"," ","seq ",seq,"\n")
fo.close()