#=====creating terminal text options===========
# obtained from https://gist.github.com/rene-d/9e584a7dd2935d0f461904b9f2950007
BLACK = "\033[0;30m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BROWN = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
YELLOW = "\033[1;33m"
BOLD = "\033[1m"
FAINT = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
END = "\033[0m"


#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity,counter):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        self.counter = counter


    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return f"""——————————————————————————————{self.counter}————————————————————————————————————————————
{CYAN}Product:        {self.product}
Product code:   {self.code}
Country:        {self.country}
Cost:           R{self.cost}
Quantity:       {self.quantity}{END}"""
        



#=============Shoe list===========
shoe_list = []

#==========Functions outside the class==============
def read_shoes_data():
    
    line_count = 0
    inv = open('inventory.txt','r')
    inv.seek(0)
    counter = 1
    try:
        for line in inv:
            if line_count > 0:
                line = line.strip('\n')
                data = line.split(',')
                listed_obj = Shoe(data[0],data[1],data[2],data[3],data[4],counter)
                shoe_list.append(listed_obj)
                counter += 1
                
            line_count += 1    
        inv.close()
    except ValueError or FileNotFoundError:
        print('Error - file could not be read/ found')
        inv.close()
    
    return(shoe_list)


def capture_shoes():
    
    new_textline = ''

    #obtain user inputs
    while True:
        try:
            new_country = str(input('What country is the shoe from? '))
            break 
        except ValueError:
            print(F'{RED}Invalid input. Try entering a name.{END}')
    while True:
        try:
            new_code = str(input('What is the shoes product code? '))
            break 
        except ValueError:
            print(F'{RED}Invalid input. Try entering a name.{END}')
    while True:
        try:
            new_product = str(input('What is the name of the shoe? '))
            break 
        except ValueError:
            print(F'{RED}Invalid input. Try entering a name.{END}')
    while True:
        try:
            new_cost = int(input('How much does the shoe cost? '))
            break 
        except ValueError:
            print(f'{RED}Invalid input. Try entering a number.{END}')
    while True:
        try:
            new_quantity = int(input('How many pairs of shoes do we have? '))
            break 
        except ValueError:
            print(f'{RED}Invalid input. Try entering a number.{END}')

    #add the new shoe to the shoe inventory text file
    inv = open('inventory.txt','a')
    new_textline = (f'\n{new_country},{new_code},{new_product},{new_cost},{new_quantity}')
    inv.write(new_textline)
    inv.close()

    #re-read the newly updated text file to update shoe_list for the new shoe product
    print(f'——————————————————————————————————————————————————————————————————————————\n{GREEN}New shoe product successfully added.{END}')


#This function reads the shoe data, and prints out each object in accordance with the __str__ self function of the class
def view_all():
    read_shoes_data()
    for obj in shoe_list:
        print(obj)
    print('——————————————————————————————————————————————————————————————————————————')

#identify the shoes with the lowest stock and inform the user which product that is, and the stock remaining
def re_stock():
    lowest_stock = 100000
    shoe_to_stock = ''
    for obj in shoe_list:       
        if int(obj.quantity) < lowest_stock:
           lowest_stock = int(obj.quantity)
           shoe_to_stock = obj.product
           
    print(f'——————————————————————————————————————————————————————————————————————————\n{YELLOW}The shoes that have the lowest stock are {shoe_to_stock}. The stock remaining is {lowest_stock}.{END}')
    
    
    #request the user inputs the amount of stock to re-stock with. Update the quantity object in the shoe_list to add the input number by the user. 
    while True:        
        try:            
            num_add = int(input('Enter the number of pairs you wish to add or enter -1 to return to the menu: '))
            if num_add == -1:
                break
            elif num_add < -1:
                print(f'{RED}Please enter a positive integer.{END}')
            else:
                for obj in shoe_list:
                    if obj.product == shoe_to_stock:
                        new_num = int(obj.quantity)+num_add
                        obj.quantity = new_num
                break        
     
        except ValueError:
            print(F'{RED}Invalid input - try again.{END}')  
    
    
    #rewrite shoe_list to the text doc
    rewrite_list()
    read_shoes_data()
    print(f'——————————————————————————————————————————————————————————————————————————\n{GREEN}Shoe successfully restocked!{END}\n——————————————————————————————————————————————————————————————————————————')
    


#based on the user input, print an object if the code is = to what the user input
def search_shoe(x):   
    for obj in shoe_list:
        if obj.code == x:
            print(obj)

#this basically only prints the product name and the value. This is then formatted according to the length of the product name
def value_per_item():
    print('——————————————————————————————————————————————————————————————————————————')
    for obj in shoe_list:
        value = int(obj.quantity) * int(obj.cost)

        if len(obj.product) <= 6:
            print(f'''{GREEN}{obj.product}:{END}        \t\tR{value}''')

        elif len(obj.product) <= 13 and len(obj.product) >  6:
            print(f'''{GREEN}{obj.product}:{END}        \tR{value}''')

        elif len(obj.product) <= 14 and len(obj.product) >  13:
            print(f'''{GREEN}{obj.product}:{END}         R{value}''')

        elif len(obj.product) <= 18 and len(obj.product) >  14:
            print(f'''{GREEN}{obj.product}:{END}        R{value}''')

        else:
            print(f'''{GREEN}{obj.product}:{END}    R{value}''')


#identify the highest stock by comparing all qty's for each shoe and updating a variable with the highest q if found. Once found, print message to user
def highest_qty():
    highest_stock = 0
    sale_shoe = ''
    for obj in shoe_list:       
        if int(obj.quantity) > highest_stock:
           highest_stock = int(obj.quantity)
           sale_shoe = obj.product
           
    print(f'——————————————————————————————————————————————————————————————————————————\n{GREEN}The shoes that have the highest stock are {sale_shoe}. \nThese shoes are now on sale with stock remaining of {highest_stock}.{END}')
    


#this is a uniquely used function, which is only called on if the text file needs to be updated with new info once shoe_list has been updated.
def rewrite_list():
    new_data = 'Country,Code,Product,Cost,Quantity'
    
    for obj in shoe_list:
      new_data += f'\n{obj.country},{obj.code},{obj.product},{obj.cost},{obj.quantity}'
    
    shoe_file = open('inventory.txt', 'w')
    shoe_file.write(new_data)
    shoe_file.close()




#==========Main Menu=============

#read the data in the text file then run the menu loop
read_shoes_data()


while True:
    menu = int(input(f'''——————————————————————————————————————————————————————————————————————————{PURPLE}
Please select an option below:
    1) View all shoes
    2) Add a new shoe type to the inventory (Capture a new item)
    3) Re_stock the shoes with the current lowest stock
    4) Search for a type of shoe
    5) View the total stock value for each shoe type
    6) Put the shoes with the highest stock on sale
    7) Exit{END}
——————————————————————————————————————————————————————————————————————————
'''))

    if menu == 1:   
        shoe_list = []
        view_all()

    elif menu == 2:
        capture_shoes()
        

    elif menu == 3:
        re_stock()

    elif menu == 4:
        search_shoe(x = input('Please enter the code of the shoe you wish to view: '))

    elif menu == 5:
        value_per_item()

    elif menu == 6:
        highest_qty()

    elif menu == 7:
        print(f'{RED}Program terminated.{END}')
        break

        
        
        

