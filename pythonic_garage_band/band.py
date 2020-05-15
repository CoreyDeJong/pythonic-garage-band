## band will be a collection of musicians

class Musicians():
    memberlist=[]
    def __init__(self,name):
        self.name = name 
        Guitarist.memberlist.append(self)
         
class Guitarist(Musicians):
    def __init__(self, name):
        # super().__init__(name)
        self.name = name

    def get_instrument(self):
        return "guitar"

    def play_solo(self):
        return "groovy"
    
class Bassist(Musicians):
    def __init__(self, name):
        super().__init__(name)
        self.name = name

    def get_instrument(self):
        return "Bass"

    def play_solo(self):
        return "subtle"

class Drummer(Musicians):
    def __init__(self, name):
        super().__init__(name)
        self.name = name

    def get_instrument(self):
        return "guitar"

    def play_solo(self):
        return "softly"

class Band():
    def __init__(self, name):
        self.name = name
        # self.members = members
    

        Musicians.memberlist

    ## go through the memberlist and play the solo in the same order as the memberlist
    def play_solos(self, memberlist):
        for self in memberlist:
            return (self.play_solo)
        

if __name__ == "__main__":
    pass
    # Radiohead = Band("Radiohead")
    # print(Radiohead.name)

    # Jonny = Guitarist("Jonny")
    # print(Jonny.name)
    # print(Jonny.get_instrument())
    # print(Jonny.play_solo())

    # Colin = Bassist("Colin")
    # print(Colin.name)
    # print(Colin.get_instrument())
    # print(Colin.play_solo())

    # Phillip = Drummer("Phillip")
    # print(Phillip.name)
    # print(Phillip.get_instrument())
    # print(Phillip.play_solo())