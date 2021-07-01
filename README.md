# CodingPractises
Just Refresh Your skills Vipin... 


Minimum time difference
April 11, 2021 by Sumit Jain
Minimum time difference

Given a list of 24-hour clock time points in “HH:MM” format. Write a program to find the minimum minutes difference between any two time-points in the list.

Example: 

Given hours: [00:00, 03:00, 22:30]
minimum time difference: 90

Given hours: [01:59, 03:00, 21:50, 22:30]
minimum time difference: 40
Solution:

Convert all the given times to minutes and have these stored in a list.
Now sort the minutes list in ascending order.
Now get the difference between every consecutive time and keep track of the minimum.
To cover the edge case when one time is before and after the 24:00 hours, in that case add 1440 (there are 1440 minutes in 24 hours ) to time which is before 24:00. For example if the first time is 1:00 and the second time is 23:30. So minutes are 60 and 1410 respectively. Now add 1440 to 60 which becomes 1500. Now the difference is 1500-1410 = 90 mins. 
Return the minimum difference.
See the code below for more understanding.
