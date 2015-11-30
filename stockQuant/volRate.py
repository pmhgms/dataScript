# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 21:35:27 2015

@author: pmhgms
"""

from pyalgotrade import dataseries
from pyalgotrade import technical
from pyalgotrade.barfeed import yahoofeed


# An EventWindow is responsible for making calculations using a window of values.
class Accumulator(technical.EventWindow):
    def getValue(self):
        ret1, ret2 = 1, 1
        if self.windowFull():
            ret1, ret2 = self.getValues()
            ret1 = ret1/ret2
        return ret1

class Vrate(technical.EventBasedFilter):
    def __init__(self, dataSeries, period=2, maxLen=dataseries.DEFAULT_MAX_LEN):
        technical.EventBasedFilter.__init__(self, dataSeries, Accumulator(period), maxLen)

    '''
    # Build a sequence based DataSeries.
    seqDS = dataseries.SequenceDataSeries()
    # Wrap it with a filter that will get fed as new values get added to the underlying DataSeries.
    accum = technical.EventBasedFilter(seqDS, Accumulator(2))
    for data in datas:
        seqDS.append(data)
    return accum'''

#instrument = '600865.ss'
#feed = yahoofeed.Feed()
#feed.addBarsFromCSV(instrument, "600865.SS-2015.csv")
#rates = vrate(feed[instrument].getVolumeDataSeries())

'''
# Put in some values.
for i in range(0, 50):
    seqDS.append(i)

# Get some values.
print accum[0]  # Not enough values yet.
print accum[1]  # Not enough values yet.
print accum[2]  # Ok, now we should have at least 3 values.
print accum[3]
print accum[4]
print accum[5]
print accum[6]

# Get the last value, which should be equal to 49 + 48 + 47.
print accum[-1]
'''