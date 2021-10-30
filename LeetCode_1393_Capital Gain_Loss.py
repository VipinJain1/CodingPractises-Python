# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 09:30:22 2021

@author: VIP
"""

# Write your MySQL query statement below

select stock_name, SUM( CASE when operation  ='Buy' then -price else price end) as capital_gain_loss 
from Stocks group by stock_name
