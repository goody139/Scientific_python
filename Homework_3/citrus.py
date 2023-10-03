""" Class definition for a citrus plant. """

import random
from secrets import choice


class Citrus:
    def __init__(self, species=None, possible_species=("Pomelo", "Mandarin", "Citron") ):
        
        self.possible_species = possible_species
        
        # initialize species randomly if not defined
        if(species == None):
            self.species = random.choice(self.possible_species)
        
        else: 
            self.species = species

    
    def __str__(self):
        return "<Citrus of species {}>".format(self.species)

    def __add__(self, other): 
        """crossover operation, representing the genetic crossing of two citrus plants. """
        

        # raise Type Error if fruits are not of type Citrus 
        if not type(other).__name__ == "Citrus":
            raise TypeError('The plants have to be of type Citrus in order to be crossed.')


        # check how fruits should be crossed 
            
        match_list = [ ["Pomelo", "Mandarin"], ["Pomelo", "Sweet Orange"], 
            ["Wildleaf Mandarin", "Sweet Orange"], ["Citron","Bitter Orange"]] 
        
        if self.species == other.species:
            return Citrus(self.species) 
        
        elif self.species in match_list[0] and other.species in match_list[0]:
            p_spec = ("Sweet Orange", "Tangerine", "Satsuma", "Wildleaf Mandarin", "Bitter Orange")
            return Citrus(random.choice(p_spec))
        
        elif self.species in match_list[1] and other.species in match_list[1]:
            return Citrus(species = "Grapefruit")
        
        elif self.species in match_list[2] and other.species in match_list[2]:
            return Citrus(species = "Clementine")
        
        elif self.species in match_list[3] and other.species in match_list[3]: 
            return Citrus(species = "Lemon")
        
        else: 
            random_l = (self.species, other.species)
            return Citrus(random.choice(random_l))



    def __radd__(self, other): 
        print("radd function")
        raise TypeError('The plants have to be of type Citrus in order to be crossed.')