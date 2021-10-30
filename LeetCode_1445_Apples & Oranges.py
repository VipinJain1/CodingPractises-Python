# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 08:27:19 2021

@author: VIP
"""

# Write your MySQL query statement below

#select sale_date, SUM(IF (fruit ='apples', sold_num, -sold_num)) as diff from sales group by sale_date

select sale_date , SUM(CASE when fruit='apples' then sold_num else -sold_num end) as diff from Sales group by sale_date

#select t1.sale_date, (t1.sold_num - t2.sold_num) as diff 
#from Sales t1, Sales t2 
#where
#t1.sale_date = t2.sale_date and 
#t1.fruit = 'apples' and t2.fruit = 'oranges'
#group by t1.sale_date
