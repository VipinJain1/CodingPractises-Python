# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 09:25:47 2021

@author: VIP
"""

/* Write your T-SQL query statement below */

select d.dept_name, isnull(count(s.student_id),0) as student_number 
from 
    Department d left join Student s  
on 
    d.dept_id = s.dept_id 
group by 
    d.dept_name
order by 
    student_number desc, d.dept_name  
