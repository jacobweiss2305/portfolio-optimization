# -*- coding: utf-8 -*-
"""
Created on Thu Mar 01 13:25:56 2018

@author: jweiss
"""

import pandas as pd
import numpy as np
from cvxpy import *

n = 51
m = 3


np.random.seed(1)
mu = np.abs(np.random.randn(n, 1))
mu

Sigma_tilde = np.random.randn(m, m)
Sigma_tilde = Sigma_tilde.T.dot(Sigma_tilde)
D = np.diag(np.random.uniform(0, 0.9, size=n))
F = np.random.randn(n, m)
F
# Factor model portfolio optimization.
w = Variable(n)
f = F.T*w
f
gamma = Parameter(sign='positive')
Lmax = Parameter()
ret = mu.T*w 
ret

risk = quad_form(f, Sigma_tilde) + quad_form(w, D)




prob_factor = Problem(Maximize(ret - gamma*risk), 
                     [sum_entries(w) == 1, 
                      norm(w, 1) <= Lmax])

# Solve the factor model problem.
Lmax.value = 2
gamma.value = 0.1
prob_factor.solve(verbose=True)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    