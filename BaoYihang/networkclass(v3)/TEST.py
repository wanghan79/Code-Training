'''
    Test method
    Author : BaoYihang
'''
from networkclass import Download

my_ftp = Download("172.28.180.117", 21)
my_ftp.login("ouyangpeng", "ouyangpeng")
    
# download single file
my_ftp.download_file("G:/ftp_test/XTCLauncher.apk", "/App/AutoUpload/ouyangpeng/I12/Release/XTCLauncher.apk")

# download the whole dictionary
my_ftp.download_file_tree("G:/ftp_test/", "App/AutoUpload/ouyangpeng/I12/")
    
my_ftp.close()

my_http = Download('https://www.uniprot.org/uniprot/A1WYA9.xml')
my_http.get_file('https://www.uniprot.org/uniprot/A1WYA9.xml')