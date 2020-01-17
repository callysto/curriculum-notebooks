#----------

#Import modules and packages 
import ipywidgets as widgets
import random

from ipywidgets import Output, IntSlider, VBox, HBox, Layout
from IPython.display import clear_output, display, HTML

#----------

#import ipywidgets as widgets
#import random

#This function produces a multiple choice form with four options
def multiple_choice(option_1, option_2, option_3, option_4):
    option_list = [option_1, option_2, option_3, option_4]
    answer = option_list[0]
    letters = ["<b>(A)</b> ", "<b>(B)</b> ", "<b>(C)</b> ", "<b>(D)</b> "]

    #Randomly shuffle the options
    random.shuffle(option_list)
    
    #Print the letters (A) to (D) in sequence with randomly chosen options
    for i in range(4):
        option_text = option_list.pop()
        option_text_2 = letters[i] + option_text
        option_output = widgets.HTMLMath(value=option_text_2)
        display(option_output)
                
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
        if "<b>(A)</b> " == letter_answer:
            print("Correct!    ", end='\r')
            button1.style.button_color = 'Moccasin'; button2.style.button_color = 'Whitesmoke'
            button3.style.button_color = 'Whitesmoke'; button4.style.button_color = 'Whitesmoke'
        else:
            print("Try again.", end='\r')
            button1.style.button_color = 'Lightgray'; button2.style.button_color = 'Whitesmoke'
            button3.style.button_color = 'Whitesmoke'; button4.style.button_color = 'Whitesmoke'

    def on_button2_clicked(b):
        if "<b>(B)</b> " == letter_answer:
            print("Correct!    ", end='\r')
            button1.style.button_color = 'Whitesmoke'; button2.style.button_color = 'Moccasin'
            button3.style.button_color = 'Whitesmoke'; button4.style.button_color = 'Whitesmoke'
        else:
            print("Try again.", end='\r')
            button1.style.button_color = 'Whitesmoke'; button2.style.button_color = 'Lightgray'
            button3.style.button_color = 'Whitesmoke'; button4.style.button_color = 'Whitesmoke'

    def on_button3_clicked(b):
        if "<b>(C)</b> " == letter_answer:
            print("Correct!    ", end='\r')
            button1.style.button_color = 'Whitesmoke'; button2.style.button_color = 'Whitesmoke'
            button3.style.button_color = 'Moccasin'; button4.style.button_color = 'Whitesmoke'
        else:
            print("Try again.", end='\r')
            button1.style.button_color = 'Whitesmoke'; button2.style.button_color = 'Whitesmoke'
            button3.style.button_color = 'Lightgray'; button4.style.button_color = 'Whitesmoke'

    def on_button4_clicked(b):
        if "<b>(D)</b> " == letter_answer:
            print("Correct!    ", end='\r')
            button1.style.button_color = 'Whitesmoke'; button2.style.button_color = 'Whitesmoke'
            button3.style.button_color = 'Whitesmoke'; button4.style.button_color = 'Moccasin'
        else:
            print("Try again.", end='\r')
            button1.style.button_color = 'Whitesmoke'; button2.style.button_color = 'Whitesmoke'
            button3.style.button_color = 'Whitesmoke'; button4.style.button_color = 'Lightgray'

    button1.on_click(on_button1_clicked); button2.on_click(on_button2_clicked)
    button3.on_click(on_button3_clicked); button4.on_click(on_button4_clicked)

#----------
#This function produces a true or false choice form with four options
def true_false(option_1, bool_1, option_2, bool_2, option_3, bool_3, option_4, bool_4, button_text_1, button_text_2):
 
    #Convert string to HTMLMath so equations can be displayed
    TF_question_1 = widgets.HTMLMath(value=option_1)
    TF_question_2 = widgets.HTMLMath(value=option_2)
    TF_question_3 = widgets.HTMLMath(value=option_3)
    TF_question_4 = widgets.HTMLMath(value=option_4)
    
    #Create true and false bottons
    button1_1 = widgets.Button(description=button_text_1); button1_2 = widgets.Button(description=button_text_2)
    button2_1 = widgets.Button(description=button_text_1); button2_2 = widgets.Button(description=button_text_2)
    button3_1 = widgets.Button(description=button_text_1); button3_2 = widgets.Button(description=button_text_2)
    button4_1 = widgets.Button(description=button_text_1); button4_2 = widgets.Button(description=button_text_2)
    
    button1_1.style.button_color = 'Whitesmoke'; button1_2.style.button_color = 'Whitesmoke'
    button2_1.style.button_color = 'Whitesmoke'; button2_2.style.button_color = 'Whitesmoke'
    button3_1.style.button_color = 'Whitesmoke'; button3_2.style.button_color = 'Whitesmoke'
    button4_1.style.button_color = 'Whitesmoke'; button4_2.style.button_color = 'Whitesmoke'

    #Display buttons in front of each question 
    container1 = widgets.HBox(children=[button1_1,button1_2,TF_question_1])
    container2 = widgets.HBox(children=[button2_1,button2_2,TF_question_2]) 
    container3 = widgets.HBox(children=[button3_1,button3_2,TF_question_3])
    container4 = widgets.HBox(children=[button4_1,button4_2,TF_question_4])
    
    #Place true or false questions in an array so they can be shuffled
    containers = [container1, container2, container3, container4]
    random.shuffle(containers)
    
    #Reassign containers and display
    container1 = containers[0]; container2 = containers[1]
    container3 = containers[2]; container4 = containers[3]
    display(container1, container2, container3, container4)
    print(" ", end='\r')

    def on_button1_1_clicked(b):
        if bool_1 == True:
            print("Correct!    ", end='\r')
            button1_1.style.button_color = 'Moccasin'; button1_2.style.button_color = 'Whitesmoke'
        else:
            print("Try again.", end='\r')
            button1_1.style.button_color = 'Lightgray'; button1_2.style.button_color = 'Whitesmoke'

    def on_button1_2_clicked(b):
        if bool_1 == False:
            print("Correct!    ", end='\r')
            button1_1.style.button_color = 'Whitesmoke'; button1_2.style.button_color = 'Moccasin'
        else:
            print("Try again.", end='\r')
            button1_1.style.button_color = 'Whitesmoke'; button1_2.style.button_color = 'Lightgray'

            
    def on_button2_1_clicked(b):
        if bool_2 == True:
            print("Correct!    ", end='\r')
            button2_1.style.button_color = 'Moccasin'; button2_2.style.button_color = 'Whitesmoke'
        else:
            print("Try again.", end='\r')
            button2_1.style.button_color = 'Lightgray'; button2_2.style.button_color = 'Whitesmoke'

    def on_button2_2_clicked(b):
        if bool_2 == False:
            print("Correct!    ", end='\r')
            button2_1.style.button_color = 'Whitesmoke'; button2_2.style.button_color = 'Moccasin'
        else:
            print("Try again.", end='\r')
            button2_1.style.button_color = 'Whitesmoke'; button2_2.style.button_color = 'Lightgray'        
            
    
    def on_button3_1_clicked(b):
        if bool_3 == True:
            print("Correct!    ", end='\r')
            button3_1.style.button_color = 'Moccasin'; button3_2.style.button_color = 'Whitesmoke'
        else:
            print("Try again.", end='\r')
            button3_1.style.button_color = 'Lightgray'; button3_2.style.button_color = 'Whitesmoke'

    def on_button3_2_clicked(b):
        if bool_3 == False:
            print("Correct!    ", end='\r')
            button3_1.style.button_color = 'Whitesmoke'; button3_2.style.button_color = 'Moccasin'
        else:
            print("Try again.", end='\r')
            button3_1.style.button_color = 'Whitesmoke'; button3_2.style.button_color = 'Lightgray'
    
    def on_button4_1_clicked(b):
        if bool_4 == True:
            print("Correct!    ", end='\r')
            button4_1.style.button_color = 'Moccasin'; button4_2.style.button_color = 'Whitesmoke'
        else:
            print("Try again.", end='\r')
            button4_1.style.button_color = 'Lightgray'; button4_2.style.button_color = 'Whitesmoke'

    def on_button4_2_clicked(b):
        if bool_4 == False:
            print("Correct!    ", end='\r')
            button4_1.style.button_color = 'Whitesmoke'; button4_2.style.button_color = 'Moccasin'
        else:
            print("Try again.", end='\r')
            button4_1.style.button_color = 'Whitesmoke'; button4_2.style.button_color = 'Lightgray'
    
    button1_1.on_click(on_button1_1_clicked); button1_2.on_click(on_button1_2_clicked)
    button2_1.on_click(on_button2_1_clicked); button2_2.on_click(on_button2_2_clicked)
    button3_1.on_click(on_button3_1_clicked); button3_2.on_click(on_button3_2_clicked)
    button4_1.on_click(on_button4_1_clicked); button4_2.on_click(on_button4_2_clicked)