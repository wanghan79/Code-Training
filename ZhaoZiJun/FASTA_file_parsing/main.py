import AnalysisFasta as AF

MyClass = AF.AnalysisFasta('Felis_catus.Felis_catus_9.0.dna.chromosome.MT.fa')

MyClass.showPath()
MyClass.readFastaFile()
MyClass.showData()
MyClass.writeInTxt()
MyClass.writeSpcificData('name')

for data in MyClass.showSpcificData('name'):
    print(str(data))