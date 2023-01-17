
class Animal:

    def __init__(
            self,
            name,
            introduction,
            conservation_status,
            kingdom,
            order,
            phylum,
            class1,
            for_more
    ):
        self.name = name
        self.introduction = introduction
        self.conservation_status = conservation_status
        self.kingdom = kingdom
        self.order = order
        self.phylum = phylum
        self.class1 = class1
        self.for_more = for_more

# __repr__ The method takes a unique parameter self
# from which it can access the attributes of the object.
    def __repr__(self):
        return f'You chose {self.name}, here is some information about {self.name}: ' \
               f'\nIntroduction : {self.introduction} ' \
               f'\nThis animal is defined by the IUCN ' \
               f'Red List of Threatened Species as {self.conservation_status} ' \
               f'\nAnd now some Scientific classification: ' \
               f'\nKingdom: {self.kingdom} ' \
               f'\nOrder: {self.order} ' \
               f'\nPhylum: {self.phylum} ' \
               f'\nClass: {self.class1} ' \
               f'\nTo get more information about {self.name} visit {self.for_more}'
