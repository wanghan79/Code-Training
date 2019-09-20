import os


def getSize():
    size = os.path.getsize('test.xml')
    k_size = size / 1000 ** 3
    return k_size


class createxml():

    def openxml(self):
        self.f = open('test.xml', 'a+')

    def writehead(self):
        self.f.write('<collection shelf="New Arrivals">\n')

    def writetail(self):
        self.f.write('</collection>')

    def writexml(self):
        self.f.write('<movie title="Enemy Behind">\n')
        self.f.write('   <type>War, Thriller</type>\n')
        self.f.write('   <format>DVD</format>\n')
        self.f.write('   <year>2003</year>\n')
        self.f.write('   <rating>PG</rating>\n')
        self.f.write('   <stars>10</stars>\n')
        self.f.write('   <description>Talk about a US-Japan war</description>\n')
        self.f.write('</movie>\n')
        self.f.write('<movie title="Enemy Behind">\n')
        self.f.write('   <type>War, Thriller</type>\n')
        self.f.write('   <format>DVD</format>\n')
        self.f.write('   <year>2003</year>\n')
        self.f.write('   <rating>PG</rating>\n')
        self.f.write('   <stars>10</stars>\n')
        self.f.write('   <description>Talk about a US-Japan war</description>\n')
        self.f.write('</movie>\n')
        self.f.write('<movie title="Enemy Behind">\n')
        self.f.write('   <type>War, Thriller</type>\n')
        self.f.write('   <format>DVD</format>\n')
        self.f.write('   <year>2003</year>\n')
        self.f.write('   <rating>PG</rating>\n')
        self.f.write('   <stars>10</stars>\n')
        self.f.write('   <description>Talk about a US-Japan war</description>\n')
        self.f.write('</movie>\n')
        self.f.write('<movie title="Enemy Behind">\n')
        self.f.write('   <type>War, Thriller</type>\n')
        self.f.write('   <format>DVD</format>\n')
        self.f.write('   <year>2003</year>\n')
        self.f.write('   <rating>PG</rating>\n')
        self.f.write('   <stars>10</stars>\n')
        self.f.write('   <description>Talk about a US-Japan war</description>\n')
        self.f.write('</movie>\n')

    def closexml(self):
        self.f.close()


if __name__ == "__main__":
    w = createxml()
    w.openxml()
    if (getSize() == 0):
        w.writehead()
    while (getSize() < 1):
        w.writexml()
    w.writetail()
    w.closexml()
