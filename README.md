# Printer_Priority
A log program for the printers. A person will be able to see if any printers are free or add themself on a waitinglist. 


## Why should I use this project 
In order to effectively use the printors I'm creating a program to log everything. With a waitinglist and all the information at hand more people will find time to use the printers. It also makes it easy to trace back errors or broken parts to one person.


### Setup
As of now everything takes place in the terminal


## 30/3 
### Startup
Planing out what functions I wanted and how things are gonna be displayed 


## 6/4 
### Class Printer:
I made a class for the printers. Here all the info about them and the person printing can be found.

### check_status 
When logging in following printers will get a status check to see wich ones are being used. 

### def__init__(self)
I used this method to return name and printing time. These values are defined when you choose to use a printer. 


## 20/4
I changed the menu and now there are 3 options and three def functions. A function is called on through the if-statement by an input. The input is defined as a choice.

### Displayed in cod:  
choice = input(">>> ") 


def pick_printer hur den fungerar mm.

## 27/4 
def next_in_waiting takes away the 0 index value from the waitinglist (Index 0 = First name on list) everytime someone adds there name to a printer. This function makes the program a lot more automatic and calls for less steps when using the printers.  