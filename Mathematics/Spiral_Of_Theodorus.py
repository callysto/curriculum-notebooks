#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May 11 11:03:28 2018

@author: jonathan
"""
import numpy as np
import matplotlib.pyplot as plt
from math import atan, sqrt, cos, sin
col = ['#e02727','#e06e27','#e0ca27','#a9e027','#57e027','#27e07e','#27e0bc','#27cde0','#2789e0','#2750e0','#2c27e0','#6827e0','#8427e0','#b527e0','#e027de','#e0279f','#e02766']
c = len(col)
def Spiral(n):
    col_counter = 0 
    N = np.arange(1,n)
    phi = 0
    plt.figure(1,figsize = (10,7))
    hold = True
    for n in N:
        phi_n = atan(1./sqrt(n))
        phi += phi_n
        if n == 1:
            plt.plot([0,1],[0,0],linewidth = 1.5,color = col[col_counter])
            plt.plot([1,1],[0,1],linewidth = 1.5,color = col[col_counter])
            r = sqrt(n + 1)
            x = r*cos(phi)
            y = r*sin(phi)
            plt.plot([0,x],[0,y],linewidth = 1.5,color = col[col_counter])
            string = str((r'$\sqrt{' + str(n + 1) + '}$'))
            plt.text(x/1.4,y/1.4,string)
            X = [0,1,x]
            Y = [0,0,y]
            plt.fill(X,Y,color = col[col_counter],alpha = 0.3)            
            last_x = 1
            last_y = 1
        else:
            r = sqrt(n + 1)
            x = r*cos(phi)
            y = r*sin(phi)
            plt.plot([0,x], [0,y], linewidth = 1.5,color = col[col_counter])
            plt.plot([last_x,x], [last_y,y],color = col[col_counter])
            string = str((r'$\sqrt{' + str(n + 1) + '}$'))
            plt.text(x/1.4,y/1.4,string)
            X = [0,last_x,x]
            Y = [0,last_y,y]
            plt.fill(X,Y,color = col[col_counter],alpha = 0.3)
            last_x = x
            last_y = y

            
        col_counter += 1
        if col_counter > c-1:
            col_counter = 0