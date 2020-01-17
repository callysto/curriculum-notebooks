#----------

#Import modules and packages 
import ipywidgets as widgets
import matplotlib.pyplot as plt
import numpy as np
import math
import random
from IPython.display import clear_output, SVG

#----------

#import ipywidgets as widgets
#import random

#This function produces a multiple choice form with four options
def multiple_choice(option_1, option_2, option_3, option_4):
    option_list = [option_1, option_2, option_3, option_4]
    answer = option_list[0]
    letters = ["(A) ", "(B) ", "(C) ", "(D) "]

    #Boldface letters at the beginning of each option
    start_bold = "\033[1m"; end_bold = "\033[0;0m"

    #Randomly shuffle the options
    random.shuffle(option_list)
    
    #Prints the letters (A) to (D) in sequence with randomly chosen options
    for i in range(4):
        option_text = option_list.pop()
        print(start_bold + letters[i] + end_bold + option_text)

        #Stores the correct answer
        if option_text == answer:
            letter_answer = letters[i]

    button1 = widgets.Button(description="(A)"); button2 = widgets.Button(description="(B)")
    button3 = widgets.Button(description="(C)"); button4 = widgets.Button(description="(D)")
    
    button1.style.button_color = 'Whitesmoke'; button2.style.button_color = 'Whitesmoke'
    button3.style.button_color = 'Whitesmoke'; button4.style.button_color = 'Whitesmoke'
    
    container = widgets.HBox(children=[button1,button2,button3,button4])
    display(container)
    print(" ", end='\r')

    def on_button1_clicked(b):
            if "(A) " == letter_answer:
                print("Correct!    ", end='\r')
                button1.style.button_color = 'Moccasin'; button2.style.button_color = 'Whitesmoke'
                button3.style.button_color = 'Whitesmoke'; button4.style.button_color = 'Whitesmoke'
            else:
                print("Try again.", end='\r')
                button1.style.button_color = 'Lightgray'; button2.style.button_color = 'Whitesmoke'
                button3.style.button_color = 'Whitesmoke'; button4.style.button_color = 'Whitesmoke'

    def on_button2_clicked(b):
            if "(B) " == letter_answer:
                print("Correct!    ", end='\r')
                button1.style.button_color = 'Whitesmoke'; button2.style.button_color = 'Moccasin'
                button3.style.button_color = 'Whitesmoke'; button4.style.button_color = 'Whitesmoke'
            else:
                print("Try again.", end='\r')
                button1.style.button_color = 'Whitesmoke'; button2.style.button_color = 'Lightgray'
                button3.style.button_color = 'Whitesmoke'; button4.style.button_color = 'Whitesmoke'

    def on_button3_clicked(b):
            if "(C) " == letter_answer:
                print("Correct!    ", end='\r')
                button1.style.button_color = 'Whitesmoke'; button2.style.button_color = 'Whitesmoke'
                button3.style.button_color = 'Moccasin'; button4.style.button_color = 'Whitesmoke'
            else:
                print("Try again.", end='\r')
                button1.style.button_color = 'Whitesmoke'; button2.style.button_color = 'Whitesmoke'
                button3.style.button_color = 'Lightgray'; button4.style.button_color = 'Whitesmoke'

    def on_button4_clicked(b):
            if "(D) " == letter_answer:
                print("Correct!    ", end='\r')
                button1.style.button_color = 'Whitesmoke'; button2.style.button_color = 'Whitesmoke'
                button3.style.button_color = 'Whitesmoke'; button4.style.button_color = 'Moccasin'
            else:
                print("Try again.", end='\r')
                button1.style.button_color = 'Whitesmoke'; button2.style.button_color = 'Whitesmoke'
                button3.style.button_color = 'Whitesmoke'; button4.style.button_color = 'Lightgray'

    button1.on_click(on_button1_clicked); button2.on_click(on_button2_clicked)
    button3.on_click(on_button3_clicked); button4.on_click(on_button4_clicked)
    
def f(Angle=45):
        angle_incidence = Angle
        angle_incline = (90-angle_incidence)
        slope = math.tan(math.radians(angle_incline))
        reflected_ray = slope*50

        plt.figure()

        #Plot normal, incident ray, and reflected ray
        plt.plot([0,0],[100,0], linestyle="dotted", color="grey")
        plt.plot([0,-50],[0,reflected_ray], color="red")
        plt.plot([0,50],[0,reflected_ray], color="red")

        plt.ylim(0,100)
        plt.xlim(-50,50)
        plt.ylabel('Length')
        plt.xlabel('Length')
        plt.annotate(xy=[-35,90],s="Incident ray")
        plt.annotate(xy=[15,90],s="Reflected ray")

        plt.show()
        
def f(Distance=30):
        object_distance = -Distance
        image_distance = Distance

        #y=mx+b
        m_1 =(80-0)/(-60-image_distance)
        b_1 = 80-(m_1*(-60))

        m_2 =(90-0)/(-60-image_distance)
        b_2 = 90-(m_2*(-60))

        plt.figure()

        #Plot incident ray, reflected ray, and projected ray
        plt.plot([object_distance,0],[0,b_1], linewidth=2.0, color="red")
        plt.plot([0,-60],[b_1,80], linewidth=2.0, color="red")
        plt.plot([0,image_distance],[b_1,0], linewidth=2.0, linestyle="dotted", color="red")

        plt.plot([object_distance,0],[0,b_2], linewidth=2.0, color="orange")
        plt.plot([0,-60],[b_2,90], linewidth=2.0, color="orange")
        plt.plot([0,image_distance],[b_2,0], linewidth=2.0, linestyle="dotted", color="orange")

        #Plot mirror, object, and image
        plt.plot([0,0],[100,0], linewidth=5.0, color="grey")

        plt.plot([object_distance,object_distance],[0,17], linewidth=4.0, color="black")
        plt.plot([(object_distance-2),(object_distance)],[14,17], linewidth=4.0, color="black")
        plt.plot([(object_distance),(object_distance+2)],[17,14], linewidth=4.0, color="black")  

        plt.plot([image_distance,image_distance],[0,17], linewidth=4.0, color="grey")
        plt.plot([(image_distance-2),(image_distance)],[14,17], linewidth=4.0, color="grey")
        plt.plot([(image_distance),(image_distance+2)],[17,14], linewidth=4.0, color="grey")

        plt.ylim(0,100)
        plt.xlim(-60,60)
        plt.ylabel('Length')
        plt.xlabel('Length')
        plt.annotate(xy=[-35,90],s="Object")
        plt.annotate(xy=[25,90],s="Image")

        plt.show()
        
    