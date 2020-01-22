import os
import sys, time

def TicketsCalculation():
    print("How many tickets do you have?")
    num_tickets = int(input())

    if num_tickets < 4:
        print("We are able to proceed")
    else:
        print("We are unable to insure customers with more than 3 tickets")
        print("Thank you for your time")
        time.sleep(5)
        os._exit(1)

    return num_tickets

def AccidentsCalculation():
    print("How many accidents do you have?")
    num_accidents = int(input())

    if num_accidents < 4:
        print("We are able to proceed")
    else:
        print("We are unable to insure customers with more than 3 accidents")
        print("Thank you for your time")
        time.sleep(5)
        os._exit(1)

    return num_accidents

def AddingPoints():
    num_tickets = TicketsCalculation()
    num_accidents = AccidentsCalculation()

    #total_points = int(num_tickets) + int(num_accidents)
    #print(f'We can insure you because you only have {total_points} points.')
    
    print(f'We can insure you because you only have {int(num_tickets) + int(num_accidents)} points.')

print("Hello, and welcome to Eri's car insurance app!")

AddingPoints()
