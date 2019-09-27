# -*- coding:utf-8 -*-
'''
	File Name：     xml_TOPO_capturer
	Description :   find the topo sequence from xml files
	Author :        Zhao ZiJun
	date：          2019/9/25 
'''

import os

########################################################################
class xml_TOPO_capturer(object):

    def __init__(self):
        pass

    def mains1s2Others(self):
        '''
        将side1为1，side2为2，其他全部视为3，进行label提取
        '''
        fulllist = open("full_pdbtm_list.txt", "r")
        for line in fulllist:
            #print('line:')
            filename=line[0:4]
            chainID=line[5]
            #print('name:'+str(filename)+' chainID:'+str(chainID))
            
            if(os.path.exists("xmlfiles/" + str(filename) + ".xml") == False):
                print('no '+str(filename)+'.xml')
                continue
            
            dataFile = open("xmlfiles/" + str(filename) + ".xml","r")
            for dataLine in dataFile:
                #print('in')
                if dataLine.startswith('  <CHAIN'):
                    #print('get CHAIN '+ str(dataLine[17:20])+str(dataLine.split("\"")[1]))
                    file_output = open("topoThreeType/"+str(filename)+'_'+str(dataLine.split("\"")[1])+'.type',"w")
                if dataLine.startswith('  </CHAIN>'):
                    file_output.close()
                if dataLine.startswith('    <REGION'):
                    #print(str(dataLine.split("\"")[1])+'  '+str(dataLine.split("\"")[3])
                    #      +'  '+str(dataLine.split("\"")[-2]))
                    seq_beg = dataLine.split("\"")[1]
                    seq_end = dataLine.split("\"")[5]
                    #print(seq_beg+' '+seq_end)
                    t = dataLine.split("\"")[-2]
                    if(str(t) == "1"):
                        type = 1
                    elif(str(t) == "2"):
                        type = 2
                    else:
                        type = 3
                    for i in range(int(seq_beg)-1,int(seq_end)):
                        file_output.write(str(type) + "\n")
            #break
        fulllist.close()
        
    def mainEveryType(self):
        '''
        统计所有的拓扑类型
        类型‘1’为1，类型‘2’为2，类型‘B’为3，
        类型'I'为4，类型'H'为5，类型'F'为6
        类型'U'为7，类型'L'为8，类型'C'为9
        进行label提取
        '''
        fulllist1 = open("full_pdbtm_list.txt", "r")
        fulllist2 = open("full_pdbtm_list.txt", "r")
        AllTypes={"1":1,"2":2}
        id = 3
        for line in fulllist1:
            #print('line:')
            filename=line[0:4]
            chainID=line[5]
            #print('name:'+str(filename)+' chainID:'+str(chainID))
            
            if(os.path.exists("xmlfiles/" + str(filename) + ".xml") == False):
                print('no '+str(filename)+'.xml')
                continue
            
            dataFile = open("xmlfiles/" + str(filename) + ".xml","r")
            for dataLine in dataFile:
                if dataLine.startswith('    <REGION'):
                    t = dataLine.split("\"")[-2]
                    if AllTypes.__contains__(str(t)) == False:
                        AllTypes[str(t)] = id
                        id = id+1
                        
        print(AllTypes)
        
        for line in fulllist2:
            #print('line:')
            filename=line[0:4]
            chainID=line[5]
            #print('name:'+str(filename)+' chainID:'+str(chainID))
            
            if(os.path.exists("xmlfiles/" + str(filename) + ".xml") == False):
                print('no '+str(filename)+'.xml')
                continue
            
            dataFile = open("xmlfiles/" + str(filename) + ".xml","r")
            for dataLine in dataFile:
                #print('in')
                if dataLine.startswith('  <CHAIN'):
                    #print('get CHAIN '+ str(dataLine[17:20])+str(dataLine.split("\"")[1]))
                    file_output = open("topoEveryType/"+str(filename)+'_'+str(dataLine.split("\"")[1])+'.type',"w")
                if dataLine.startswith('  </CHAIN>'):
                    file_output.close()
                if dataLine.startswith('    <REGION'):
                    #print(str(dataLine.split("\"")[1])+'  '+str(dataLine.split("\"")[3])
                    #      +'  '+str(dataLine.split("\"")[-2]))
                    seq_beg = dataLine.split("\"")[1]
                    seq_end = dataLine.split("\"")[5]
                    #print(seq_beg+' '+seq_end)
                    t = dataLine.split("\"")[-2]
                    type = AllTypes[str(t)]
                    for i in range(int(seq_beg)-1,int(seq_end)):
                        file_output.write(str(type) + "\n")        
        
            #break
        fulllist1.close()  
        fulllist2.close() 

########################################################################
if __name__ == "__main__": 
    capturer = xml_TOPO_capturer()
    capturer.mains1s2Others()
    capturer.mainEveryType()