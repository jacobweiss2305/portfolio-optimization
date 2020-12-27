# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from pulp import *
import pandas as pd

data = pd.read_excel("C:/Users/jacob weiss/Desktop/Position_Data2.xlsx", header = 0 )


data = data.values.tolist()

ticker = [x[0] for x in data]

sector = dict([(x[0], float(x[4])) for x in data])

price = dict([(x[0], float(x[1])) for x in data])

pwr = dict([(x[0], float(x[2])) for x in data])

prob = LpProblem('Portfolio optimization', LpMaximize)

sectorVars=LpVariable.dict("Sector",sector,0,9, cat = 'Integer')
tickerVars = LpVariable.dicts("Ticker", ticker,0)
tickerVars_selected = LpVariable.dicts("ticker_select",ticker,0,1,LpBinary)

prob += lpSum([pwr[f] * tickerVars[f] for f in ticker])

prob += lpSum([tickerVars[i] for i in ticker]) == 100

for i in ticker:
    prob += tickerVars[i] <= 10

for i in ticker:
    prob += tickerVars[i] >= 1

for i in sector:
    prob += lpSum(tickerVars[i]) <= 20 

prob.solve()

print()
print("---------The solution to this Portfolio Optimization problem is----------")
for var in prob.variables():
    if var.varValue > 0:
        print(str(var.varValue)+" units of "+str(var).replace('Ticker_','') )
print()
print("Total cost of Portfolio = $%.3f" % value(prob.objective))



#print(prob.variables)
