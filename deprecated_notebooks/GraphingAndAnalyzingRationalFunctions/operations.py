import sympy as sym
from sympy import diff
from sympy.utilities.lambdify import lambdify, implemented_function
from sympy import Function
import numpy as np

from plotting_routines import *
from IPython.display import clear_output
import ipywidgets
from ipywidgets import interact, interactive, fixed, interact_manual

from functools import partial, update_wrapper
from collections import OrderedDict

from ipywidgets import Layout, Output
   
def variables_setup():
    x = sym.symbols('x')
    a = sym.symbols('a',real=True,positive = True)
    return x,a

def derivative_setup(x_value,a_value,function_setup):
    x,a = variables_setup()
    num, denom = function_setup(x_value,a_value)[1], function_setup(x_value,a_value)[2]
    func = sym.simplify(diff(num/denom,x))
    return (func, sym.fraction(func)[0], sym.fraction(func)[1])

def sign(function_setup,x_value,a_value):
    
    x,a = variables_setup()
    
    lam_f = lambdify((x,a), function_setup(x,a)[0])

    if lam_f(x,a_value).evalf(subs={x: x_value}).is_positive:
        return 1
    elif lam_f(x,a_value).evalf(subs={x: x_value}).is_negative:
        return -1
    else:
        return 0
    

def simplified_function(function_setup,a_value):
    
    x,a = variables_setup()
  
    lam_f_num = lambdify((x,a), function_setup(x,a)[1])
    lam_f_denom = lambdify((x,a), function_setup(x,a)[2])
    
    num = lam_f_num(x,a_value)
    denom = lam_f_denom(x,a_value)
    
    func = sym.simplify(factorize(num,x)/factorize(denom,x))
    
    return (func, sym.fraction(func)[0], sym.fraction(func)[1])

def factorize(poly,x):
    roots = sym.solve(poly,x)
    final_product = 1
    for root in roots:
        if sym.im(root) == 0:
            final_product = final_product*(x-root)
            
    unfactorized_part = sym.polys.polytools.div(poly,final_product)[0]
    final_product = final_product*unfactorized_part
    
    return final_product

def limits_at_a(a_value,x_value,function_setup):
    x,a = variables_setup()
    return sym.limit(function_setup(x,a_value)[0], x, x_value)


def find_real_roots(poly,a_value,function_setup):
    x,a = variables_setup()

    if poly == 'num':
        
        lam_f = lambdify((x,a), function_setup(x,a)[1])
        
    elif poly == 'denom':
        lam_f = lambdify((x,a), function_setup(x,a)[2])
        
        
    poly_at_a = lam_f(x,a_value)
    coeffs = sym.Poly(poly_at_a,x).all_coeffs()
    
    all_local_roots = np.roots(coeffs)
    
    real_roots = []
    
    for every_root in all_local_roots:
        if np.imag(every_root) == 0:
            real_roots = np.append(real_roots,np.real(every_root))
            
    return np.round(real_roots,4)

def find_multiplicities(poly,a_value,function_setup,numerator,denominator):
    x,a = variables_setup()
    
    multiplicity_full_dict = {'num':{},'denom':{}}
    multiplicity_real_dict = {'num':{},'denom':{}}
        
    lam_f_num = lambdify((x,a), function_setup(x,a)[1])
    lam_f_denom = lambdify((x,a), function_setup(x,a)[2])
    
    num_at_a = lam_f_num(x,a_value)
    denom_at_a = lam_f_denom(x,a_value)
        
    num_coeffs = sym.Poly(num_at_a,x).all_coeffs()
    denom_coeffs = sym.Poly(denom_at_a,x).all_coeffs()
    
    all_num_roots = list(np.round(np.roots(num_coeffs),4))
    unique_num_roots = list(set(all_num_roots))
    
    all_denom_roots = list(np.round(np.roots(denom_coeffs),4))
    unique_denom_roots = list(set(all_denom_roots))
    
    unique_roots = list(set(np.append(unique_num_roots,unique_denom_roots)))
        
 
    for each_unique_root in unique_roots:
        diff = all_num_roots.count(each_unique_root) - all_denom_roots.count(each_unique_root)
        if diff > 0:
            multiplicity_full_dict['num'][each_unique_root] = diff
        elif diff < 0:
            multiplicity_full_dict['denom'][each_unique_root] = np.abs(diff)
            
    all_keys = np.append(list(multiplicity_full_dict['num'].keys()),list(multiplicity_full_dict['denom'].keys()))
   
    for each_root in all_keys:
        
        #for symbolic roots do:
        #simplified_root = each_root.conjugate().conjugate().simplify().trigsimp()
        #(skip for the roots found numerically with numpy)
        
        if np.imag(each_root) == 0:
            
            if each_root in list(multiplicity_full_dict['num'].keys()):
            
                multiplicity_real_dict['num'][np.real(each_root)] = multiplicity_full_dict['num'][each_root]
            
            elif each_root in list(multiplicity_full_dict['denom'].keys()):
                
                multiplicity_real_dict['denom'][np.real(each_root)] = multiplicity_full_dict['denom'][each_root]
                
    
    return multiplicity_real_dict,num_at_a,denom_at_a
        
      

def true_answers(P,Q,function_setup,a_value):
    x,a = variables_setup()
	
    true_answers = {}
    if factorize(Q,x) == Q:
        true_answers['factorization'] = 'No'
    else:
        true_answers['factorization'] = 'Yes'

    disc_option_a = 'No cancellation occurs; therefore, we have vertical asymptotes at all of the denominator roots.'
    disc_option_b = 'Some factors got cancelled, and the corresponding discontinuities are removable!'
    
    list_num_roots = []
    list_denom_roots = []
    
    for each_num_root in sym.solve(P,x):
        list_num_roots = np.append(list_num_roots, each_num_root.evalf(subs={a: a_value}))
    
    for each_denom_root in sym.solve(Q,x):
        list_denom_roots = np.append(list_denom_roots, each_denom_root.evalf(subs = {a: a_value}))
    

    if bool(set(list_num_roots) & set(list_denom_roots)) == False:
        true_answers['general_discontinuity_type'] = disc_option_a
    else:
        true_answers['general_discontinuity_type'] = disc_option_b
        
      
    true_answers['specific_discontinuity_type'] = {}
    
    for each_remov_disc in return_zeros(a_value,function_setup)[1]:
        true_answers['specific_discontinuity_type'][each_remov_disc] = 'removable discontinuity'
    
    for each_inf_disc in return_zeros(a_value, function_setup)[2]:
        true_answers['specific_discontinuity_type'][each_inf_disc] = 'vertical asymptote'
        
    
        
   
    num_root_multiplicities = find_multiplicities('num',a_value,function_setup,P,Q)[0]['num']
    denom_root_multiplicities = find_multiplicities('denom',a_value,function_setup,P,Q)[0]['denom']
    
    root_multiplicities = {**num_root_multiplicities, **denom_root_multiplicities}
    
    true_answers['multiplicity'] = {}
    
    for each_root in root_multiplicities.keys():
        true_answers['multiplicity'][each_root] = root_multiplicities[each_root]
        
    

    return true_answers


def on_value_change(change, problem_type, widget, function_setup, a_value):
    
    clear_output()
    display(widget)
    
    x,a = variables_setup()
        
    P,Q = function_setup(x,a)[1], function_setup(x,a)[2]
    if change['new'] == true_answers(P,Q,function_setup,a_value)[problem_type]:
        print('Correct!')

    else:
        print('Please try again!')

def return_zeros(a,function_setup):
    
    x = variables_setup()[0]

    numerator,denominator = function_setup(x,a)[1], function_setup(x,a)[2]
    
    func_zeros = []
    func_remov_disc = []
    func_inf_disc = []
    func_limits_remov = []
    
    multiplicity_data = find_multiplicities('num',a,function_setup, numerator,denominator)
    
    numerator_roots = np.round(np.real(np.roots(sym.Poly(multiplicity_data[1],x).all_coeffs())),4)
    denominator_roots = np.round(np.real(np.roots(sym.Poly(multiplicity_data[2],x).all_coeffs())),4)
    
    multiplicity_list_num = list(multiplicity_data[0]['num'].keys())
    multiplicity_list_denom = list(multiplicity_data[0]['denom'].keys())
    
    for every_root in numerator_roots:
        
        if (every_root in multiplicity_list_num) & (every_root in denominator_roots):
            func_remov_disc = np.append(func_remov_disc, every_root)
            
        elif (every_root not in multiplicity_list_num) & (every_root not in multiplicity_list_denom):
            func_remov_disc = np.append(func_remov_disc, every_root)
            
        elif every_root in multiplicity_list_denom:
            continue
        else:
            func_zeros = np.append(func_zeros, every_root)
    
    for every_root in denominator_roots:
        if every_root in multiplicity_list_denom:
            func_inf_disc = np.append(func_inf_disc,every_root)
    
    return (func_zeros, func_remov_disc, func_inf_disc)


def when_we_click_check_button(change, function_setup, a_value, widget_dict, feedback_dict, test_values, problem_type, 
                               check_button, try_again_button, output):
    
    x,a = variables_setup()
    P,Q = function_setup(x,a)[1], function_setup(x,a)[2]
    
    proper_type = type(true_answers(P,Q,function_setup,a_value)[problem_type][test_values[0]])
    
    for each_tv in test_values:
        
        if proper_type(widget_dict[each_tv].value) == true_answers(P,Q,function_setup,a_value)[problem_type][each_tv]:
            with output:
                feedback_dict[each_tv].value += 'Correct!'
                
            
        else:
            with output:
                feedback_dict[each_tv].value += 'Wrong!'
                
    check_button.disabled = True
    try_again_button.disabled = False
    
            
def when_we_click_try_again_button(change, widget_dict, feedback_dict, 
                                   test_values, check_button, try_again_button, output):
    with output:
        clear_output()
    
    for each_tv in test_values:
        feedback_dict[each_tv].value = 'Feedback: '
        
    check_button.disabled = False
    try_again_button.disabled = True
    
    

    

                
         
  

