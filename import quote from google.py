__author__ = 'AKonline13'
import urllib2
import urllib
import re

from googlefinance import getQuotes
import json


symbolfile = open('/Users/AKonline13/PycharmProjects/Machine learning/Data mining/stockslist1.txt')

symbolslist = symbolfile.read()

symbolslist = symbolslist.split("\n")

#prices = []
print str(symbolslist)

#for i in range(len(symbolslist)):

json.dumps(getQuotes(str(symbolslist)), indent=2)

json.loads(stockdata)

for item in quote:
    price = item["LastTradePrice"]




