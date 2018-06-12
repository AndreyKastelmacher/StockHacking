__author__ = 'AKonline13'


import urllib
import re

textfile1= '/Users/AKonline13/PycharmProjects/Machine learning/Data mining/Import_oneQuotefromyahoo output.txt'

symbolfile = open('/Users/AKonline13/PycharmProjects/Machine learning/Data mining/stockslist1.txt')

symbolslist = symbolfile.read()

symbolslist = symbolslist.split("\n")
print symbolslist


def write_csv(matrix, path):
    f = open(path, 'w')
    for line in matrix:
        for i in range(len(line)):
            item = line[i]
            if (type(item) == int):
                item = str(item) + ','
            elif (type(item)) == float:
                item = str(item) + ','
            elif (type(item)) == str:
                item = item + ','
            if i == len(line) - 1:
                item = item.strip(',')
            f.write(item)
        f.write('\n')
    f.close()


i=0

# stock value scoper through symbolslist, goes to yahoo finance and looks for stock quotes.
datacollected =[]
while i < len(symbolslist):
    #datacollected.append([])
    url = "https://finance.yahoo.com/q?s="+symbolslist[i]
    htmlfile = urllib.urlopen(url)
    htmltext = htmlfile.read()
    regex = '<span id="yfs_l84_[^.]*">(.+?)</span>'
    pattern = re.compile(regex)
    price = re.findall(pattern, htmltext)
    print "the price of" , symbolslist[i], "is" , price
    datacollected.append([symbolslist[i],price[0]])
    print datacollected
    i = i + 1
    print len(datacollected)
    write_csv(datacollected,textfile1)


















