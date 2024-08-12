##The Pet Adoption Center

##Part 1: The Adoption Center.

##get_name()- Returns the name of the adoption center
##get_location()- Returns the location of the adoption center
##get_species_count()- Returns a copy of the full list and count of the available species at the adoption center.
##get_number_of_species(species_name)- Returns the number of a given species that the adoption center has.
##adopt_pet(species_name)- Decrements the value of a specific species at the adoption center and does not return anything.



class AdoptionCenter:
    """
    The AdoptionCenter class stores the important information that a
    client would need to know about, such as the different numbers of
    species stored, the location, and the name. It also has a method to adopt a pet.
    """
    def __init__(self, name, species_types, location):
        self.name = name
        self.species_types = species_types
        self.location = location

    def get_name(self):
        return self.name

    def get_number_of_species(self, animal):
        if animal in self.species_types.keys():
            return self.species_types[animal]
        else:
            return 0

    def get_location(self):
        return tuple(map(float, self.location))

    def get_species_count(self):
        species_count_copy = self.species_types.copy()
        return species_count_copy

    def adopt_pet(self, species_name):
        try:
            if self.get_number_of_species(species_name) > 0:
                self.species_types[species_name] = self.species_types.get(species_name) - 1
            if self.get_number_of_species(species_name) == 0:
                del self.species_types[species_name]
        except KeyError:
            pass

##Part 2A: The Adopter.
##name- A string that represents the name of the adopter
##desired_species- A string that represents the desired species to adopt
##Adopter Methods
##get_name() - Returns the name of the adopter
##get_desired_species() - Returns the desired species of the adopter
##get_score(adoption_center) - Returns the score (details below)

class Adopter:
    """ 
    Adopters represent people interested in adopting a species.
    They have a desired species type that they want, and their score is
    simply the number of species that the shelter has of that species.
    """
    def __init__(self, name, desired_species):
        self.name = name
        self.desired_species = desired_species

    def get_name(self):
        return self.name 

    def get_desired_species(self):
        return self.desired_species 

    def get_score(self, adoption_center):
        num_desired = adoption_center.get_number_of_species(self.desired_species)
        return float(1 * num_desired)

##Part 2B: Flexible and Fearful Adopters
##The next two types of adopters will be the FlexibleAdopter and the FearfulAdopter,
##and both will be subclasses of the base Adopter class.

class FlexibleAdopter(Adopter):
    """
    A FlexibleAdopter still has one type of species that they desire,
    but they are also alright with considering other types of species.
    considered_species is a list containing the other species the adopter will consider
    Their score should be 1x their desired species + .3x all of their desired species
    """
    def __init__(self, name, desired_species, considered_species):
        Adopter.__init__(self, name, desired_species)
        self.considered_species = list(considered_species)

    def get_score(self, adoption_center):
        num_other = 0.3 * sum([adoption_center.get_species_count().get(c, 0) for c in self.considered_species])
        return Adopter.get_score(self, adoption_center) + num_other


class FearfulAdopter(Adopter):
    """
    A FearfulAdopter is afraid of a particular species of animal.
    If the adoption center has one or more of those animals in it, they will
    be a bit more reluctant to go there due to the presence of the feared species.
    Their score should be 1x number of desired species - .3x the number of feared species
    """
    def __init__(self, name, desired_species, feared_species):
        Adopter.__init__(self, name, desired_species)
        self.feared_species = str(feared_species)

    def get_score(self, adoption_center):
        adopter_score = float(Adopter.get_score(self, adoption_center))
        num_feared = adoption_center.get_number_of_species(self.feared_species)

        return float(max(0.0, adopter_score - ( 0.3 * num_feared)))

##Part 2C: AllergicAdopter and MedicatedAllergicAdopter

class AllergicAdopter(Adopter):
    """
    An AllergicAdopter is extremely allergic to a one or more species and cannot
    even be around it a little bit! If the adoption center contains one or more of
    these animals, they will not go there.
    Score should be 0 if the center contains any of the animals, or 1x number of desired animals if not
    """
    def __init__(self, name, desired_species, allergic_species):
        Adopter.__init__(self, name, desired_species)
        self.allergic_species = list(allergic_species)

    def get_score(self, adoption_center):
        for animal in self.allergic_species:
            if adoption_center.get_species_count().get(animal, 0) > 0:
                return 0.0
            
        return float(Adopter.get_score(self, adoption_center))

class MedicatedAllergicAdopter(AllergicAdopter):
    """
    A MedicatedAllergicAdopter is extremely allergic to a particular species
    However! They have a medicine of varying effectiveness, which will be given in a dictionary
    To calculate the score for a specific adoption center, we want to find what is the most allergy-inducing species that the adoption center has for the particular MedicatedAllergicAdopter. 
    To do this, first examine what species the AdoptionCenter has that the MedicatedAllergicAdopter is allergic to, then compare them to the medicine_effectiveness dictionary. 
    Take the lowest medicine_effectiveness found for these species, and multiply that value by the Adopter's calculate score method.
    """
    def __init__(self, name, desired_species, allergic_species, medicine_effectiveness):
        AllergicAdopter.__init__(self, name, desired_species, allergic_species)
        self.medicine_effectiveness = medicine_effectiveness

    def get_score(self, adoption_center):
        min_medicine_effect = 1.0

        for animal in self.allergic_species:
            if animal in adoption_center.get_species_count():
                medicine_effect = self.medicine_effectiveness.get(animal, 0)
                if medicine_effect < min_medicine_effect:
                    min_medicine_effect = medicine_effect

##Part 2D: SluggishAdopter

class SluggishAdopter(Adopter):
    """
    A SluggishAdopter really dislikes travelling. The further away the
    AdoptionCenter is linearly, the less likely they will want to visit it.
    Since we are not sure the specific mood the SluggishAdopter will be in on a
    given day, we will asign their score with a random modifier depending on
    distance as a guess.
    Score should be
    If distance < 1 return 1 x number of desired species
    elif distance < 3 return random between (.7, .9) times number of desired species
    elif distance < 5. return random between (.5, .7 times number of desired species
    else return random between (.1, .5) times number of desired species
    """
    def __init__(self, name, desired_species, location):
        Adopter.__init__(self, name, desired_species)
        self.location = tuple(location)

    def get_linear_distance(self, to_location):
        import math

        return math.sqrt((to_location[0] - self.location[0]) ** 2 + (to_location[1] - self.location[1]) ** 2)

    def get_score(self, adoption_center):
        import random
        distance = self.get_linear_distance(adoption_center.get_location())
               
        if distance < 1:
            return float(1 * Adopter.get_score(self, adoption_center))
        if 1 <= distance < 3:
            return random.uniform(0.7, 0.9) * float(Adopter.get_score(self, adoption_center))
        if 3 <= distance < 5:
            return random.uniform(0.5, 0.7) * float(Adopter.get_score(self, adoption_center))
        if distance >= 5:
            return random.uniform(0.1, 0.5) * float(Adopter.get_score(self, adoption_center))
        if self.desired_species not in adoption_center.get_species_count():
            return 0.0


##Part 3: Connecting Adopters and Adoption Centers

def get_ordered_adoption_center_list(adopter, list_of_adoption_centers):
    """
    The method returns a list of an organized adoption_center such that the scores for each AdoptionCenter to the Adopter will be ordered from highest score to lowest score.
    """
    
    def get_score_key(x):
        return adopter.get_score(x)

    def get_name_key(x):
        return x.get_name()

    s = sorted(list_of_adoption_centers, key=get_name_key)
    return sorted(s, key=get_score_key, reverse=True)

def get_adopters_for_advertisement(adoption_center, list_of_adopters, n):
    """
    The function returns a list of the top n scoring Adopters from list_of_adopters (in numerical order of score)
    """
    def get_score_key(x):
        return x.get_score(adoption_center)

    def get_name_key(x):
        return x.get_name()

    s1 = sorted(list_of_adopters, key=get_name_key)
    s2 = sorted(s1, key=get_score_key, reverse = True)
    if n > len(s2):
        return s2
    return s2[:n + 1]

