#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 21:39:50 2018

@author: MariusD
"""

#%%
            
available_products={"Guitar":"1000",
                    "Pick box":"5",
                    "Guitar Strings":"10"}

def checkout(cart):
    cost=0
    if cart==[]:
        return "Please select an item!"
    else:
        for product in cart:
            cost+=int(available_products[product])
        return cost

#%%