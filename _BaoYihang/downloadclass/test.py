from networkclass import FileDownload
url = input("Please input url")
path = input("Please input path")
FileDownload.download(url,path)
print("done")