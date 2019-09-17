class read_fasta:
    '''
    FASTA类型文件解析类

    read(self,fp)
    输入文件路径
    返回三个信息分别为序列的名称、注释信息、蛋白质序列

    print_save(self,fp)
    输入文件路径
    方法中调用read方法
    将解析过的文件信息存入data.txt中
    同时输出

    '''
    def read(self,fp):
        '''
        :param fp: 输入文件路径
        :return:返回序列的名称、注释信息、蛋白质序列
        '''
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

    def print_save(self,fp):
        '''
        :param fp: 输入文件路径
        :return: 输出序列的名称、注释信息、蛋白质序列
                 并存入文件
        '''
        fo = open("data.txt", "w")
        for name, name1, name2, seq in self.read(fp):
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
            fo.write("\n")
            print("name ", name1, "\n", " ", "INFO ", name2, "\n", " ", "seq ", seq)
        fo.close()