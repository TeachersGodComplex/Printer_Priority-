# Imports

# Global variables
from tracemalloc import start
from unicodedata import name


printers = []
EOL = "\n"

# Classes

class Printer:
    def __init__(self, name, time="", start="") -> None:
        self.name = name
        self.time = time
        self.start= start
        self.status = False #True if printer, else False 
    
    def __str__(self) -> str:
        return f"Det som ska printas när vi printar objektet."

    def name(self):
        return self.name

    def time(self):
        return self.time

    def start(self):
        return self.start

    def check_status(self):
        status = ""
        status = "is printing" if self.status else "is free"
        print(f"{self.name} {status}\nPrinting time:{self.time}\nStarted:{self.start}")


# Functions

def menu():
     
    print("""
Press '1' to se waitinglist
Press '2' to add your name to waitinglist

If your turn, write free printers name 
and file out required info
""")
    get_printers()

    while True: 
        choice = input(">>>")
        if (choice == "1"):
                view()

        elif (choice == "2"):
                add_to_list()
        
        elif (choice == "Tomda"):
                print_info()
        
        elif (choice == "Nemy"):
                print_info()
                
        else:
            print("Incorrect input")
                        

def print_info(self):
        choice = "Tomda"
        print("Please enter:")
        self.name = input("Enter name: ")
        self.start = input("Enter printing time: ")
        self.time = input("Enter current time: ")

        choice = "Nemy"
        print("Please enter:")
        self.name = input("Name: ")
        self.start = input("Printing time: ")
        self.time = input("Current time: ")

def get_printers():
    print("----Printers----")
    for printer in printers:
        printer.check_status()
        print()


def view():
    my_file = open("waitinglist.txt", "r")
    content_list = my_file.readlines()
    print(content_list)
    


def add_to_list(self):
    list = ['waitinglist.txt']
    input("Enter name:")
    list.append(input)
    
    print(list)
    
    file = open('waitinglist.txt', "rt")
    childName = input("Enter your name:")
    print("----- Waitinglist -----")
    print("Name: " + file, end="")
    
    counter = 0
    while True:
        counter += 1
        name = file.readline()
        if (name == ""):
            break
        print("Name " + str(counter) + ": " + name, end="")
    return self.add



def main():
    #global printers

    
    printers.append(Printer("Tomda"))
    printers.append(Printer("Nemy"))
    print("Printers has been initialized.")
    print("Following printers are currently online.")
    for printer in printers:
        print(printer.name)

    menu()
    

if __name__ == "__main__":
    main()