# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 14:39:54 2015

@author: pmhgms
"""

import itertools
from pyalgotrade.optimizer import local
from pyalgotrade.barfeed import yahoofeed
from pyalgotrade.tools import yahoofinance
import tut


def parameters_generator():
    instruments = ["600865.SS"]
    hPer = range(5,40)
    lPer = range(5,40)
    return itertools.product(instruments, hPer, lPer)


# The if __name__ == '__main__' part is necessary if running on Windows.
if __name__ == '__main__':
    # Load the feed from the CSV files.
    instruments = ["600865.SS"]
    feed = yahoofinance.build_feed(instruments, 2005, 2015, "yhfeed", skipErrors=True)

    local.run(tut.MyStrategy, feed, parameters_generator())