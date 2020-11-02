# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 12:25:06 2020

@author: Dani Ossé
"""
import glassdoor_scraper as gs
import pandas as pd

path = "C:/Users/ossed/MyDSProjects/Quant_salary_prediction/Quant_salary_prediction/chromedriver"
df = gs.get_jobs('quantitative analyst',1000,False,path,15)