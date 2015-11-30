# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 18:01:41 2015

@author: pmhgms
"""

from pyalgotrade import strategy
from pyalgotrade.barfeed import yahoofeed
from pyalgotrade.tools import yahoofinance
from pyalgotrade.technical.highlow import High,Low
from pyalgotrade.technical.atr import ATR
import volRate
from pyalgotrade.technical import ma
from pyalgotrade.technical import cross

class MyStrategy(strategy.BacktestingStrategy):
    def __init__(self, feed, instrument, hper, lper, usevir):
        strategy.BacktestingStrategy.__init__(self, feed, 1000)
        self.__instrument=instrument
        self.__position = None
        self.setUseAdjustedValues(True)
        self.__high = High(feed[instrument].getPriceDataSeries(), hper)
        self.__low = Low(feed[instrument].getPriceDataSeries(), lper)
        self.__atr = ATR(feed[instrument], 20)
        self.__cost = 0
        self.stoplosstimes = 0
        self.skipbuy = 0
        self.__wined = False
        self.__virposin = False
        self.__vircost = 0
        self.__usevir = usevir
        #self.cost=0
        
    def onExitOk(self, position):
        execInfo = position.getExitOrder().getExecutionInfo()
        #self.info("SELL at $%.2f, cost at $%.2f" % (execInfo.getPrice(), self.__cost))
        #self.info("stop price at $%.2f" % (self.__cost - self.__atr[-1]*2))
        self.__position = None
    def onEnterOk(self, position):
        execInfo = position.getEntryOrder().getExecutionInfo()
        self.__cost = execInfo.getPrice()
        #self.info("BUY at $%.2f" % (execInfo.getPrice()))
    def onEnterCanceled(self, position):
        self.__position = None
    
    def onBars(self,bars):
        if self.__high[-1] is None:
            return
        bar=bars[self.__instrument]
        if bar.getVolume() == 0:
            return
        #self.info("%s %s %s" % (bar.getClose(), self.__high[-1], self.__low[-1]))

        
        if self.__position is None:
            #rate = bar.getClose()/bar.getOpen()
            if bar.getPrice() >= self.__high[-1]:
                if not self.__wined:
                    shares = int(self.getBroker().getCash() * 0.9 / bars[self.__instrument].getPrice())
                    self.__position = self.enterLong(self.__instrument, shares, True)
                else:
                    self.skipbuy += 1
                #self.cost = float(bar.getPrice())
        
        #跌破最低价卖出
        #rate = bar.getClose()/bar.getOpen() >0.9
        elif bar.getPrice() <= self.__low[-1] or self.stoploss(bar):
            if self.notexiting():
                self.__position.exitMarket()
                
        if self.__usevir == 1:
            self.onbarsvir(bar)
                
        '''
        #止盈卖出
        elif self.__position.getEntryOrder().getExecutionInfo().getPrice() <= bar.getPrice()*0.95 and not self.__position.exitActive():
            self.__position.exitMarket()
        #self.info("%s" % (bar.getClose()))
        '''    
    def getHigh(self):
        return self.__high
    def getLow(self):
        return self.__low
        
    def stoploss(self, bar):
        if bar.getPrice() < self.__cost - self.__atr[-1]*2:
            self.stoplosstimes += 1
            return True
    def notexiting(self):
        return not self.__position.exitActive()
        
    def onbarsvir(self, bar):
        if not self.__virposin:
            if bar.getPrice() >= self.__high[-1]:
                self.__virposin = True
                self.__vircost = bar.getPrice()
        elif bar.getPrice() <= self.__low[-1]:
            self.__virposin = False
            if bar.getPrice() <= self.__vircost:
                self.__wined = False
            else:
                self.__wined = True
        elif bar.getPrice() < self.__vircost - self.__atr[-1]*2:
            self.__virposin = False
            self.__wined = False
            
def run_strategy():
    # Load the yahoo feed from the CSV file
    yahoofinance.download_daily_bars('600865.SS', 2015, '600865.SS-2015.csv')
    feed = yahoofeed.Feed()
    feed.addBarsFromCSV("600865.SS", "600865.SS-2015.csv")

    # Evaluate the strategy with the feed.
    myStrategy = MyStrategy(feed, "600865.SS", 10, 5, 1)
    myStrategy.run()
    print "Final portfolio value: $%.2f" % myStrategy.getBroker().getEquity()
    
#run_strategy()

class SMACrossOver(strategy.BacktestingStrategy):
    def __init__(self, feed, instrument, smaPeriod):
        strategy.BacktestingStrategy.__init__(self, feed)
        self.__instrument = instrument
        self.__position = None
        # We'll use adjusted close values instead of regular close values.
        self.setUseAdjustedValues(True)
        self.__prices = feed[instrument].getPriceDataSeries()
        self.__sma = ma.SMA(self.__prices, smaPeriod)

    def getSMA(self):
        return self.__sma

    def onEnterCanceled(self, position):
        self.__position = None

    def onExitOk(self, position):
        self.__position = None

    def onExitCanceled(self, position):
        # If the exit was canceled, re-submit it.
        self.__position.exitMarket()

    def onBars(self, bars):
        # If a position was not opened, check if we should enter a long position.
        if self.__position is None:
            if cross.cross_above(self.__prices, self.__sma) > 0:
                shares = int(self.getBroker().getCash() * 0.9 / bars[self.__instrument].getPrice())
                # Enter a buy market order. The order is good till canceled.
                self.__position = self.enterLong(self.__instrument, shares, True)
        # Check if we have to exit the position.
        elif not self.__position.exitActive() and cross.cross_below(self.__prices, self.__sma) > 0:
            self.__position.exitMarket()
