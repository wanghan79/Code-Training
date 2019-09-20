#!/usr/bin/python
# -*- coding: UTF-8 -*-

import xml.sax

class MovieHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.type = ""
        self.format = ""
        self.year = ""
        self.rating = ""
        self.stars = ""
        self.description = ""

    def openfile(self):
        self.f = open('text.txt', 'a+')

    def closefile(self):
        self.f.close()

    # 元素开始事件处理
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "movie":
            self.f.write('*****Movie*****\n')

            title = attributes["title"]

            self.f.write('Title:%s\n' % title)

    # 元素结束事件处理
    def endElement(self, tag):
        if self.CurrentData == "type":
            self.f.write('Type:%s\n' % self.type)


        elif self.CurrentData == "format":
            self.f.write('Format:%s\n' % self.format)


        elif self.CurrentData == "year":
            self.f.write('Year:%s\n' % self.year)


        elif self.CurrentData == "rating":
            self.f.write('Rating:%s\n' % self.rating)

        elif self.CurrentData == "stars":
            self.f.write('Stars:%s\n' % self.stars)

        elif self.CurrentData == "description":
            self.f.write('Description:%s\n' % self.description)

        self.CurrentData = ""

    # 内容事件处理
    def characters(self, content):
        if self.CurrentData == "type":
            self.type = content
        elif self.CurrentData == "format":
            self.format = content
        elif self.CurrentData == "year":
            self.year = content
        elif self.CurrentData == "rating":
            self.rating = content
        elif self.CurrentData == "stars":
            self.stars = content
        elif self.CurrentData == "description":
            self.description = content


if __name__ == "__main__":
    # 创建一个 XMLReader
    parser = xml.sax.make_parser()
    # turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    Handler = MovieHandler()

    Handler.openfile()
    # 重写 ContextHandler
    parser.setContentHandler(Handler)
    #加载xml文件
    parser.parse("test.xml")

    Handler.closefile()
