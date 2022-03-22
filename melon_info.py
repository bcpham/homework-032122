"""Print out all the melons in our inventory."""


#from melons import melon_names, melon_prices, melon_seedlessness 


# def print_melon(name, price, seedless):
#     """Print each melon with corresponding attribute information."""

#     have_or_have_not = 'have'
#     if seedless:
#         have_or_have_not = 'do not have'

#     print(f'{name}s {have_or_have_not} seeds and are ${price}')


# for i in melon_names:
#     print_melon(melon_names[i], melon_prices[i], melon_seedlessness[i])

from melons import melons_informat

def print_melons(melons):

    for melon, infos in melons_informat.items():
        print(melon.upper()) 

        for info, value in infos.items():
            print(f'{info}:{value}')
            
        #this was when I attempted to work with lists...
        #if melon_informat[melon] == melon_name:
            #print(melon_name)

print_melons("melons")
