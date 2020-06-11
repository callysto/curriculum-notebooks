import matplotlib.pyplot as plt
import matplotlib
import matplotlib.ticker as ticker
from operations import *
import itertools
import numpy as np



def set_up_plotting(width,height,title):

    plt.style.use('seaborn-white')
    plt.rcParams["xtick.labelsize"] = 14
    plt.rcParams["ytick.labelsize"] = 14
    plt.rcParams["font.size"] = 14
    plt.rcParams['mathtext.fontset'] = 'stix'
    plt.rcParams['font.family'] = 'STIXGeneral'
    plt.rcParams['legend.facecolor'] = 'white'
    plt.rcParams['axes.linewidth'] = 0
    
    fig = plt.figure(figsize=(width,height), num = title)
    ax = fig.add_subplot(111)

    ax.xaxis.set_tick_params(which = 'major',length = 10, width = 2)
    ax.yaxis.set_tick_params(which = 'major',length = 10, width = 2)
        
    ax.xaxis.set_tick_params(which = 'minor',length = 6, width = 1.5)
    ax.yaxis.set_tick_params(which = 'minor',length = 6, width = 1.5)
    
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero') 
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')    

    return (fig,ax)


def build_snake(function_setup, a_value, snake_ax, arr_flag):
    
    i = len(snake_ax.collections)
    while i > 0:
        del snake_ax.collections[i-1]
        i = i-1
        
    j = len(snake_ax.lines)
    while j > 1:
        del snake_ax.lines[j-1]
        j = j-1
        
    k = len(snake_ax.texts)
    while k > 0:
        del snake_ax.texts[k-1]
        k = k-1

    
    x,a = variables_setup()
    P = function_setup(x,a)[1]
    Q = function_setup(x,a)[2]
    
    local_num_roots =  list(find_multiplicities('num',a_value,function_setup,P,Q)[0]['num'].keys())
    local_denom_roots = list(find_multiplicities('denom',a_value,function_setup,P,Q)[0]['denom'].keys())

    all_local_roots = np.sort(np.append(local_num_roots, local_denom_roots))
    local_str_roots = []
    
    for i in range(0,len(all_local_roots)):
        
        str_label = '$' + str(np.round(all_local_roots[i],2)) + '$'
        local_str_roots = np.append(local_str_roots, str_label)

    try:
        xstart = int(min(all_local_roots)) - 5
        xend = int(max(all_local_roots)) + 5

        snake_ax.set(xticks=all_local_roots, xticklabels = local_str_roots)

        index_range = np.arange(0,len(all_local_roots),1)

        for i in index_range:
            
            if all_local_roots[i] in return_zeros(a_value,function_setup)[0]:
                snake_ax.plot(all_local_roots[i],0,marker = 'o', markersize = 8, color = 'black')
                
            elif all_local_roots[i] in local_denom_roots:
                snake_ax.plot(all_local_roots[i],0,marker = 'o', color = 'white', markeredgecolor = 'black',
                             markeredgewidth = 1.5, markersize = 8)

            if (i-1) not in index_range:
                trial_value = all_local_roots[i] - 100
                trial_sign = sign(function_setup, trial_value, a_value)
                snake_ax.hlines(y=trial_sign, xmin = xstart, xmax = all_local_roots[i], lw = 3, color = '#1c965d', 
                                linestyles = 'dotted', alpha = 0.5)
                if trial_sign == -1:
                    snake_ax.text((xstart+all_local_roots[i])/2. - 0.1, -0.5, '$-$',
                                 fontsize = 10)
                    if arr_flag == 1:
                        snake_ax.text((xstart+all_local_roots[i])/2. - 0.1, -0.75, '$\searrow$',
                                 fontsize = 15)
                        
                else:
                    snake_ax.text((xstart+all_local_roots[i])/2. - 0.1, +0.5, '$+$',
                                 fontsize = 10)
                    if arr_flag == 1:
                        snake_ax.text((xstart+all_local_roots[i])/2. - 0.1, +0.25, r'${\nearrow}$',
                                 fontsize = 15)                    

            if (i+1) not in index_range:
                trial_value = all_local_roots[i] + 100
                trial_sign = sign(function_setup, trial_value, a_value)
                snake_ax.hlines(y=trial_sign, xmin = all_local_roots[i], xmax = xend, lw = 3, color = '#1c965d', 
                                linestyles = 'dotted', alpha = 0.5)
                if trial_sign == -1:
                    snake_ax.text((xend+all_local_roots[i])/2. - 0.1, -0.5, '$-$',
                                 fontsize = 10)
                    if arr_flag == 1:
                        snake_ax.text((xend+all_local_roots[i])/2. - 0.1, -0.75, '$\searrow$',
                                 fontsize = 15) 
                else:
                    snake_ax.text((xend+all_local_roots[i])/2. - 0.1, +0.5, '$+$',
                                 fontsize = 10)
                    if arr_flag == 1:
                        snake_ax.text((xend+all_local_roots[i])/2. - 0.1, +0.25, r'${\nearrow}$',
                                 fontsize = 15) 

            else:
                trial_value = np.random.uniform(all_local_roots[i],all_local_roots[i+1])
                trial_sign = sign(function_setup, trial_value, a_value)
                snake_ax.hlines(y=trial_sign, xmin = all_local_roots[i], xmax = all_local_roots[i+1], lw = 3, 
                                color = '#1c965d',  linestyles = 'dotted', alpha = 0.5)

                if trial_sign == -1:
                    snake_ax.text((all_local_roots[i]+all_local_roots[i+1])/2. - 0.1, -0.5, '$-$',
                                 fontsize = 10)
                    if arr_flag == 1:
                        snake_ax.text((all_local_roots[i]+all_local_roots[i+1])/2. - 0.1, -0.75, '$\searrow$',
                                 fontsize = 15) 
                else:
                    snake_ax.text((all_local_roots[i]+all_local_roots[i+1])/2. - 0.1, +0.5, '$+$',
                                 fontsize = 10)
                    if arr_flag == 1:
                        snake_ax.text((all_local_roots[i]+all_local_roots[i+1])/2. - 0.1, +0.25, r'${\nearrow}$',
                                 fontsize = 15) 



            if true_answers(P,Q,function_setup,a_value)['multiplicity'][all_local_roots[i]] % 2 != 0:
                    snake_ax.vlines(x = all_local_roots[i], ymin = -1, ymax = 1, lw = 3, color = '#1c965d',
                                  linestyles = 'dotted', alpha = 0.5)

            else:
                if trial_sign == -1:
                    snake_ax.vlines(x = all_local_roots[i], ymin = trial_sign, ymax = 0, lw = 3, color = '#1c965d', 
                                linestyles = 'dotted', alpha = 0.5)
                elif trial_sign == 1:
                    snake_ax.vlines(x = all_local_roots[i], ymin = 0, ymax = trial_sign, lw = 3, color = '#1c965d', 
                                linestyles = 'dotted', alpha = 0.5)

            dy = itertools.cycle([0,40/72.])


            for label in snake_ax.xaxis.get_majorticklabels():
                label.set_position((label.get_position()[0],next(dy)))
                
    except ValueError:
        snake_ax.set_xticks([])
        trial_sign = sign(function_setup, 0, a_value)
        snake_ax.axhline(y=trial_sign, xmin = 0, xmax = 1, lw = 3, 
                                color = '#1c965d',  ls = 'dotted', alpha = 0.5) 
        
        