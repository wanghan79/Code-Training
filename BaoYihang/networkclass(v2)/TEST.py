'''
    Test method
    Author : BaoYihang
'''
from networkclass import Download_F
from networkclass import Download_h

my_ftp = Download_F("172.28.180.117")
my_ftp.login("ouyangpeng", "ouyangpeng")
    
# 下载单个文件
my_ftp.download_file("G:/ftp_test/XTCLauncher.apk", "/App/AutoUpload/ouyangpeng/I12/Release/XTCLauncher.apk")

# 下载目录
my_ftp.download_file_tree("G:/ftp_test/", "App/AutoUpload/ouyangpeng/I12/")
    
my_ftp.close()
my_http = Download_h('https://www.uniprot.org/uniprot/A1WYA9.xml')
my_http.get_file('https://www.uniprot.org/uniprot/A1WYA9.xml')