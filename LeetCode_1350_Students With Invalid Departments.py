# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 10:19:23 2021

@author: VIP
"""

# Write your MySQL query statement below

select id, name 
from Students  where department_id  not in (select id  from  Departments )
