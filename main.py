import copy
import itertools

# Python 2.7
# This program creates an object of game Life (https://en.wikipedia.org/wiki/Conway's_Game_of_Life)
class Life(object):

    empty, rock, fish, shrimp = range(4) # cell forms
    ocean = [[]]

    def __init__(self, ocean):
        self.ocean = copy.deepcopy(ocean)
        self.day = 0
        self.oceanLength = len(self.ocean)
        self.oceanWidth = len(self.ocean[0])

    def count_neighbor_elements(self, i, j, species):
        neighbor_species_set = [(x, y) for x in range(self.oceanLength)
                                for y in range(self.oceanWidth)
                                if ((x != i or y != j) and
                                abs(i - x) <= 1 and abs(j - y) <= 1 and
                                (self.ocean[x][y] == species))]
        return len(neighbor_species_set)

    def renew(self): # next game state
        next_day_ocean = copy.deepcopy(self.ocean)
        for i, j in itertools.product(
                range(self.oceanLength), range(self.oceanWidth)):
            element = self.ocean[i][j]
            if element == self.empty:
                fish_count = self.count_neighbor_elements(i, j, self.fish)
                if fish_count == 3:
                    next_day_ocean[i][j] = self.fish
                else:
                    shrimp_count = self.count_neighbor_elements(
                        i, j, self.shrimp)
                    if shrimp_count == 3:
                        next_day_ocean[i][j] = self.shrimp
            elif element == self.fish or element == self.shrimp:
                element_count = self.count_neighbor_elements(i, j, element)
                if element_count > 3 or element_count < 2:
                    next_day_ocean[i][j] = self.empty
        self.ocean = next_day_ocean
        self.day += 1

    def __str__(self):
        return "\n".join(
            (' '.join((str(el) for el in line))
             for line in self.ocean)
        )

    def calculate_generation(self, day):
        if day > 0:
            for i in range(day):
                self.renew()

my_ocean = []
generation = int(raw_input())
dimensions = raw_input().split(' ')
length = int(dimensions[0])
width = int(dimensions[1])
for index in range(length):
    my_ocean.append([])
    elements = raw_input().split(' ')
    my_ocean[index] = [int(element) for element in elements]
new_life = Life(my_ocean)
new_life.calculate_generation(generation)
print new_life
