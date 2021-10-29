# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 15:05:47 2021

@author: VIP
"""

# Write your MySQL query statement below

# Write your MySQL query statement below

select 
employee_id , CASE 
WHEN employee_id %2 =1 and name NOT like '%M%' THEN salary
ELSE 0 
END
as bonus
from Employees 
order by employee_id