# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 15:43:36 2021

@author: VIP
"""

SELECT date_id, make_name, COUNT(DISTINCT lead_id) as unique_leads, COUNT(DISTINCT partner_id) as unique_partners
FROM Dailysales
GROUP BY date_id, make_name