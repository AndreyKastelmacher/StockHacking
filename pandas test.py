__author__ = 'AKonline13'


from pandas.io.data import DataReader
from datetime import datetime

goog = DataReader('goog',  'yahoo', datetime(2012,1,1), datetime(2014,1,1))
print(goog['Adj Close'])
