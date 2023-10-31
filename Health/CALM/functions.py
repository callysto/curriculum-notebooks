import ipywidgets as widgets

def create_widget(type1, description, value, min=None, max=None, step=None):
    match type1:
        case 'Text':
            return widgets.Text(
                value=value,
                description=description,
                disabled=False,
                indent=False,
                layout=widgets.Layout(width='400px'),
                style=dict(description_width='initial'),
            )
        case 'TextArea':
            return widgets.Textarea(
                value=value,
                description=description,
                disabled=False,
                indent=False,
                layout=widgets.Layout(width='400px', height='100px'),
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
                min=value,
                max=max,
                step=step,
                description=description,
                disabled=False,
                layout=widgets.Layout(width='500px'),
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
                layout=widgets.Layout(width='500px'),
                style=dict(description_width='initial'),
            )
        case 'SelectM':
            return widgets.SelectMultiple(
                options=value,
                value=[],
                description=description,
                layout=widgets.Layout(height='150px'),
                style=dict(description_width='initial'),
                disabled=False,
            )
        case 'Radio':
            return widgets.RadioButtons(
                options=value,
                description=description,
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

    taxBrackets = [0, 53359, 106717, 165430, 235675, float('inf')]
    taxRates = [0.15, 0.205, 0.26, 0.29, 0.33]
    bpa  = 15000 # basic personal allowance deduction

    income -= bpa
    fed_tax = 0
    for i in range(len(taxBrackets)-1):
        if (income >= taxBrackets[i]) and (income <= taxBrackets[i+1]):
            fed_tax = (income-taxBrackets[i])*taxRates[i] + \
                sum({(taxBrackets[j+1]-taxBrackets[j])*taxRates[j] for j in range(i)})
    return fed_tax

def calculateProvincialTax(income):
    """
    Calculate the provincial tax based on the given income, for Alberta.

    Parameters:
        income (float): The income on which the provincial tax is calculated.

    Returns:
        float: The amount of provincial tax calculated based on the income.
    """

    taxBrackets = [0, 142292, 170751, 227668, 341502, float('inf')]
    taxRates = [0.10, 0.12, 0.13, 0.14, 0.15]
    bpa  = 15000 # basic personal allowance deduction

    income -= bpa
    prov_tax = 0
    for i in range(len(taxBrackets)-1):
        if (income >= taxBrackets[i]) and (income <= taxBrackets[i+1]):
            prov_tax = (income-taxBrackets[i])*taxRates[i] + \
                sum({(taxBrackets[j+1]-taxBrackets[j])*taxRates[j] for j in range(i)})

    return prov_tax

def calculateEI(income):
    """
    Calculate the employment insurance (EI) premium based on the given income.

    Parameters:
        income (float): The income of the individual.

    Returns:
        float: The calculated EI premium.
    """

    eiMaxInsurableEarnings = 61500
    eiRate = 0.0163
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

    cppMaxContributoryEarnings = 63100
    cppExempt = 3500
    cppRate = 0.0595
    if income >= cppMaxContributoryEarnings:
        cppPremium = (cppMaxContributoryEarnings - cppExempt)* cppRate
    else:
        cppPremium = max(0,income - cppExempt) * cppRate
    return cppPremium
