'''
    python download method
    Attention:
    The path must contain the filename that stored
    the data. eg:'/Users/roarboil/Desktop/kkk.html'
    Author : BaoYihang
    '''
import requests
class FileDownload(object):
    @classmethod
    def download(cls,file_url,file_path):
        r = requests.get(file_url, stream=True)
        with open(file_path, "wb") as fil:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    fil.write(chunk)
if __name__ == '__main__':
    url = input("Please input url")
    path = input("Please input path")
    FileDownload.download(url,path)
    print("done")
