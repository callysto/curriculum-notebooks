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
        case 'SelectM':
            return widgets.SelectMultiple(
                    options=value,
                    value=[],
                    description=description,
                    disabled=False,
                )
        case _:
            return None
        
def calculateFederalTax(income):
    taxBrackets = [47630, 95259, 147667, 210371]
    taxRates = [.15, .205, .26, .29, .33]
    taxes = []
    for i in range(0, len(taxBrackets)):
        taxes.append(taxBrackets[i] * taxRates[i])
    if income < taxBrackets[0]:
        tax = income * taxRates[0]
    elif income < taxBrackets[1]:
        tax = taxes[0] + (income - taxBrackets[0]) * taxRates[1]
    elif income < taxBrackets[2]:
        tax = taxes[1] + (income - taxBrackets[1]) * taxRates[2]
    elif income < taxBrackets[3]:
        tax = taxes[2] + (income - taxBrackets[2]) * taxRates[3]
    else:
        tax = taxes[3] + (income - taxBrackets[3]) * taxRates[4]
    return tax

def calculateProvincialTax(income):
    taxBrackets = [131220, 157464, 209952, 314928] # for Alberta
    taxRates = [.1, .12, .13, .14, .15]
    taxes = []
    for i in range(0, len(taxBrackets)):
        taxes.append(taxBrackets[i] * taxRates[i])
    if income < taxBrackets[0]:
        tax = income * taxRates[0]
    elif income < taxBrackets[1]:
        tax = taxes[0] + (income - taxBrackets[0]) * taxRates[1]
    elif income < taxBrackets[2]:
        tax = taxes[1] + (income - taxBrackets[1]) * taxRates[2]
    elif income < taxBrackets[3]:
        tax = taxes[2] + (income - taxBrackets[2]) * taxRates[3]
    else:
        tax = taxes[3] + (income - taxBrackets[3]) * taxRates[4]
    return tax

def calculateEI(income):
    eiMaxInsurableEarnings = 53100
    eiRate = 0.0162
    if income >= eiMaxInsurableEarnings:
        eiPremium = eiMaxInsurableEarnings * eiRate
    else:
        eiPremium = income * eiRate
    return eiPremium

def calculateCPP(income):
    cppMaxContributoryEarnings = 53900
    cppRate = 0.051
    if income >= cppMaxContributoryEarnings:
        cppPremium = cppMaxContributoryEarnings * cppRate
    else:
        cppPremium = income * cppRate
    return cppPremium



