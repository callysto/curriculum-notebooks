digit_answers=[1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8,8,4,1,9,7,1]
current_position=0
number_of_mistakes=5
number_of_mistakes_left=number_of_mistakes
digit_widgets=[]
for i in range(len(digit_answers)):
    digit_widgets.append(widgets.Text(value='',disabled=True,layout=widgets.Layout(width='3%')))
pi_real=widgets.HTMLMath(value="$$\pi=3.$$")
next_number=widgets.HTML(value="Select the next digit:")
answer_text=widgets.Select(options=['0','1','2','3','4','5','6','7','8','9'],value='0',
    description='',disabled=False,layout=widgets.Layout(width='10%'))
warning=widgets.HTML(value="")
mistakes=widgets.HTML(value="Mistakes left: <font color='red'>"+str(number_of_mistakes_left)+"</font>")
reset_button=widgets.Button(description='Reset',disabled=False)
def on_digit_selected(b):
    global current_position,number_of_mistakes_left
    if answer_text.value == str(digit_answers[current_position]):
        digit_widgets[current_position].value=answer_text.value
        current_position=current_position+1
        warning.value="<font color='green'> Correct! </font>"
    else:
        warning.value="<font color='red'> Not quite... </font>"
        number_of_mistakes_left=number_of_mistakes_left-1
        mistakes.value="Mistakes left: <font color='red'>"+str(number_of_mistakes_left)+"</font>"
    if number_of_mistakes_left==0 or current_position==len(digit_answers):
        b.disabled=True
        answer_text.disabled=True
        for i in range(len(digit_answers)):
            digit_widgets[i].value=str(digit_answers[i])
        warning.value="<font color='red'> You scored "+str(current_position)+"! Run the code cell again to start over.</font>"
answer_text.observe(on_digit_selected, names='value')
display(Markdown("**How many digits of $\pi$ can you remember?**"))
display(widgets.HBox([pi_real]+digit_widgets[:17]))
display(widgets.HBox(digit_widgets[17:]))
display(widgets.HBox([next_number,answer_text,warning]))
display(widgets.HBox([mistakes]))