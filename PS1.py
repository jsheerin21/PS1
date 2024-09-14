"""
Course  : CMPSC 131, Fall 2024
File    : PS1.py 
Name    : James Sheerin

GitHub User:   jsheerin21
"""

# Part 1
# Function #1

def math_func_1(x: int):
    """
    This function takes an integer x and plugs it into a mathematical equation.
    """
    result = float(((10*x-3)/8)*(7/(4*x-3)))
    return result

# Part 1
# Function #2

def math_func_2(a: int, b: int, c: int):
    """
    This function takes three integers, a, b, and c, and plugs it into a mathematical equation.
    """
    result = float(((2%a-3)/(c*b))+(4//c)-b)
    return result

# Part 2
# Problem 2.1

def m_to_arshins(m: int):
    """
    This function takes a value in meters and converts it to arshins
    """
    arshins_per_meter = 1.406
    result = float(m*arshins_per_meter)
    return result

# Part 2
# Problem 2.2

def convert_min(num_minutes: int):
    """
    This function takes a value in minutes and returns how many years and days it would contain
    """
    minutes_in_a_year = 525600
    minutes_in_a_day = 1440
    num_years = int(num_minutes/minutes_in_a_year)
    num_days = int(((num_minutes/minutes_in_a_year) % 1) *365)
    answer = str(num_minutes) + " min = " + str(int(num_years)) + " year(s) and " + str(int(num_days)) + " day(s)"
    print(answer)
    return 1
    
# Part 3
# Problem 3.1

def calc_final_price(original_price: float, tax_rate: int):
    """
    This function takes the price of an item and returns the total cost when the tax is added.
    """
    final_price = (original_price + original_price*tax_rate/100)
    return final_price

# Part 3
# Problem 3.2

def get_displacement(vo: float, a: float, t: float):
    """
    This function takes a given initial velocity of the moving body in m/s, acceleration of the moving body in (m/s)^2,
    and elapsed time in seconds and calculates the displacement.
    """
    displacement = (vo*t)+(0.5*a*(t**2))
    return displacement

# Part 3
# Problem 3.3

def p_volume(height_pyramid: float, base_side_length: float):
    """
    This function takes the height of a square pyramid and the side length of its base and returns the volume of the pyramid.
    """
    area_of_base = base_side_length**2
    volume = (area_of_base*height_pyramid/3)
    return volume

# Part 4
# Problem 4.1

def heat_index(temp_f: float, humidity: float):
    """
    This function takes the temperature in farenheit and a number for humidity in the range 0-100 and returns the heat index.
    """
    C1 = float(-42.379)
    C2 = float(2.04901523)
    C3 = float(10.14333127)
    C4 = float(-0.22475541)
    C5 = float(-6.83783*(10**(-3)))
    C6 = float(-5.481717*(10**(-2)))
    C7 = float(1.22874*(10**(-3)))
    C8 = float(8.5282*(10**(-4)))
    C9 = float(-1.99*(10**(-6)))
    result = float(C1 + (C2*temp_f) + (C3*humidity) + (C4*temp_f*humidity) + (C5*(temp_f**2)) + (C6*(humidity**2)) + (C7*(temp_f**2)*humidity) + (C8*temp_f*(humidity**2)) + (C9*(temp_f**2)*(humidity**2)))
    return float(result)

# Part 4
# Problem 4.2

def round_to_two(number: float):
    """
    This function takes a number and rounds it to two decimal places.
    """
    integer = number // 1
    decimal = number % 1
    two_decimals = (decimal * 100)
    rounded_decimal = (two_decimals + 0.5) // 1
    result = integer + (rounded_decimal / 100)
    return result

# Part 4
# Problem 4.3

def get_apparent_temperature(temp_f: float, humidity: float):
    """
    This function takes a temperature in farenheit and a humidity between 0-100 and returns a feels-like temperature rounded to two
    decimal places
    """
    heat_index_1 = float(heat_index(temp_f, humidity))
    answer = str(float(temp_f)) + " F and " + str(float(humidity)) + " % humidity feels like " + str(round_to_two(heat_index_1)) + " F"
    print(answer)
    return float(heat_index_1)


def main():
    #-YOUR TESTS FOR YOUR FUNCTIONS STARTS HERE (TODO)
    print(round_to_two(65.2))

if __name__ == "__main__":
    main()