""" Class definition for a garden with plants. """

from citrus import Citrus

import random


class Garden:

    def __init__(self, plants = []):
        """ Args: plants(list)"""
        self.plants = []


    def __len__(self):
        """returns lenght of plant"""
        return len(self.plants)

    def __str__(self):
        """ Provides information about garden. """
        num_spec=[]
        for spec in self.plants: 
            num_spec.append(spec.species)
        num_spec = set(num_spec)
        return "<Garden with {} ".format(len(self.plants)) +  "plants and {} species>".format(len(num_spec))
        

    def plant(self, new_plant = None):
        if(new_plant == None):
            self.plants.append(Citrus())
               
        else: 
            self.plants.append(new_plant)


    def cross(self):
        if len(self.plants) >= 2: 
            # cross 2 random plants in garden and plant the result 
            two_p = random.choices(self.plants, k=2)
            crossed_p = two_p[0] + two_p[1]
            self.plant(crossed_p)
