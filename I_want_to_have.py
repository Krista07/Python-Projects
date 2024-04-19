#This is a very simple randomization project that outputs a random place on the list for the user.
#If the user doesn't want to go to the randomly selected place, they can restart the script.

import random

#List of Resturants or food types
resturants = ['Taco Bell', 
                   'Chino Banditos', 
                   'Jack in the Box', 
                   'Great Wall', 
                   'Phoenix Palace',
                   'Korean BBQ', 
                   'Sushi', 
                   'Indian', 
                   'Thai', 
                   'Pho', 
                   'Raising Canes', 
                   'Churches Chicken', 
                   'Popeyes', 
                   'Chick-Fil-A', 
                   'Jin Shabu', 
                   'Tacos',
                   'Dim Sum',
                   'Chipotle']

#Shows a simple starting text with a random variable from the list above
print("I want to have", resturants[random.randint(0, len(resturants) - 1)])
