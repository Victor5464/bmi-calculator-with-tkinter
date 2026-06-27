

def bmi_calculator(weight, height):
    '''Takes weight and height as parameters and converts to bmi value'''
    
    if height <=0:
        return None, 'Height must be greater than zero'
    
    bmi_value= weight/height**2
    if bmi_value < 18.5:
        category = 'Underweight'
    elif 18.5<= bmi_value <=24.9:
        category = 'Normal'
    elif 25<= bmi_value<= 29.9:
        category='Overweight'
    else:
        category= 'Obese'

    return bmi_value, category


