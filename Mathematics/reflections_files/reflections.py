#%matplotlib inline
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import parser
import random
from math import sin, cos, tan, log, exp, sqrt
from ipywidgets import fixed, interact, interact_manual
import ipywidgets as widgets



# Returns the reflections of a point across the x-axis
def reflect_across_x_axis(p) :
  (x, y) = p
  return (x, -y)



# Returns the reflections of a point across the y-axis
def reflect_across_y_axis(p) :
  (x, y) = p
  return (-x, y)



# Returns the reflections of a point across the line y = x
def reflect_across_y_equals_x(p) :
  (x, y) = p
  return (y, x)



# Plots the point (x, y) on a graph.
# Formatting options may be specified with fmt.
# If label = True, the point will be labeled with its coordinates, otherwise no label is given.
def plot_point(x, y, fmt, label=True) :
    plt.plot(x, y, fmt)
    if (label) :
        plt.annotate("$({0},{1})$".format(x, y), xy = (x,y), xytext=(4,4), textcoords="offset points")
    return



# Arguments:
#   pts  : a set of points
#   line : one of "x-axis", "y-axis", "both", or "y=x"
#
# Using matplotlib, plots the given list of points in blue, and their reflections in red.
# When a point and its reflection overlap, it is drawn in magenta.
# If label = True, all points will be labeled with their coordinates.
# If set_bounds = True, this function will set the bound of the plot so that all of the plots are visible.
def plot_and_reflect_points(pts, line, label = True, set_bounds = True) :
    if (line == "x-axis") :
        reflect = reflect_across_x_axis
    elif (line == "y-axis") :
        reflect = reflect_across_y_axis
    elif (line == "both") :
        reflect = lambda p : reflect_across_x_axis(reflect_across_y_axis(p))
    elif (line == "y=x") :
        reflect = reflect_across_y_equals_x
    reflections = set(map(reflect, pts))

    # Determine width and height of graph.
    # The plot should fit all of the points with a bit of extra space.
    xmin, xmax, ymin, ymax = 0, 1, 0, 1
    for p in (pts | reflections) :
        (x, y) = p
        xmin = min(xmin, x)
        xmax = max(xmax, x)
        ymin = min(ymin, y)
        ymax = max(ymax, y)
    if (set_bounds) :
        plt.rcParams["figure.figsize"] = [5,5] # Sets plot size to 5 x 5 inches
        plt.axhline(color="black", linewidth=1)
        plt.axvline(color="black", linewidth=1)
        plt.xlim(xmin - 1, xmax + 1)
        plt.ylim(ymin - 1, ymax + 1)
    
    # If we are reflecting over the line y = x,
    # plot the line y = x as a visual reference
    if (line == "y=x") :
        x, y = [xmin - 1, xmax + 1], [ymin - 1, ymax + 1]
        plt.plot(x, y, color="gray", ls="--")
    
    common = pts & reflections
    pts = pts - common
    reflections = reflections - common

    # Plot the points
    for (x, y) in pts : 
        plot_point(x, y, "bo", label)
    for (x, y) in reflections : 
        plot_point(x, y, "ro", label)
    for (x, y) in common : 
        plot_point(x, y, "mo", label)



# Arguments:
#   f      : a function
#   xrange : a pair (a, b)
#   n      : the number of points to sample
#   line   : one of "x-axis", "y-axis", "both", or "y=x"
#
# Samples n equidistributed points in the range xrange = [a, b]
# For each such point x, plots the point (x, f(x)) on the graph, as well as its reflection across the specified line.
def plot_and_reflect_sample_points(f, xrange, n, line) :
    (xmin, xmax) = xrange
    xarr = np.linspace(xmin, xmax, n)
    pts = set()
    for x in xarr :
        pts.add( (x,f(x)) )
    plot_and_reflect_points(pts, line, label = False, set_bounds = False)



def graph_and_reflect_function(func, line, xrange=10, yrange=10):
    # Parse user input string into a function, f(x)
    def g(x):
        try :
            ret = eval(parser.expr(func).compile()) # IMPORTANT! Is it unsafe to use eval here?
        except :
            ret = np.nan
        return ret
    
    f = np.vectorize(g) # Turn g into a function f operating on arrays rather than scalars.
    
    x = np.linspace(-xrange, xrange, 1000) # Build an array of 1000 equally spaced values over the interval [-xrange, xrange]
    y = f(x)

    # Set large values of y to infinity.
    # This prevents matplotlib.pyplot.plot from plotting them, resulting in ugly vertical lines at poles.
    map(lambda t : t if (t == np.nan) else np.inf if (t > 2*yrange) else -np.inf if (t < -2*yrange) else t, y)

    # Some plot formatting
    plt.axhline(color="black", linewidth=1)
    plt.axvline(color="black", linewidth=1, )
    plt.xlim(-xrange, xrange)
    plt.ylim(-yrange, yrange)

    # Plot the functions
    plt.plot(x, y, color="blue", label="$y = f(x)$")
    if (line == "x-axis") :
        plt.plot(x, -y, color="red", label="$y = -f(x)$")
    elif (line == "y-axis") :
        plt.plot(-x, y, color="red", label="$y = f(-x)$")
    elif (line == "both") :
        plt.plot(-x, -y, color="red", label="$y = -f(-x)$")
    elif (line == "y=x") :
        plt.plot(x, x, color="gray", ls="--")
        plt.plot(y, x, color="red", label="$x = f(y)$")

    # Print legend
    plt.legend(loc='upper center', bbox_to_anchor=(1.45, 0.8))



# Plots a graph of the given function with the specified limits on x and y.
# xrange and yrange should be pairs, e.g. xrange = (-5, 10)
def plot_graph(func, xrange, yrange):
    (xmin, xmax) = xrange
    (ymin, ymax) = yrange
    nsamples = 100

    plt.axhline(color="black", linewidth=1)
    plt.axvline(color="black", linewidth=1)
    plt.xlim(xmin, xmax)
    plt.ylim(ymin, ymax)

    x = np.linspace(xmin, xmax, nsamples)
    plt.plot(x, func(x), label="$y = f(x)$")

