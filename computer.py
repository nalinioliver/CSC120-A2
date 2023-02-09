"""
   Filename: computer.py
Description: the file that contains the methods/class for looking at the inventory of the shop, as well as editing it (by buying/selling computers within the store).
     Author: Nalini Oliver
     Collaborators: CS TA Hours, Prof. Crouser's OneCard Python example, and Prof Crouser's procedural_resale_shop.py code/ main() code. 
       Date: 8 February 2023
"""
class Computer:
    
    '''These are the attributes needed to "describe" the computers for this shop. This information will be used later on to refurbish the computer/update the price, and update the operating system.'''
    description: str = ""
    processor_type: str = ""
    hard_drive_capacity: int 
    memory: int 
    operating_system: str = ""
    year_made: int 
    price: int 

    '''These are the constructors that are used in the program, which defines the attributes we have shown above (as adapted from Prof Crouser's OneCard example).'''
    def __init__(self, computer_description, computer_processor, computer_hard_drive, computer_memory, operating_system, computer_age, computer_price) -> None:
        self.description = computer_description
        self.processor_type = computer_processor
        self.hard_drive_capacity = computer_hard_drive
        self.memory = computer_memory
        self.operating_system = operating_system
        self.year_made = computer_age
        self.price = computer_price

    
    '''This method updates a computer's operating system, so that no matter what it comes in with, it will automatically be updated to the newest Mac OS, Mac OS Ventura. This is adapted from the program in Prof. Crouser's procedural program'''
    def updateOS(self, inputOS):
        newOS = "MacOS Ventura"
        if newOS is not None:
            self.operating_system = "MacOS Ventura"
        else:
            print("All operating systems updated!")
    
    '''This method refurbishes the computer (AKA, changes its price) based on its age. These guidelines/program is adapted from the program in Prof. Crouser's procedural re-sale shop.'''
    def refurbish(self, yearmade) -> None:   
        if self.year_made < 2000:
            self.price = 10
        elif self.year_made < 2012:
            self.price = 100
        elif self.year_made < 2018:
            self.price = 550
        else:
            self.price = 1000
    
'''This is an example of what you would type to use the following methods that I have written above. This includes refurbishing the computer, checking its age, etc.'''
def main():
    computerA = Computer("Macbook Air 2022", "M1 Processor", 55.7, 22, "Mac OS Mojave", 2021, 200)
    print(computerA)
    print("New computer added to inventory, has a description of", computerA.description, "a price of", computerA.price, "and was made in", computerA.year_made)
    print("The operating system for this computer is", computerA.operating_system)
    print("Updating the computer OS...")
    computerA.updateOS(computerA.operating_system)
    print("The new operating system is", computerA.operating_system)
    print("The current price of the computer is", computerA.price, "and the current age of the computer is", computerA.year_made)
    computerA.refurbish(computerA.year_made)
    print("The new price of the computer based on its age is", computerA.price)


main() 
        

    
    
    
