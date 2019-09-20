1.   xml下面框架，etree能够很好的解析xml文件。但对于判断xml是否符合规范较为麻烦。
但另外的一个包，sax却能很容易地判断xml文件格式是否符合规范。

class XmlUtil:
	def get_page(self, file_path)   用于返回一个etree的根，即xml的根节点
	def getConfig(self, filepath)   用于获取在该class中初始化的值

class page：
	def haveError（self，filepath）用于检测xml中是否存在格式错误

class UiElement:
	def getAttribute（self， root） 获取所有子节点的tag和attrib
	def get_someAttrib(self, root, attrib)   获取某个节点的tag和attrib并将其祖先节点（来源）进行输出



如果你要使用的话：
	#1.先实例化page，检验xml页面是否有问题
	page = page()    
	flag = page.haveError(file_path)
	#2.如果页面不出错那么对xml进行解析
	xml = XmlUtil(file_path)
	root = xml.get_page(file_path)
	ui = UiElement()
	ui.getAttrib()
	#即可获取到所有子节点的值
	
	
	**正确的是parsexml.py    
	firstTry.py是我最开始解决识别xml是否有格式错误的文件，
	但是字节识别的方式影响读取速度，代码繁杂，导致存在一些bug