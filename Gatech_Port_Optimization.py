"""
Portfolio optimization with CVXPY
See examples at http://cvxpy.org
Author: Shabbir Ahmed
"""

import pandas as pd
import numpy as np
from cvxpy import *



# compute mean return
r = np.array([10,12,18])
sd = np.array([4,10,14]) 
tickers = ['a','b','c']
# covariance
C = np.matrix([[1,.2,.4],[.2,1,.7],[.4,.7,1]])
 
# set up optimization model
n = 3
x = Variable(n)
req_return = 5
ret = r.T*x
risk = quad_form(x, C)
prob = Problem(Minimize(risk),[sum_entries(x) == 1])
prob.solve()
print "----------------------"
print "Optimal portfolio"
print "----------------------"
for s in range(len(tickers)):
    print 'x[%s] = %f' %(tickers[s],x.value[s,0])
print "----------------------"
print 'Exp ret = %f' %(ret.value)
print 'risk    = %f' %((risk.value))
print "----------------------"


#Pulp Optimzer
from pulp import *
ticker = ['aapl','ibm','fds']
ret = [10,12,18]
sd = [4,10,14]

prob2 = LpProblem('Portfolio optimization', LpMinimize)
tickerVars = LpVariable.dicts("Ticker", ticker,0)

prob2 += lpSum([sd[f] * tickerVars[f] for f in ticker])

prob2 += lpSum([tickerVars[f] for f in ticker]) == 1

prob2.solve()
print("---------The solution to this Portfolio Optimization problem is----------")
print("Total Tickers:")
for var in prob.variables():
    if var.varValue > 0.0:
        print(str(var).replace('Ticker_','')+" "+str(var.varValue))






# solve problem and write solution
try:
    prob.solve()
    print "----------------------"
    print "Optimal portfolio"
    print "----------------------"
    for s in range(len(symbols)):
        print 'x[%s] = %f' %(symbols[s],x.value[s,0])
    print "----------------------"
    print 'Exp ret = %f' %(ret.value)
    print 'risk    = %f' %((risk.value))
    print "----------------------"
except:
    print 'Error'
