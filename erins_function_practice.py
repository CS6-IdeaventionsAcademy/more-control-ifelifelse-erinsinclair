#Erin J Sinclair
#121217
#Function Practice
import math
import time

def cheese():
    """Makes a screen full of llamas and bunnies and lambs and goats and cows and salamanders and lemurs and more  !"""
    print("llama  lamb  bunny  cow  goat  salamander  lemur  frog  lizard  turtle  bat  chicken!  "*1000)

def temp_C(temp_F):
    '''Converts a temperature in Fahrenheit to Celsius
    temp_F is the temperature in Fahrenheit.'''
    time.sleep(0.5)
    print ("Calculating...")
    time.sleep(1)
    answer = (temp_F-32) * 5/9
    return answer

def volume_of_sphere(radius):
    '''Calculates the volume of a sphere. Radius is an integer or a float.'''
    volume=(4/3)*math.pi*r**3
    time.sleep(0.5)
    print ("Calculating...")
    time.sleep(1)
    return volume


cheese()

t_in_F =input ("Please enter a temperature in Fahrenheit: ")
t_in_F = float (t_in_F)
t_in_C = temp_C (t_in_F)

print (t_in_F, "degrees in Celcius is", str (t_in_C),"degrees.")
time.sleep(3)
       

r=input ("Please enter the radius of a sphere: ")
r=float (r)
v = volume_of_sphere(r)
print ("The volume of a sphere with radius", r ,"is", str(v))
