from Utilities.MultiProcess.MultiThread import thread_manager
import os
import PDBParser.ParserBase
import Utilities.Compression.Uncompress as us


def func():
    pass


def file_open(file_name, q):
    """ file reade thread"""
    ppb = PDBParser.ParserBase.ParserBase(func)
    result = ppb.parser(file_name, target="ALL")
    if result != {}:
        q.put(result)
    return 0


def get_filelist(dir,Filelist):
    '''
    :param dir:
    :param Filelist:
    :return:a list of files to be parse
    '''
    newDir = dir
    if os.path.isfile(dir):
        Filelist.append(dir)
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            newDir = os.path.join(dir, s)
            get_filelist(newDir, Filelist)
    return Filelist


@thread_manager
def file_parser(path):
    '''
    open threads
    '''

    dirlist = os.listdir(path)
    filelist = []
    for dir in dirlist:
        dir = os.path.join(path, dir)
        filelist = get_filelist(dir, filelist)
    print(filelist)
    thread_list = []
    for i in filelist:
        thread_list.append([file_open, i])
    return thread_list


def main():
    # path = input("please input file direction:\n")
    path = r"PDBtest"
    us.un_gz_all(r"PDBtest")
    """uncompress files"""
    result = file_parser(path)
    print(len(result))


if __name__ == '__main__':
    main()