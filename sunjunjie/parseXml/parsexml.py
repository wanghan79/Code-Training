import xml.etree.ElementTree as ET
import sys
from xml.sax.handler import ContentHandler
from xml.sax import make_parser

# 三引号中的代码为不封装方法的测试样例
'''
#打开xml文件
#如下两行代码在后期会重复使用，后面的操作就不用重复书写
tree = ET.parse("test1.xml")
root = tree.getroot()    #获取根节点

print(root.tag)      #打印根节点的值
print(root.attrib)   #打印属性值

#利用findall方法获取所有子节点，返回的节点会存在一个列表里
nodes = root.findall('province')

for node in nodes:
    print('节点名称', node.tag)
    print('节点属性值：', node.attrib)

#直接利用遍历的方法去直接遍历子节点的所有元素

for node in root:    #遍历二级节点
    print("二级节点{}的属性{}：".format(node.tag, node.attrib))
    print('三级节点的获取：')
    for sub_node in node:
        print("{}={},".format(sub_node.tag, sub_node.attrib, end=''))  # 可将sub_node.attrib被sub_node.text
    print('\n')
'''

#上述代码可以封装进class中

#传递一个参数file_path
#实现元素的读取，返回列表形式的数据，并且列表里面存储每个page节点的信息;
#@input ：file_path: 文件路径
class XmlUtil:
    def get_page(self, file_path):
        tree = ET.parse(file_path)
        root = tree.getroot()
        return root

    def __init__(self, file_path):
        self.filepath = file_path


    def getConfig(self, file_path):
        config = {'root': self.get_page(file_path),
                  'file_path': file_path
                  }
        return config

# page_key_word，存储页面信息;
# uiElement存储列表数据
class page:
    page_key_word = {}
    uiElment = {}
    def __init__(self, page_key_word={}, uiElment={}):
        self.page_key_word = page_key_word
        self.uiElment = uiElment

    # 检查xml文件是否有错误
    # @file_path : 文件的路径
    def haveError(self, file_path):
        parser = make_parser()
        flag = 1
        try:
            parser.setContentHandler(ContentHandler())
            parser.parse(file_path)
            print('\n\t:), %s is OK!\n' % file_path)
        except Exception as e:
            print('\n\t:(,  Error found in file:%s\n' % e)
            flag = 0
        return flag


class UiElement:
    list_attrib = {}
    #得到所有的属性值
    def getAttrib(self, root):
        for node in root:  # 遍历二级节点
            print("二级节点{}的属性{}：".format(node.tag, node.attrib))
            print('三级节点的获取：')
            for sub_node in node:
                print("{}={},".format(sub_node.tag, sub_node.attrib, end=''))  # 可将sub_node.attrib被sub_node.text
            print('\n')

    #找到指定属性值的来源
    # @input root: etree生成的根节点   attrib : 需要查询的属性值
    def get_someAttrib(self, root, attrib):
        config_attrib = [{root.tag:root.attrib}]
        for node in root:
            for sub_node in node:
                if(sub_node == attrib):
                    lastlevel = {node.tag: node.attrib}
                    currentLevel = {sub_node.tag: sub_node.attrib}
                    config_attrib.append(lastlevel)
                    config_attrib.append(currentLevel)

        if config_attrib == [{root.tag: root.attrib}]:
            print('没有该属性值')
            return None
        return config_attrib


if __name__ == '__main__':
    file_path = 'test1.xml'
    page = page()
    flag = page.haveError(file_path)
    if flag:
        xml = XmlUtil(file_path)
        root = xml.get_page(file_path)
        ui = UiElement()
        ui.getAttrib(root)



