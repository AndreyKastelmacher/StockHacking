# coding=utf-8
__author__ = 'AKonline13'

import time
import urllib
import os

#inputfile = open('/Users/AKonline13/PycharmProjects/MachineLearning/DataMining/NasdaqHistoricalQuotes/g.txt')
#inputlist = inputfile.read()
#inputlist = inputlist.split("\n")



symbolfile = open('/Users/AKonline13/PycharmProjects/MachineLearning/DataMining/stockslist1.txt')
symbolslist = symbolfile.read()
symbolslist = symbolslist.split("\n")


# url-  https://www.youtube.com/watch?v=tJGGu2bqZeI - data plotting

base_url = "http://ichart.finance.yahoo.com/table.csv?s="

def make_url(ticker_symbol):

    print ticker_symbol
    return base_url + ticker_symbol

output_path = '/Users/AKonline13/PycharmProjects/MachineLearning/DataMining'


def make_filename(ticker_symbol, directory="NasdaqHistoricalQuotes"):
    return output_path + "/" + directory + "/" + ticker_symbol + ".csv"


def pull_historical_data(ticker_symbol, directory="NasdaqHistoricalQuotes"):
    try:
        urllib.urlretrieve(make_url(ticker_symbol), make_filename(ticker_symbol, directory))

    except urllib.ContentTooShortError as e:
        outfile = open(make_filename(ticker_symbol, directory), "w")
        outfile.write(e.content)
        outfile.close()



# This will compare NasdaqHistorialQuotes and stocklist1 and get all stocks that are missing.


Made_List = os.listdir('/Users/AKonline13/PycharmProjects/MachineLearning/DataMining/NasdaqHistoricalQuotes/')
diff = 0

for i in range(len(symbolslist)):
    try:
        Made_List[i] == symbolslist[i]+".csv"

    except:
        print i
        diff = diff + 1

        pull_historical_data(symbolslist[i])
        time.sleep(1)

print len(Made_List)
print len(symbolslist)
print int(diff)

#i = 1
 #   try:
#for i in symbolslist:
#    time.sleep(2.5)
#    pull_historical_data(i)


