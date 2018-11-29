#! python3
# bmi.py - BMI calculation app.

def getName():
    #Collects a name input
    print('Please state your name:')
    name = input().title()
    return name

name = getName()

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
        height = input('Enter your height value: ')
        if float_test(height) == True:
            height = float(height)
            return height
            break
        else:
            print('\nInvalid input for height! Try again.')
                   
def getHeightUnit():
    # Function to receive input values for height unit and ensure that inputs are
    # In the required format and return them for further use
    while True:
        heightUnit = input('\nWhat is the height unit?: ').lower()
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
            print('\nInvalid input for height unit!')
            print('Enter milimeters(mm) or centimeters(cm) or meters(m)')

def getWeight():
    # Function to receive input values for weight and ensure that inputs are
    # In the required format and return them for further use
    while True:
        weight = input('\nEnter your weight value: ')
        if float_test(weight) == True:
            weight = float(weight)
            return weight
            break
        else:
            print('\nInvalid input for weight! Try again.')
                   
def getWeightUnit():
    # Function to receive input values for weight unit and ensure that inputs are
    # In the required format and return them for further use
    while True:
        weightUnit = input('\nWhat is the weight unit?: ').lower()
        if weightUnit.startswith('kg') or weightUnit.startswith('po') or weightUnit.startswith('lb'):
            if weightUnit.startswith('kg') or weightUnit.startswith('kil'):
                return 'kilograms'
                break            
            elif weightUnit.startswith('po') or weightUnit.startswith('lbs'):
                return 'pounds'
                break
        else:
            print('\nInvalid input for weight unit!')
            print('Enter kilograms(kg) or pounds(lbs)')

height = getHeight()
heightUnit = getHeightUnit()
weight = getWeight()
weightUnit = getWeightUnit()

def get_st_height(height, heightUnit):
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

def get_st_weight(weight, weightUnit):
    #Returns a weight value in the standard unit
    if weightUnit.startswith('ki'):
        st_weight = weight
        return st_weight
    elif weightUnit.startswith('po'):
        st_weight = weight/2.205
        st_weight = round(st_weight, 1)
        return st_weight

st_height = get_st_height(height, heightUnit)
st_weight = get_st_weight(weight, weightUnit)
values = {st_height: heightUnit, st_weight: weightUnit}

print('\n' + name.center(23))
print('*' * 23)
print('Height' + '_ ' * 5 + str(st_height) + 'm')
print('Weight' + '_ ' * 5 + str(st_weight) + 'kg')
print()
print('BMI = Weight(kg)/(Height)(Height)(m)')
print('    = ' + str(round(st_weight/(st_height)**2, 2)))
