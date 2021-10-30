# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 10:15:56 2021

@author: VIP
"""


select unique_id , name 
from Employees A LEFT JOIN  EmployeeUNI B 
on A.id = B.id