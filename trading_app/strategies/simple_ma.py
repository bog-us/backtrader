"""Simple moving average crossover strategy."""

import backtrader as bt


class SmaCross(bt.Strategy):
    """Moving average crossover strategy."""

    params = (('fast', 10), ('slow', 30),)

    def __init__(self):
        ma1 = bt.ind.SMA(period=self.p.fast)
        ma2 = bt.ind.SMA(period=self.p.slow)
        self.crossover = bt.ind.CrossOver(ma1, ma2)

    def next(self):
        if not self.position and self.crossover > 0:
            self.buy()
        elif self.position and self.crossover < 0:
            self.sell()
