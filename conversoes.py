def celcius_p_fahrenheit(c):
    temp_fahrenheit =(c * 9 / 5) + 32
    return temp_fahrenheit

def celcius_p_kelvin(c):
    temp_kelvin = c + 273.15
    return temp_kelvin 

def fahrenheit_p_celcius(f):
    temp_celcius = 5/9 * (f-32)   
    return temp_celcius

def fahrenheit_p_kelvin(f):
    temp_kelvin = (f-32) * 5/9 + 273.15
    return temp_kelvin

def kelvin_p_celcius(k):
    temp_celcius = k - 273.15
    return temp_celcius

def kelvin_p_fahrenheit(k):
   temp_fahrenheit = (k - 273.15) * 9/5 + 32
   return temp_fahrenheit