# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 21:26:50 2015

@author: pmhgms
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 18:01:41 2015

@author: pmhgms
"""
import datetime
from pyalgotrade import strategy
from pyalgotrade.barfeed import yahoofeed
from pyalgotrade.tools import yahoofinance
from pyalgotrade.technical.highlow import High,Low
import volRate

class MyStrategy(strategy.BacktestingStrategy):
    def __init__(self, feed, instrument):
        strategy.BacktestingStrategy.__init__(self, feed)
        self.__instrument=instrument
        self.__position = None
        self.setUseAdjustedValues(True)
        self.__high = High(feed[instrument].getPriceDataSeries(), 20)
        self.__low = Low(feed[instrument].getPriceDataSeries(), 10)
        self.__vrate = volRate.Vrate(feed[instrument].getVolumeDataSeries())
        self.__crate = volRate.Vrate(feed[instrument].getPriceDataSeries())
        #self.cost=0
        
    def onExitOk(self, position):
        execInfo = position.getExitOrder().getExecutionInfo()
        #self.info("SELL at $%.2f, cost at $%.2f" % (execInfo.getPrice(), self.__position.getEntryOrder().getExecutionInfo().getPrice()))
        self.__position = None
    def onEnterOk(self, position):
        execInfo = position.getEntryOrder().getExecutionInfo()
        self.info("BUY at $%.2f" % (execInfo.getPrice()))
        self.info(execInfo.getDateTime())
    
    def onBars(self,bars):
        if self.__high[-1] is None:
            return
        bar=bars[self.__instrument]
        #self.info("%s %s %s" % (bar.getClose(), self.__high[-1], self.__low[-1]))

        if self.__position is None:
            #买入策略
            #量比策略
            '''
            if self.__vrate[-1] >= 1.3 and self.__crate[-1]<1.09:
                shares = int(self.getBroker().getCash() * 0.9 / bars[self.__instrument].getPrice())
                self.__position = self.enterLong(self.__instrument, shares, True)
                #self.cost = float(bar.getPrice())
            '''
            #突破最高价策略
            if bar.getPrice() >= self.__high[-1] and self.__crate[-1]<1.09:
                shares = int(self.getBroker().getCash() * 0.9 / bars[self.__instrument].getPrice())
                self.__position = self.enterLong(self.__instrument, shares, True)
                print bar.getDateTime()
            
        
        #卖出策略
        #固定周期策略
        elif self.__position.getEntryOrder().getExecutionInfo().getPrice() <= bar.getPrice()*0.95 and not self.__position.exitActive():
            self.__position.exitMarket()
        '''
        #止盈策略
        elif self.__position.getEntryOrder().getExecutionInfo().getPrice() <= bar.getPrice()*0.95 and not self.__position.exitActive():
            self.__position.exitMarket()
            
        #量比策略
        elif self.__vrate[-1] <= 0.9:
            self.__position.exitMarket()
        '''
        #self.info("%s" % (bar.getClose()))
            
    def getHigh(self):
        return self.__vrate
    def getLow(self):
        return self.__low
        
def run_strategy():
    # Load the yahoo feed from the CSV file
    #yahoofinance.download_daily_bars('600865.SS', 2015, '600865.SS-2015.csv')
    feed = yahoofeed.Feed()
    feed.addBarsFromCSV("600865.SS", "600865.SS-2015.csv")

    # Evaluate the strategy with the feed.
    myStrategy = MyStrategy(feed, "600865.SS")
    myStrategy.run()
    print "Final portfolio value: $%.2f" % myStrategy.getBroker().getEquity()
    
run_strategy()