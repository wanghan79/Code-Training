'''
    Test method for networkclass vision 1.4
    Author : BaoYihang
'''
from networkclass import Download

@Download('https://www.uniprot.org/uniprot/A1WYA9.xml')
#Download("172.28.180.117", 21)
def test1():
    print('done!')
test1()
