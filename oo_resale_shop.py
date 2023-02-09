"""
   Filename: oo_resale_shop.py
Description: the file that contains the methods/class for looking at the inventory of the shop, as well as editing it (by buying/selling computers within the store).
     Author: Nalini Oliver
     Collaborators: CS TA Hours, Prof. Crouser's OneCard Python example, and Prof Crouser's procedural_resale_shop.py code/ main() code. 
       Date: 8 February 2023
"""
from computer import * 

class ResaleShop:

    ''' These are the attributes for the resale shop. The only attribute included is an empty inventory list. '''
    inventory = []

    
    '''' The only constructor we have is based on the attribute "inventory". In this case, it is equivalent to an empty list. ''' 
    def __init__(self) -> None:
        self.inventory = []
        pass # You'll remove this when you fill out your constructor

    
    ''' This method will buy a new computer, meaning it will add it to the inventory list.'''
    def buy(self, object1) -> None:
       self.inventory.append(object1)
    
    '''This method will print the inventory list (and therefore reflect changes when we buy/sell computeres, and therefore "add" or "remove" them from the inventory). This function is adapted from Prof. Crouser's inventory print function in the procedural resale shop.''' 
    def printinventory(self):
        if self.inventory:
        # For each item
            for self.description in self.inventory:
            # Print its details
                print(self.description)
        else:
            print("No inventory to display.")
        
    ''' This method will "sell" and therefore remove computers from the inventory list.''' 
    def sellcomputer(self, object2) -> None:
       self.inventory.remove(object2)
    
    ''' This is an example of what you would type to use the following methods that I have written above. This includes "naming" the store based on the class name, and using this store to edit the inventory.''' 
def main():
    mystore = ResaleShop()
    print("Welcome to Nalini's computer shop!")
    computerA = Computer("Macbook Air 2022", "M1 Processor", 55.7, 22, "Mac OS Mojave", 2021, 200)
    mystore.buy(computerA)
    computerB = Computer("Macbook Pro 2012", "Intel Processor", 55.7, 22, "Mac OS Puma", 2012, 50)
    mystore.buy(computerB)
    print("We just bought two new computers! here is our inventory")
    mystore.printinventory()
    mystore.sellcomputer(computerA)
    print("We just sold one computer. Now, here is our inventory")
    mystore.printinventory()

main()






    



