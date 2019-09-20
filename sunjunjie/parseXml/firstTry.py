import re


class XmlTree:
    def __init__(self):
        self.tag = ""
        self.text = ""
        self.attrs = {}
        self.children = []
        self.parent = None
    # 通过标签名字找到元素
    # @input: name   标签名字
    def findElementsByTagName(self, name):
        children = self.children[:]
        trees = []
        for child in children:
            if (child.tag == name):
                trees.append(child)
            sub = child.children[:]
            for i in sub:
                children.append(i)
        return trees
    # 查询attrs列表中是否有相应的属性与input相匹配
    # @input: attr   属性值
    def hasAttribute(self, attr):
        has = False
        # 遍历属性列表
        for key, value in self.attrs.items():
            # 将属性前后的引号去掉
            if (key == attr.strip("\"")):
                has = True
                break
        return has
    # 获取属性
    def getAttribute(self, attr):
        # 查询是否有该属性值
        # 如果返回值为False，则抛出一个异常
        if (self.hasAttribute(attr)):
            return self.attrs[attr]
        else:
            raise Exception("No such Attribute:%s" % attr)

# xml解析器
class XmlParser():
    # \s只要出现空白就可以匹配
    space = re.compile(r"\s")
    tagStack = []
    # 设置三种错误信息：
    #     无相应的字符
    #     标签没有闭合
    #     标签不匹配
    attr_Error = "Attribute [%s] should be included by \" \""
    tag_Unclosed_Error = "No closed tag matches :\"%s\""
    tag_Unmatched_Error = "pop tag:%s  red tag:%s."

    def __init__(self, path):
        self.path = path
        self.document = self.getRoot()

    # 获取根节点
    def getRoot(self):
        root = XmlTree()
        file = open(self.path, "r")
        firstLine = file.readline()
        if (firstLine.find("<?xml") >= 0):
            root.text = firstLine
        else:
            file.close()
            file = open(self.path, "r")
        self.beginTag(file, root)
        return root
    # 获取起始标签
    def beginTag(self, file, parent, has=None):
        if (has == None):
            byte = file.read(1)  # read "<"
            byte = self.ignoreWhiteSpace(file, byte)
            byte = file.read(1)
            if (byte == ""):
                self.tryRaiseTagError(file)
                return
            # 读到'/'对标签进行匹配
            elif (byte == '/'):
                self.endTag(file, parent.parent)
            elif (byte == "!"):
                self.ignoreNote(file, parent)
            s = byte
        else:
            byte = has
            s = has

        if (byte != ""):
            me = XmlTree()
            parent.children.append(me)
            me.parent = parent
            byte = file.read(1)
            while (byte != '>' and byte != ""):
                s += byte
                byte = file.read(1)
            if (byte == ""):
                self.tryRaiseTagError(file)
                return
            attrs = s.split()
            if (len(attrs) > 1):
                for i in range(1, len(attrs)):
                    # print attrs[i]
                    key, value = attrs[i].split('=')
                    if (value.startswith("\"") == False or value.endswith("\"") == False):
                        self.raiseAttributeError(file, value)
                    me.attrs[key] = value.strip("\"")
            me.tag = attrs[0]
            '''print "tag:%s"%me["tag"]
            print "parent:%s"%me["parent"]["tag"]
            print "parent's chlildren:%s"%me["parent"]["children"]'''
            self.tagStack.append(attrs[0])
            self.Content(file, parent, me)
        else:
            self.tryRaiseTagError(file)
            return
    #获取起始标签与结束标签之间的内容
    def Content(self, file, parent, me):
        byte = file.read(1)
        if (byte == ""):
            self.tryRaiseTagError(file)
            return
        byte = self.ignoreWhiteSpace(file, byte)
        if (byte != "<"):
            s = byte
            while (byte != "<" and byte != ""):
                s += byte
                byte = file.read(1)
            if (byte == ""):
                self.tryRaiseTagError(file)
                return
            me.text = s
            self.endTag(file, parent)
        else:
            byte = file.read(1)
            if (byte == ""):
                self.tryRaiseTagError(file)
                return
            if (byte == "/"):
                self.endTag(file, parent)
            elif (byte == "!"):
                self.ignoreNote(file, parent)
            else:
                self.beginTag(file, me, byte)
    # 获取结束标签
    def endTag(self, file, parent):
        byte = file.read(1)
        s = byte
        if (byte == ""):
            self.tryRaiseTagError(file)
            return
        while (byte != ">" and byte != ""):
            byte = file.read(1)
            s += byte
        if (byte == ""):
            self.tryRaiseTagError(file)
            return
        tag = self.tagStack.pop()
        if (s.find(tag) < 0):
            file.close()
            raise Exception("Tag Unmatched!", self.tag_Unmatched_Error % (tag, s))
        else:
            self.beginTag(file, parent)

    # 遍历tagStack, 记录xml文件中是否有标签不闭合的情况
    def tryRaiseTagError(self, file):
        if (len(self.tagStack) > 0):
            file.close()
            unclosed = " "
            for i in self.tagStack:
                unclosed += i + " "
            raise Exception("Tag Unclosed!", self.tag_Unclosed_Error % unclosed)
        else:
            pass
    # 抛出属性格式错误
    def raiseAttributeError(self, file, attr):
        file.close()
        raise Exception("Attribute formate Error!", self.attr_Error % attr)

    def ignoreNote(self, file, parent):
        byte = file.read(1)
        s = byte
        if (byte == ""):
            self.tryRaiseTagError(file)
            return
        while (byte != ">" and byte != ""):
            byte = file.read(1)
            s += byte
        print(s)
        if (byte == ""):
            self.tryRaiseTagError(file)
            return
        if (s.startswith("--") == False or s.endswith("-->") == False):
            file.close()
            raise Exception("Note formate Error :""<%s""" % s)
        else:
            self.beginTag(file, parent)


    # 忽略空白字符
    def ignoreWhiteSpace(self, file, byte):
        if (byte == ""):
            self.tryRaiseTagError(file)
        while (self.space.match(byte)):
            byte = file.read(1)
        return byte


def test():
    parser = XmlParser(r"test1.xml")  # path  of  a  xml file
    document = parser.document  # root of the xml tree
    zip = document.findElementsByTagName("zip")
    print(document.text,zip[0])
    print(zip.hasAttribute("category"))
    print(zip.getAttribute("category"))
    author = zip.findElementsByTagName("author")[0]
    print(author.text)


if __name__ == '__main__':
    test()



