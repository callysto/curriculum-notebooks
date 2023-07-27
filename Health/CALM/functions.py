import ipywidgets as widgets

def create_widget(type,description,value,max,step):
    match type:
        case 'Text':
            return widgets.Text(
                    value=value,
                    description=description,
                    disabled=False,
                    indent=False, 
                    layout= widgets.Layout(width='400px'), 
                    style=dict(description_width='initial'),
                )
        case 'TextArea':
            return widgets.Textarea(
                    value=value,
                    description=description,
                    disabled=False,
                    indent=False, 
                    layout= widgets.Layout(width='400px',height='100px'), 
                    style=dict(description_width='initial'),
                )
        case 'Checkbox':
            return widgets.Checkbox(
                    value=value,
                    description=description,
                    disabled=False,
                    indent=False,
                )
        case 'IntSlider':
            return widgets.IntSlider(
                    value=value,
                    min = value,
                    max= max,
                    step = step,
                    description=description,
                    disabled=False,
                    layout= widgets.Layout(width='500px'),
                    style=dict(description_width='initial'),
                )
        case 'IntRangeSlider':
            return widgets.IntRangeSlider(
                    value=value,
                    min=0,
                    max=max,
                    step=step,
                    description=description,
                    disabled=False,
                    continuous_update=False,
                    layout= widgets.Layout(width='500px'),
                    style=dict(description_width='initial'),           
                )
        case _:
            return None