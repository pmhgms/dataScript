# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 18:01:16 2015

@author: pmhgms
"""

from pyalgotrade import plotter
from pyalgotrade.tools import yahoofinance
from pyalgotrade.stratanalyzer import returns
import pickle
import os
from random import randint
import tut
from pyalgotrade.stratanalyzer import sharpe

def pickAsFunToLoop(instrument,usevir=0):

    #code = pickle.load(open(r'C:\Users\pmhgms\Desktop\machine_leaning\DataSet\stock_code.pickle','rb'))
    #instrument = code[randint(0, len(code))]
    # Load the yahoo feed from the CSV file
    instruments = [instrument]
    sy, ey = 2000, 2015
    p1, p2 = 20, 10
    usevir = usevir
    feed = yahoofinance.build_feed(instruments, sy, ey, "yhfeed", skipErrors=True)
    
    # Evaluate the strategy with the feed's bars.
    myStrategy = tut.MyStrategy(feed, instrument, p1, p1, usevir)
    
    # Attach a returns analyzers to the strategy.
    returnsAnalyzer = returns.Returns()
    myStrategy.attachAnalyzer(returnsAnalyzer)
    
    # Attach the plotter to the strategy.
    plt = plotter.StrategyPlotter(myStrategy)
    # Include the SMA in the instrument's subplot to get it displayed along with the closing prices.
    plt.getInstrumentSubplot(instrument).addDataSeries("high", myStrategy.getHigh())
    plt.getInstrumentSubplot(instrument).addDataSeries("low", myStrategy.getLow())
    # Plot the simple returns on each bar.
    #plt.getOrCreateSubplot("returns").addDataSeries("Simple returns", returnsAnalyzer.getReturns())
    
    # Run the strategy.
    myStrategy.run()
    myStrategy.info("Final portfolio value: $%.2f, Stop loss %d time, Skip buy %d time" % (myStrategy.getResult(), myStrategy.stoplosstimes, myStrategy.skipbuy))
    
    # Plot the strategy.
    directory = 'temjpg'
    picname = instrument+'_From_'+str(sy)+'_To_'+str(ey)+'_p1_'+str(p1)+'_p2_'+str(p2)+'_usevir_'+str(usevir)+'.jpg'
    path = os.path.join(directory, picname)
    plt.plot(savefige=True, path=path)
    



def pickAsFunToLoop2(instrument):

    #code = pickle.load(open(r'C:\Users\pmhgms\Desktop\machine_leaning\DataSet\stock_code.pickle','rb'))
    #instrument = code[randint(0, len(code))]
    # Load the yahoo feed from the CSV file
    instruments = [instrument]
    sy, ey = 2000, 2015
    smaPeriod = 60
    feed = yahoofinance.build_feed(instruments, sy, ey, "yhfeed", skipErrors=True)
    
    # Evaluate the strategy with the feed's bars.
    myStrategy = tut.SMACrossOver(feed, instrument, smaPeriod)
    
    # Attach a returns analyzers to the strategy.
    returnsAnalyzer = returns.Returns()
    myStrategy.attachAnalyzer(returnsAnalyzer)
    sharpeRatioAnalyzer = sharpe.SharpeRatio()
    myStrategy.attachAnalyzer(sharpeRatioAnalyzer)
    # Attach the plotter to the strategy.
    plt = plotter.StrategyPlotter(myStrategy)
    # Include the SMA in the instrument's subplot to get it displayed along with the closing prices.
    plt.getInstrumentSubplot(instrument).addDataSeries("sma", myStrategy.getSMA())
    # Plot the simple returns on each bar.
    #plt.getOrCreateSubplot("returns").addDataSeries("Simple returns", returnsAnalyzer.getReturns())
    
    # Run the strategy.
    myStrategy.run()
    myStrategy.info("Final portfolio value: $%.2f" % (myStrategy.getResult()))
    
    # Plot the strategy.
    directory = 'smajpg'
    picname = instrument+'_From_'+str(sy)+'_To_'+str(ey)+'_smaPeriod_'+str(smaPeriod)+'.jpg'
    path = os.path.join(directory, picname)
    plt.plot(savefige=True, path=path)