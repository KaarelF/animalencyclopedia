from time import sleep
from animal_function import get_the_thing
from animal_function import get_subclass_info

go_again = 'yes'
encyclopedia_list = [
    'alpaca',
    'raccoon',
    'honey_bee',
    'emperor_penguin',
    'eastern_newt',
    'pogona',
    'red_footed_booby',
    'japanese_sawshark',
    'diploria',
    'king_cobra',
    'red_lionfish',
    'leaf_green_tree_frog'
]
subclasses_list = [
    'mammal',
    'fish',
    'bird',
    'reptile',
    'amphibian',
    'invertebrate'
]
print('Hello to the wonderful world of animals')
sleep(1)
while go_again.lower() == 'yes':
    print('First, would you choose a subclass of animals '
          'from where you would pick the one you are looking for?')
    get_first_answer = input('Yes or No : ')
    while get_first_answer.lower() != 'no' and get_first_answer.lower() != 'yes':
        print('I am sorry, I did no understand that')
        get_first_answer = input('Yes or No : ')
    if get_first_answer.lower() == 'no':
        print('Would you like to see the list of animals '
              'we have available, or pick an animal for information?')
        sleep(1)
        print('For the first choice write: List')
        sleep(1)
        print('For the second choice write: Pick ')
        get_choice = input('You chose: ')
        sleep(1)
        while get_choice.lower() != 'list' and get_choice.lower() != 'pick':
            print('I am sorry, that choice was invalid')
            get_choice = input('Choose: ')
            sleep(1)

        if get_choice.lower() == 'list':
            print('Here is the list of all available animals:')
            print(*encyclopedia_list, sep='\n')
            get_info = input('Pick an animal from the list: ')
            while get_info.lower() not in encyclopedia_list:
                print('Sorry we do not have this animal in our encyclopedia')
                get_info = input('Pick an animal from the list: ')

            print(get_the_thing(get_info))

        else:
            get_info = input('Pick an animal from the list: ')
            # TODO: You can see that this code block is repeated.
            #  Think of the way how you could leave just one block of this code for all conditions
            while get_info.lower() not in encyclopedia_list:
                print('Sorry we do not have this animal in our encyclopedia')
                get_info = input('Pick an animal from the list: ')

            print(get_the_thing(get_info))

    else:
        print('Here is the list of all available subclasses:')
        print(*subclasses_list, sep='\n')
        get_subclass = input('Pick a subclass from the list: ')
        while get_subclass.lower() not in subclasses_list:
            print('Sorry we do not have this class in our encyclopedia')
            get_subclass = input('Pick a subclass from the list: ')

        print(f'You have chosen the {get_subclass.lower()} subclass. '
              f'And here are the all the animals to choose from: ')
        get_subclass_info(get_subclass)
        print(*get_subclass_info(get_subclass), sep='\n')

        get_subanimal = input('Pick an animal from the list: ')
        while get_subanimal.lower() not in get_subclass_info(get_subclass):
            print('Sorry we do not have this animal in this subclass')
            get_subanimal = input('Pick an animal from the list: ')

        print(get_the_thing(get_subanimal))

    go_again = input('Are you interested in looking up something else? yes/no: ')
    while go_again.lower() != 'no' and go_again.lower() != 'yes':
        print('I am sorry, I did no understand that')
        go_again = input('Are you interested in looking up something else? yes/no: ')
    if go_again.lower() == 'no':
        sleep(1)
        print('Hope do see you again, until next time, goodbye!!!')
        print()
        exit()
