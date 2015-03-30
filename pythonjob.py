__author__ = 'jeff'
from urllib import urlopen
import re
p = re.compile(' <span class=".*">New</span> <a href=".*">(.*)</a><br/>\n(.*)')
# q= re.compile('E-mail contact</strong>: <a class="reference external" href="(.*)">')
websitep = 'http://www.python.org/jobs/?page='
# websiteq = 'https://www.python.org/jobs/'
def filefind(filename, strings):
    for line in open(filename, 'r').readlines():
        if strings in line:
            return True
for i in range(1, 4):
    i = bytes(i)
    text = urlopen(websitep+i).read()
    co = p.finditer(text)
    for m in co:
        #print m.group(1)
        a, b = m.group(1), m.group(2)
        buer = filefind('/home/jeff/fd.txt', a and b)
        print a, b
        print buer
        if buer is None:
            f = open('/home/jeff/fd.txt', 'a')
            print >> f, m.group(1), m.group(2)
            f.close()
        if buer is True:
            pass
    print len(p.findall(text))
