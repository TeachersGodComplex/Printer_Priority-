# Imports

# Global variables
from ssl import Options
from tracemalloc import start
from unicodedata import name


printers = []
EOL = "\n"

# Class

class Printer:
    """
    Class printers innehåller all info om
    Jag använda denna metod för att returna 
    namn (str): 
    tid (int):
    status 
    maker 
    I used this method to return name and printing time. 
    These values are defined when you choose to use a printer. 
    """
    def __init__(self, name, time="") -> None:
        self.name = name
        self.time = time
        self.status = False #True if printer, else False
        self.maker = ""

    def name(self):
        return self.name

    def start(self):
        return self.time

    def check_status(self):
        """
        Statusen visas när man öppnar programet och berättar vilken printer som är ledig/upptagen 
        Om printern används ser man vem som printar och hur lång tid det kommer ta 
        
        self.name anges av indexet man väljer i pick_printer
        self.time/maker anges av användaren i new_print
        """
        status = ""
        status = "is printing" if self.status else "is free"
        print(f"{self.name} {status}\nPrinting:{self.maker}\nTime:{self.time}")
    
    def new_print(self):
        """
        
        """
        print("")
        self.status = True
        print(f"Adding new print to {self.name}") # Self.name = namn på vald printer
        self.maker = input("Who is printing: ") 
        self.time = input("Enter printing time: ") 
        next_in_waiting()
        print("Your name is automatically moved from the waitinglist")
        get_printers()
    

    def done_printing(self):
        """
        Self.name anges i used_printer, functionen tar bort 
        maker och time från skrivarn samt ändrar statusen.
        """
        print()
        print(f"{self.maker} is done printing") 
        print(f"{self.name} is now free to use")
        # Removes self.maker and self.name from get_printers
        self.maker = ""
        self.time = ""
        self.status = False 
        print()
       

# Functions

def options():
    print("(1) See waitinglist")
    print("(2) Add name to waitinglist")
    print("(3) Chose printer to use")
    print("(4) Done printing")
    print("(#) To exit the program.")

def view(): 
    lines = []
    with open('waitinglist.txt') as f: 
        lines = f.readlines() # Readline läser upp listan rad för rad
    # Namn i listan numreras 
    count = 0
    for line in lines:
        count += 1
        print(f'{count}: {line}')


def add_to_list():
    with open("waitinglist.txt", "a", encoding="utf-8") as waiting_list:
        name = input("Enter name:") # Skriv in ditt namn i listan 
        waiting_list.write(name+"\n")
    get_printers()
    

def pick_printer():
    """
    Ger printrarna ett index.
    Valet beslutar vilken printer man vill använda.
    """
    print()
    print("Choose a printer:")
    print("Pick the index you want to use.")
    # Detta ger printrarna ett index vilket gör att vi kan välja mellan dom
    for i, printer in enumerate(printers):
        print(f"{i}, {printer.name}")
    pick = input(">>> ")
    return printers[int(pick)]


def used_printer():
    """
    Samma function som def pick_printer utom texten som printas
    Detta index används dock för att identifiera vilken printer man ska 
    ta bort en print ifrån.
    """
    print()
    print("Choose used printer:")
    print("Pick the index you have used.")
    for i, printer in enumerate(printers):
        print(f"{i}, {printer.name}")
    pick = input(">>> ")
    return printers[int(pick)]


def menu():
    """
    En def kallas på genom if-satsen av ett input som är lika med ett choice.
    Choice definerars av inputet 1-4 eller #
    """
    choice = ""
    while choice != "#":
    # När choice är "#" avsluta programet annars printa menu
    # Genom att sätta menyn i en loop slipper jag kalla på den efter varje def
        print("""----Options----""")
        options()
        choice = input(">>> ")
        if choice == "1":
            view()

        elif choice == "2":
            add_to_list()

        elif choice == "3":
            # Tar vald printer och sätter den som self.name
            # i efterföljande def vet programet under 
            # vilken printer den ska ändra infon och statusen
            printer = pick_printer()
            printer.new_print()

        elif choice == "4":
            printer = used_printer()
            printer.done_printing()

        elif choice == "#":
            # Avslutar loppen och programet
            print("Goodbye!")

        else:
            # Felaktigt input gör att menyn loppas  
            print("Incorrect input")


def next_in_waiting():
    """
    I väntelistan numreras alla namn, functionen plockar bort indexet nr1 
    varje gång någon skriver in ett namn på en av printrarna.
    Nr 1 i väntelistan skriver in sitt namn på en printer 
    och tas samtidigt bort från väntelistan. För att det ska fungera 
    måste folk respektera ordningen på väntelistan.
    """
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

    get_printers()
    menu()
    print()
    
if __name__ == "__main__":
    main()