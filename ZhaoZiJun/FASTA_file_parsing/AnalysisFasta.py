class AnalysisFasta:
    """
    class AnalysisFasta  FASTA类型文件解析类
    包含以下方法
    __init__(self, path)
    将目的文件所在路径保存至class中
    
    showPath(self)
    测试方法，确保path成功传入
    
    readFastaFile(self)
    读取指定目录下的FASTA文件，并将序列的名称、注释信息、蛋白质序列保存至列表dataList中
    
    showData(self)
    将列表dataList中的内容输出在控制台，并在前面加注标识
    
    writeInTxt(self)
    将列表dataList中的全部内容写入文件'data.txt'中
    
    writeSpcificData(self,item)
    将列表dataList中的指定内容写入文件'specificData.txt'中,
    item为name,info,protein分别对应列的名称、注释信息、蛋白质序列
    
    showSpcificData(self,item)
    返回列表dataList中的指定内容的生成器,
    item为name,info,protein分别对应列的名称、注释信息、蛋白质序列
    """
    
    dataList = []
    dataID = ['name','info','protein']
    def __init__(self, path):
        self.path = path
        
    def showPath(self):
        print('path : ' + self.path);
        
    def readFastaFile(self):
        f=open(self.path)
        data=[]
        _sequence=''
        for line in f:
            if line.startswith('>'):
                if _sequence != '':
                    data.append(_sequence)
                    self.dataList.append(data)
                    data=[]
                    _sequence = ''
                name=line.replace('>','').split()[0]
                info=line.split()[1:]
                data.append(name)
                data.append(info)
                
            else:
                _sequence+=line.replace('\n','').strip()
        data.append(_sequence)
        self.dataList.append(data)

        f.close()

    def showData(self):
        for data in self.dataList:
            for i in range(3):
                print(str(self.dataID[i]) + ' : ' + str(data[i]))
            print('\n')
            
    def writeInTxt(self):
        file_output = open('data.txt','w')
        for data in self.dataList:
            for i in range(3):
                file_output.write(str(self.dataID[i]) + ':' +str(data[i]) + '\n')
            file_output.write('\n')
        file_output.close()
    
    def writeSpcificData(self,item):
        name_output = open('specificData.txt','w')
        pos = self.dataID.index(item)
        for data in self.dataList:
                name_output.write(str(data[pos]) + '\n')
        name_output.write('\n')
    
    def showSpcificData(self,item):
        pos = self.dataID.index(item)
        for data in self.dataList:
            yield data[pos]
            
    