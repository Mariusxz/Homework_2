#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 22:08:26 2018

@author: MariusD
"""

#%%
        
product_list = {
        "Guitar": 1000, 
        "Pick box": 5, 
        "Guitar string": 10, 
        "Insurance": 5, 
        "Priority mail": 10
        }   

my_shopping_cart = ["Guitar", "Insurance", "Insurance", "Priority mail", "Priority mail", "Pick box", "Guitar string"]

def checkout_blue_belt(my_shopping_cart): 
    
    price = 0 
    indexes_insurance = [i for i, x in enumerate(my_shopping_cart) if x == "Insurance"]
    indexes_priority = [b for b, y in enumerate(my_shopping_cart) if y == "Priority mail"]
    
    if len(indexes_insurance) > 0: 
        price += (product_list["Insurance"])
    if len(indexes_priority) > 0: 
        price += (product_list["Priority mail"])     
    if my_shopping_cart == []:
        return "Please select an item!" 
    
    else:
        for item in my_shopping_cart: 
            if item == "Insurance":
                continue
            elif item == "Priority mail": 
                continue
            else: 
                price += (product_list[item])
    
    return price

#%%