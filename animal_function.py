from raccoon import raccoon
from alpaca import alpaca
from eastern_newt import eastern_newt
from honey_bee import honey_bee
from japanese_sawshark import japanese_sawshark
from red_footed_booby import red_footed_booby
from pogona import pogona
from emperor_penguin import emperor_penguin
from red_lionfish import red_lionfish
from king_cobra import king_cobra
from leaf_green_tree_frog import leaf_green_tree_frog
from diploria import diploria

mammal_list = ['raccoon', 'alpaca']
fish_list = ['japanese_sawshark', 'red_lionfish']
reptile_list = ['pogona', 'king_cobra']
bird_list = ['emperor_penguin', 'red_footed_booby']
invertebrate_list = ['honey_bee', 'diploria']
amphibian_list = ['eastern_newt', 'leaf_green_tree_frog']


def get_the_thing(a: str):
    if a.lower() == 'alpaca':
        a = alpaca
    elif a.lower() == 'raccoon':
        a = raccoon
    elif a.lower() == 'honey_bee':
        a = honey_bee
    elif a.lower() == 'emperor_penguin':
        a = emperor_penguin
    elif a.lower() == 'eastern_newt':
        a = eastern_newt
    elif a.lower() == 'red_footed_booby':
        a = red_footed_booby
    elif a.lower() == 'japanese_sawshark':
        a = japanese_sawshark
    elif a.lower() == 'red_lionfish':
        a = red_lionfish
    elif a.lower() == 'pogona':
        a = pogona
    elif a.lower() == 'king_cobra':
        a = king_cobra
    elif a.lower() == 'diploria':
        a = diploria
    elif a.lower() == 'leaf_green_tree_frog':
        a = leaf_green_tree_frog
    return a


def get_subclass_info(b):
    if b.lower() == 'fish':
        b = fish_list
    elif b.lower() == 'mammal':
        b = mammal_list
    elif b.lower() == 'bird':
        b = bird_list
    elif b.lower() == 'reptile':
        b = reptile_list
    elif b.lower() == 'amphibian':
        b = amphibian_list
    elif b.lower() == 'invertebrate':
        b = invertebrate_list
    return b
