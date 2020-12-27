# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 21:16:36 2018

@author: jweiss
"""





#------------------------------------------------------------------------------
#Using PuLP
import pandas as pd
from pulp import *
data = pd.read_csv("C:/Users/jweiss/Documents/pos_data1.csv", header = 0 )

#Show me the top 5
data.head()

#Put that data in a list
data = data.values.tolist()

#Let's create some variables
ticker = [x[0] for x in data]
pwr = dict([(x[0],float(x[1])) for x in data])
OPS_per = dict([(x[0],float(x[2])) for x in data])
z_score = dict([(x[0],float(x[3])) for x in data])
wz_score = dict([(x[0],float(x[4])) for x in data])

#Optimizer
prob = LpProblem('Portfolio optimization', LpMinimize)

#Decision Variables
tickerVars = LpVariable.dicts("Ticker", ticker,0)

#Objective Function
prob += lpSum([pwr[f] * tickerVars[f] for f in ticker]) >= .1

#Constraints
for i in ticker:
    prob += tickerVars[i] <= OPS_per[i]


prob += lpSum([wz_score[f] * tickerVars[f] for f in ticker]) >= .05


#Solution
prob.solve()
if prob.solve() == 1:
    print("Feasible Optimal Solution") 
elif prob.solve() == -1:
    print("Error: Infeasible Solution")
elif prob.solve() is not 1 or -1:
    print("Error: Unbounded or Not Optimal")
    
print("---------The solution to this Portfolio Optimization problem is----------")
print("Total Tickers:")
for var in prob.variables():
    if var.varValue > 0.0:
        print(str(var).replace('Ticker_','')+" "+str(var.varValue))







