# -*- coding:utf-8 -*-
import sys

from lxml import html
import time

etree = html.etree

def fast_iter(context, func, tag = None ,*args, **kwargs):
    """
    读取xml数据，并释放空间
    :params context: etree.iterparse生成的迭代器
    :params func:处理xml数据的func
    """
    # 事件、元素
    for event, elem in context:
        # 处理xml数据
        if tag is not None:
            func(elem, tag, *args, **kwargs)
        else:
            func(elem, *args, **kwargs)
        # 重置元素，清空元素内部数据
        elem.clear()
        # 选取当前节点的所有先辈（父、祖父等）以及当前节点本身
        for ancestor in elem.xpath('ancestor-or-self::*'):
            # 如果当前节点还有前一个兄弟，则删除父节点的第一个子节点。getprevious():返回当前节点的前一个兄弟或None。
            while ancestor.getprevious() is not None:
                # 删除父节点的第一个子节点，getparent()：返回当前节点的父元素或根元素或None。
                del ancestor.getparent()[0]
    # 释放内存
    del context


def process_element(elem):
    """
    处理element
    :params elem: Element
    """
    # 储存基因列表
    gene_list = []
    for i in elem.xpath('.//*[local-name()="gene"]/*[local-name()="name"]'):
        # 获取基因名字
        gene = i.text
        # 添加到列表
        gene_list.append(gene)

    print('gene', gene_list)

def process_element1(elem, tag):
    """
    处理element
    :params elem: Element
     """
    # 储存基因列表
    tag_list = []
    for i in elem.xpath('.//*[local-name()="%s"]/*[local-name()="name"]'%tag):
        # 获取基因名字
        tag1 = i.text
        # 添加到列表
        tag_list.append(tag1)

    print('%s'%tag, tag_list)


class Logger(object):
    def __init__(self, fileN="Default.log"):
        self.terminal = sys.stdout
        self.log = open(fileN, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass

if __name__ == '__main__':
    sys.stdout = Logger("D:\\log1.txt")  # 这里我将Log输出到D盘
    # 下面所有的打印，只要控制台输出，都将写入"D:\\log1.txt"
    print('start', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    start = time.time()

    # 文件路径
    infile = r'uniprot_sprot.xml'
    # 通过迭代读取xml，带命名空间的要加上命名空间
    context = etree.iterparse(infile, events=('end',), encoding='UTF-8', tag='{http://uniprot.org/uniprot}entry')
    # 快速读取xml数据
    # fast_iter(context, process_element)

    fast_iter(context, process_element1, 'gene')

    print('stop', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    print('time', time.time() - start)