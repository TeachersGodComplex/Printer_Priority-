# Imports

# Global variables
from ssl import Options
from tracemalloc import start
from unicodedata import name


printers = []
EOL = "\n"

# Class

class Printer:
    def __init__(self, name, time="") -> None:
        self.name = name
        self.time = time
        self.status = False #True if printer, else False
        self.maker = ""
    
        def __str__(self) -> str:
            return f"Det som ska printas när vi printar objektet."

    def name(self):
        return self.name

    def start(self):
        return self.time

    def check_status(self):
        status = ""
        status = "is printing" if self.status else "is free"
        # Detta visas när man "loggar in" 
        # Om printern används ser man vem som printar, när den startades samt hur lång tid det kommer ta
        print(f"{self.name} {status}\nPrinting:{self.maker}\nTime:{self.time}")
    
    def new_print(self):
        print("")
        print(f"Adding new print to {self.name}") # Self.name = namn på vald printer
        self.maker = input("Who is printing: ") # name == next_in_line???
        self.start = input("Enter printing time: ") # Kan man skriva in detta i listan 
        print("Your name is automatically moved from the waitinglist")
        menu()
       # next_in_waiting()
    
   # def done_printing(self):
       # print("")
       # print(f"{self.maker} are done printing") 
       # print(f"{self.name} is now free to use") 

# Functions

def options():
    print("(1) See waitinglist")
    print("(2) Add name to waitinglist")
    print("(3) Chose printer to use")
    # print("(4) Done printing")

def view(): 
    lines = []
    with open('waitinglist.txt') as f: 
        lines = f.readlines() # Readline läser upp listan rad för rad
    # Namn i listan numreras 
    count = 0
    for line in lines:
        count += 1
        print(f'{count}: {line}')
    menu()

def add_to_list():
    with open("waitinglist.txt", "a", encoding="utf-8") as waiting_list:
        name = input("Enter name:") # Skriv in ditt namn i listan 
        waiting_list.write(name+"\n")
    menu()

def pick_printer():
    print()
    print("Choose a printer:")
    print("Pick the index you want to use.")
    # Detta ger printrarna ett index vilket gör att vi kan välja mellan dom
    for i, printer in enumerate(printers):
        print(f"{i}, {printer.name}")
    pick = input(">>> ")
    return printers[int(pick)]

# def picked_printer():
   # print("Choose used printer:")
   # print("Pick the index you have used.")
   # for i, printed in enumerate(printers):
    #    print(f"{i}, {printed.name}")
   # pick = input(">>> ")
   # return printers[int(pick)]
    
def menu():
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

    # elif choice == "4":
       # printed = picked_printer()
       # printed.done_printing()
    
    else:
        print("Incorrect input")

def next_in_waiting():
    waiters = []
    with open("waitinglist.txt", "r", encoding="utf-8") as f:
        waiters = f.readlines()
    next_in_line = waiters.pop(0)
    with open("waitinglist.txt", "w", encoding="utf-8") as f:
        for line in waiters:
            f.write(line)

def get_printers():
    print("----Printers----")
    # Visar vilka printers som är lediga Free/Printing
    for printer in printers:
        printer.check_status()
        print()

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
(Input ALWAYS 1-3)
""")

    get_printers()
    menu()
    print()
    
if __name__ == "__main__":
    main()