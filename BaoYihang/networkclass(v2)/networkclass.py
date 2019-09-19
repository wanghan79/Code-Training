'''
    python download method
    For Ftp download and http download
    Author : BaoYihang
'''
from __future__ import with_statement
import requests
import re
import os
import sys
from ftplib import FTP
import time
import socket
import urllib

dfltSite = 'home.rmi.net'
dfltRdir = '.'
dfltUser = 'lutz'

class Download_F:
    def __init__(self, host, port=21):

        self.host = host
        self.port = port
        self.ftp = FTP()
        self.ftp.encoding = 'gbk'
        self.log_file = open("log.txt", "a")
        self.file_list = []

    def login(self, username, password):
        try:
            timeout = 60
            socket.setdefaulttimeout(timeout)
            self.ftp.set_pasv(True)
            self.debug_print('开始尝试连接到 %s' % self.host)
            self.ftp.connect(self.host, self.port)
            self.debug_print('成功连接到 %s' % self.host)

            self.debug_print('开始尝试登录到 %s' % self.host)
            self.ftp.login(username, password)
            self.debug_print('成功登录到 %s' % self.host)

            self.debug_print(self.ftp.welcome)
        except Exception as err:
            self.deal_error("FTP 连接或登录失败 ，错误描述为：%s" % err)
            pass

    def is_same_size(self, local_file, remote_file):
        try:
            remote_file_size = self.ftp.size(remote_file)
        except Exception as err:
            remote_file_size = -1

        try:
            local_file_size = os.path.getsize(local_file)
        except Exception as err:
            local_file_size = -1

        self.debug_print('local_file_size:%d  , remote_file_size:%d' % (local_file_size, remote_file_size))
        if remote_file_size == local_file_size:
            return 1
        else:
            return 0

    def download_file(self, local_file, remote_file):
        self.debug_print("download_file()---> local_path = %s ,remote_path = %s" % (local_file, remote_file))

        if self.is_same_size(local_file, remote_file):
            self.debug_print('%s 文件大小相同，无需下载' % local_file)
            return
        else:
            try:
                self.debug_print('>>>>>>>>>>>>下载文件 %s ... ...' % local_file)
                buf_size = 1024
                file_handler = open(local_file, 'wb')
                self.ftp.retrbinary('RETR %s' % remote_file, file_handler.write, buf_size)
                file_handler.close()
            except Exception as err:
                self.debug_print('下载文件出错，出现异常：%s ' % err)
                return

    def download_file_tree(self, local_path, remote_path):
        print("download_file_tree()--->  local_path = %s ,remote_path = %s" % (local_path, remote_path))
        try:
            self.ftp.cwd(remote_path)
        except Exception as err:
            self.debug_print('远程目录%s不存在，继续...' % remote_path + " ,具体错误描述为：%s" % err)
            return

        if not os.path.isdir(local_path):
            self.debug_print('本地目录%s不存在，先创建本地目录' % local_path)
            os.makedirs(local_path)

        self.debug_print('切换至目录: %s' % self.ftp.pwd())

        self.file_list = [] 
        self.ftp.dir(self.get_file_list)

        remote_names = self.file_list
        self.debug_print('远程目录 列表: %s' % remote_names)
        for item in remote_names:
            file_type = item[0]
            file_name = item[1]
            local = os.path.join(local_path, file_name)
            if file_type == 'd':
                print("download_file_tree()---> 下载目录： %s" % file_name)
                self.download_file_tree(local, file_name)
            elif file_type == '-':
                print("download_file()---> 下载文件： %s" % file_name)
                self.download_file(local, file_name)
            self.ftp.cwd("..")
            self.debug_print('返回上层目录 %s' % self.ftp.pwd())
        return True

    def close(self):
        self.debug_print("close()---> FTP退出")
        self.ftp.quit()
        self.log_file.close()

    def debug_print(self, s):
        self.write_log(s)

    def deal_error(self, e):
        log_str = '发生错误: %s' % e
        self.write_log(log_str)
        sys.exit()

    def write_log(self, log_str):
        time_now = time.localtime()
        date_now = time.strftime('%Y-%m-%d', time_now)
        format_log_str = "%s ---> %s \n " % (date_now, log_str)
        print(format_log_str)
        self.log_file.write(format_log_str)

    def get_file_list(self, line):
        file_arr = self.get_file_name(line)
        if file_arr[1] not in ['.', '..']:
            self.file_list.append(file_arr)

    def get_file_name(self, line):
        pos = line.rfind(':')
        while (line[pos] != ' '):
            pos += 1
        while (line[pos] == ' '):
            pos += 1
        file_arr = [line[0], line[pos:]]
        return file_arr

#下面是利用url下载http文件或目录下所有文件
class Download_h:
    def __init__(self,url):
        self.url = url
    def isFile(self,url):
        if url.endswith('/'):
            return False
        else:
            return True
    def download(self,url):
        full_name = url.split('//')[-1]
        filename = full_name.split('/')[-1]
        dirname = "/".join(full_name.split('/')[:-1])
        if os.path.exists(dirname):
            pass
        else:
            os.makedirs(dirname, exist_ok=True)
        urllib.request.urlretrieve(url, full_name)
    def get_url(self,base_url):
        text = ''
        try:
            text = requests.get(base_url).text
        except Exception as e:
            print("error - > ",base_url,e)
            pass
        reg = '<a href="(.*)">.*</a>'
        urls = [base_url + url for url in re.findall(reg, text) if url != '../']
        return urls
    def get_file(self,url):
        if self.isFile(url):
            print(url)
            try:
                self.download(url)
            except:
                pass
        else:
            urls = self.get_url(url)
            for u in urls:
                self.get_file(u)
