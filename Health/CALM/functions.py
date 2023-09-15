import ipywidgets as widgets

def create_widget(type,description,value,min,max,step):
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
                    min=min,
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
                    layout= widgets.Layout(height='150px'),
                    style=dict(description_width='initial'),
                    disabled=False,
                )
        case _:
            return None
        
def calculateFederalTax(income):
    """
    Calculates the federal tax based on the given income.

    Parameters:
        income (float): The income on which the federal tax needs to be calculated.

    Returns:
        float: The calculated federal tax.

    """
    
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
    """
    Calculate the provincial tax based on the given income.

    Parameters:
        income (float): The income on which the provincial tax is calculated.

    Returns:
        float: The amount of provincial tax calculated based on the income.
    """

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
    """
    Calculate the employment insurance (EI) premium based on the given income.

    Parameters:
        income (float): The income of the individual.

    Returns:
        float: The calculated EI premium.
    """

    eiMaxInsurableEarnings = 53100
    eiRate = 0.0162
    if income >= eiMaxInsurableEarnings:
        eiPremium = eiMaxInsurableEarnings * eiRate
    else:
        eiPremium = income * eiRate
    return eiPremium

def calculateCPP(income):
    """
    Calculates the CPP (Canada Pension Plan) premium based on the given income.

    Parameters:
        income (float): The income of an individual.

    Returns:
        float: The calculated CPP premium.
    """

    cppMaxContributoryEarnings = 53900
    cppRate = 0.051
    if income >= cppMaxContributoryEarnings:
        cppPremium = cppMaxContributoryEarnings * cppRate
    else:
        cppPremium = income * cppRate
    return cppPremium

