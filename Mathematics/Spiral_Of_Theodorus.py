#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May 11 11:03:28 2018

@author: jonathan
"""
import numpy as np
import matplotlib.pyplot as plt
from math import atan, sqrt, cos, sin

def Spiral(n):
    N = np.arange(1,n+1)
    phi = 0
    plt.figure(1,figsize = (14,10))
    for n in N:
        phi_n = atan(1./sqrt(n))
        phi += phi_n
        if n == 1:
            plt.plot([0,1],[0,0],linewidth = 1)
            plt.plot([1,1],[0,1],linewidth = 1)
            last_x = 1
            last_y = 1
        r = sqrt(n + 1)
        x = r*cos(phi)
        y = r*sin(phi)
        plt.plot([0,x], [0,y], linewidth = 1)
        plt.plot([last_x,x], [last_y,y])
        string = str((r'$\sqrt{' + str(n + 1) + '}$'))
        plt.text(x/1.2,y/1.2,string)
        last_x = x
        last_y = y