__author__ = 'AKonline13'


symbolfile = open('/Users/AKonline13/PycharmProjects/Machine learning/Data mining/StockLiveMonitor.txt')

symbolslist = symbolfile.read()

symbolslist = symbolslist.split("\n")
print symbolslist

import urllib
