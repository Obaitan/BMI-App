#! python3
# bmi.py - BMI calculation app.

def getName():
    #Collects a name input
    print('Please state your name:')
    name = input().title()
    return name

def float_test(number):
    #Tests if argument is numeric string and converts it to a float
    #Also provides error handling for invalid inputs
    try:
        number = float(number)
        return True
    except ValueError:
        return False

def getHeight():
    # Function to receive input values for height and ensure that inputs are
    # In the required format and return them for further use
    while True:
        print('Enter your height value only:')
        height = input()
        if float_test(height) == True:
            height = float(height)
            return height
            break
        else:
            print('Invalid input for height! Enter height figure only.')
                   
def getHeightUnit():
    # Function to receive input values for height unit and ensure that inputs are
    # In the required format and return them for further use
    while True:
        print('What is the height unit?:')
        heightUnit = input().lower()
        if heightUnit.startswith('m') or heightUnit.startswith('c'):
            if heightUnit.startswith('mm') or heightUnit.startswith('mil'):
                return 'milimeters'
                break            
            elif heightUnit.startswith('cm') or heightUnit.startswith('cen'):
                return 'centimeters'
                break
            elif heightUnit.startswith('m') or heightUnit.startswith('met'):
                return 'meters'
                break
        else:
            print('Invalid input for height unit!')
            print('Enter milimeters(mm) or centimeters(cm) or meters(m)')

def getWeight():
    # Function to receive input values for weight and ensure that inputs are
    # In the required format and return them for further use
    while True:
        print('Enter your weight value only: ')
        weight = input()
        if float_test(weight) == True:
            weight = float(weight)
            return weight
            break
        else:
            print('Invalid input for weight! Enter weight figure only.')
                   
def getWeightUnit():
    # Function to receive input values for weight unit and ensure that inputs are
    # In the required format and return them for further use
    while True:
        print('What is the weight unit?:')
        weightUnit = input().lower()
        if weightUnit.startswith('kg') or weightUnit.startswith('po') or weightUnit.startswith('lb'):
            if weightUnit.startswith('kg') or weightUnit.startswith('kil'):
                return 'kilograms'
                break            
            elif weightUnit.startswith('po') or weightUnit.startswith('lbs'):
                return 'pounds'
                break
        else:
            print('Invalid input for weight unit!')
            print('Enter kilograms(kg) or pounds(lbs)')


print("""BMI - Body Mass Index is a measurement of
a person's weight with respect to his/her
height. It is more of an indicator than a
direct measurement of a person's total body
body fat.

Usually, as a person's BMI increases, so
does his/her total body fat.\n""")

print('BMI CATEGORIES'.center(20))
print("""Underweight   = < 19.0
Normal Weight = 19.0 - 25.0
Overweight    = 25.0 - 30.0
Obesity       = > 30.0""")
print('\nLet\'s calculate yours!\n')

name = getName()
height = getHeight()
heightUnit = getHeightUnit()
weight = getWeight()
weightUnit = getWeightUnit()

def get_st_height():
    #Returns a height value in the standard unit
    if heightUnit.startswith('mi'):
        st_height = height/1000
        return st_height
    elif heightUnit.startswith('ce'):
        st_height = height/100
        return st_height
    elif heightUnit.startswith('me'):
        st_height = height
        return st_height

def get_st_weight():
    #Returns a weight value in the standard unit
    if weightUnit.startswith('ki'):
        st_weight = weight
        return st_weight
    elif weightUnit.startswith('po'):
        st_weight = weight/2.205
        st_weight = round(st_weight, 1)
        return st_weight

st_height = get_st_height()
st_weight = get_st_weight()
values = {st_height: heightUnit, st_weight: weightUnit}

def get_BMI():
    #Calculates the bmi
    global bmi
    bmi = round(st_weight/(st_height)**2, 2)
    return bmi

bmi = get_BMI()

def bmi_analysis():
    #Analyses the bmi
    if bmi < 19.0:
        return 'Your BMI is under 19.0.\n -You are probably underweight and should see a doctor.'
    elif bmi > 19.0 and bmi < 25.0:
        return 'Your BMI is within the normal range.\n -Your body fat is probably fine.'
    elif bmi > 25.0 and bmi < 30.0:
        return 'Your BMI is within the overweight range.\n -You should see a doctor.'
    elif bmi > 30:
        return 'Your BMI is rather high at over 30.\n -Please see a doctor!.'
    
Analysis = bmi_analysis()

print('\n' + name.center(23))
print('*' * 23)
print('Height' + '_ ' * 5 + str(st_height) + 'm')
print('Weight' + '_ ' * 5 + str(st_weight) + 'kg')
print()
print("BMI = Weight(kg)/{}\u00b2(m)".format('Height'))
print('    = ' + str(bmi))
print('ANALYSIS:')
print(' -' + Analysis)
