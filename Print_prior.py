# Imports

# Global variables
from ssl import Options
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
        self.maker = ""
    
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
        print(f"{self.name} {status}\ntime:{self.time}\nStarted:{self.start}\nPrinting:{self.maker}")
    
    def new_print(self):
        print(f"Adding new print to {self.name}") # Vad vill du ska stå här?
        self.start = input("Enter printing time: ")
        self.time = input("Enter current time: ")
        self.maker = input("Who is printing: ")
        self.status = True

# Functions

def options():
    print("(1) See waitinglist")
    print("(2) Add name to waitinglist")
    print("(3) Chose printer to use")

def view():
    my_file = open("waitinglist.txt", "r")
    content_list = my_file.readlines()
    print(content_list)
    
def add_to_list():
    list = ['waitinglist.txt']
    name = input("Enter name:")
    list.append(input)
    print(list.name)

def menu():
    while True:
        print("""----Options----""")
        options()
        choice = input(">>> ")
        if choice == "1":
            view()

        elif choice == "2":
            add_to_list()

        elif choice == "3":
            printer = pick_printer()
            printer.new_print()
     
        else:
            print("Incorrect input")


def get_printers():
    print("----Printers----")
    for printer in printers:
        printer.check_status()
        print()

def pick_printer():
    print()
    print("Choose a printer:")
    print("Pick the index you want to use.")
    for i, printer in enumerate(printers):
        print(f"{i}, {printer.name}")
    pick = input(">>> ")
    return printers[int(pick)]

def main():
    #global printers
    nemy = Printer("Nemy")
    tomda = Printer("Tomda")
    printers.append(nemy)
    printers.append(tomda)
    print("Loading Printers...")
    print("Following printers are online:")
    for printer in printers:
        print(printer.name)

    print("""
If your turn, choose printer 
and fill in required info
(Input is ALWAYS 1-4)
""")

    get_printers()
    menu()
    
if __name__ == "__main__":
    main()