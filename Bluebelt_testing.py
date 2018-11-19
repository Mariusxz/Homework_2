#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 22:08:55 2018

@author: MariusD
"""

from Bluebelt import checkout_blue_belt

def test_checkout_multiple_insurance():
    multiple_insurance = ["Guitar", "Insurance", "Insurance"]
    
    assert checkout_blue_belt(multiple_insurance)== 1005

def test_checkout_multiple_Priority_Mail():
    multiple_priority = ["Guitar", "Priority mail", "Priority mail"]
    
    assert checkout_blue_belt(multiple_priority)==1010