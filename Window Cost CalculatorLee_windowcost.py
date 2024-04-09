#-------------------------------------------------------------------------------
# Name:Byung Rog Lee
# Course Name: CS1010
# Class Time: Tuesday, Thursday 9:30A.M. - 10:45A.M.
# Program Assignment Number: CS1010 Program 2
# Program File Name: Lee_window_cost.py
# Due Date: 02/12/2023
# Purpose: Writing a program that helps a local builder to calculate the total cost of a new window
#
# Author:      holyr
#
# Created:     12-02-2023
# Copyright:   (c) holyr 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

#Initialization Section (Symbolic Constants)
price_of_glass = 5.50
price_of_framing = 8.60
tax_rate = 0.055
labor_rate = 11.25


#Input Section
height = float(input('Enter window height:'))
width = float(input('Enter window width:'))


#Calculation Section
glass_area = height * width
cost_of_glass = glass_area * price_of_glass
framing = 2 * (height + width)
cost_of_framing = framing * price_of_framing
sales_tax = tax_rate * (cost_of_glass + cost_of_framing)
labor_cost = labor_rate * glass_area
total_cost = cost_of_glass + cost_of_framing + sales_tax + labor_cost


#Output Section
print('Enter window height:', height)
print('Enter window width:', width)
print('-----------------------------------------------------------------')
print('                     Window Cost Calculator                      ')
print('-----------------------------------------------------------------')
print('Glass Area                                                ', f'{glass_area:.2f}')
print('Linear Framing                                            ', f'{framing:.2f}')
print('Cost Of Glass                                           $ ',    f'{cost_of_glass:.2f}')
print('Cost of Framing                                         $',  f'{cost_of_framing:.2f}')
print('Sales Tax                                               $ ',         f'{sales_tax:.2f}')
print('Cost Of Labor                                           $',       f'{labor_cost:.2f}')
print('-----------------------------------------------------------------')
print('Total Cost                                              $',        f'{total_cost:.2f}')
