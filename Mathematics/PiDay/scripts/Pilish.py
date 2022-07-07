pi_digits=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8,8,4,1,9,7,1]
text_area1=widgets.Textarea(placeholder='Type something(up to 32 words)',disabled=False,layout=widgets.Layout(height='100px'))
text_area2=widgets.Textarea(disabled=True,layout=widgets.Layout(height='100px'))
submit_button=widgets.Button(description='Submit',button_style='info',disabled=False)
reset_button1=widgets.Button(description='Reset',disabled=False)
warning1=widgets.HTML(value=" ")
def on_button_reset1_clicked(b):
    text_area1.value=""
    text_area2.value=""
    warning1.value=""
reset_button1.on_click(on_button_reset1_clicked)
def on_button_submit_clicked(b):
    text=re.sub(r'[^\w\s]',' ',text_area1.value)
    text = re.sub("\d+", "", text)
    text_list=text.split()
    text_len=len(text_list)
    if text_len==0:
        text_area1.value=""
        warning1.value="There is no text, try again!"
    else:
        if text_len>32:
            text_len=32
            text_list=text_list[:text_len]
        pi_subset=pi_digits[:text_len]
        text_list1=[]
        word_length=[]
        for word in text_list:
            lenw=len(word)
            word_length.append(lenw)
            text_list1.append(word+"("+ str(lenw)+")")
        if word_length==pi_subset:
            warning1.value=" <font color='green'> Well done! This is written in Pilish!</font>"
        else:
            warning1.value=" <font color='red'>Not quite. Your sequence is "+' '.join(str(word_length))+", it needs to be "+' '.join(str(pi_subset))+"</font>"
        text_area2.value=' '.join(text_list1)
submit_button.on_click(on_button_submit_clicked)
display(Markdown("**Can you write in Pilish?** Remember $\pi=3.1415926535897932384626433832795028841971$..."))
display(Markdown("**Note**: numbers and special characters are excluded."))
vbox1=widgets.VBox([text_area1,widgets.HBox([submit_button,reset_button1])])
vbox2=widgets.VBox([text_area2,warning1])                
display(widgets.HBox([vbox1,vbox2]))