#--- HDR ---#
def ajouter_fruit(panier, fruit):
    if fruit not in panier:
        print("Ce fruit n'est pas sur la liste de courses")
    else :
        panier[fruit] = panier[fruit] + 1
    return panier
#--- HDR ---#

panier_de_fruits = {'pomme' : 2, 'poire' : 3, 'abricot' : 1}

def avalanche_de_fruits(panier):
    pass


# Tests
assert avalanche_de_fruits(panier_de_fruits) == {'pomme' : 3, 'poire' : 4, 'abricot' : 2}