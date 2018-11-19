#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 21:40:06 2018

@author: MariusD
"""

from Whitebelt import checkout

def test_checkout_full_order():
    full_order = ["Guitar", "Pick box", "Guitar Strings"]
    
    assert checkout(full_order)== 1015
    
def test_checkout_white_some_items():
    some_items_order = ["Guitar", "Pick box"]
    
    assert checkout(some_items_order)== 1005

def test_empty_cart():
    empty_cart = []
    
    assert checkout(empty_cart)== "Please select an item!"