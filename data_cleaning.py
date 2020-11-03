# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 12:19:02 2020

@author: Dani Ossé
"""

import pandas as pd 

df = pd.read_csv('glassdoor_quants_jobs.csv')

#salary parsing 

df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'par heure' in x.lower() else 0)
df['hourly'].value_counts()
#df['employer_provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0)

df = df[df['Salary Estimate'] != '-1']
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_Kd = salary.apply(lambda x: x.replace(' k','').replace('$',''))

min_hr = minus_Kd.apply(lambda x: x.lower().replace('par heure','').replace('employer provided salary:',''))

df['min_salary'] = min_hr.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = min_hr.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary+df.max_salary)/2

#Company name text only
df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] <0 else x['Company Name'][:-3], axis = 1)

#correcting values in Location
indices = [69, 91, 108]
location = ['New York, NY','Maryland, MD','Maryland, MD']
for i,j in zip(indices, location):
    df.loc[i,'Location'] = j
#index 69 : New York, NY
#index 91 : Maryland, MD
#index 108 : Maryland, MD
df['Location'] = df['Location'].apply(lambda x: x.replace('Maryland','Maryland, MD'))
df['Location'] = df['Location'].apply(lambda x: x.replace('États-Unis','États-Unis, USA'))

#state field 
df['job_state'] = df['Location'].apply(lambda x: x.split(',')[-1])
df.job_state.value_counts()
df[['company_txt','Job Title']][df['Location']=='États-Unis, USA']

#df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis = 1)

#age of company 
df['age'] = df.Founded.apply(lambda x: x if x <1 else 2020 - x)


#parsing of job description (python, etc.)

#python
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df.python_yn.value_counts() 
#r studio 
df['R_yn'] = df['Job Description'].apply(lambda x: 1 if ' R,' in x or ' R ' in x else 0)
df.R_yn.value_counts()

#spark 
df['spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df.spark.value_counts()

#aws 
df['aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df.aws.value_counts()

#excel
df['excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
df.excel.value_counts()

#mathematics
df['mathematics'] = df['Job Description'].apply(lambda x: 1 if 'mathemati' in x.lower() else 0)
df.mathematics.value_counts()

#finance
df['finance'] = df['Job Description'].apply(lambda x: 1 if 'financ' in x.lower() else 0)
df.finance.value_counts()

#modeling
df['modeling'] = df['Job Description'].apply(lambda x: 1 if 'modeling' in x.lower() else 0)
df.modeling.value_counts()

#statistics
df['statistics'] = df['Job Description'].apply(lambda x: 1 if any(elem in x.lower() for elem in ['statisti','probabili','econometr']) else 0)
df.statistics.value_counts()

#vba
df['vba'] = df['Job Description'].apply(lambda x: 1 if 'vba' in x.lower() else 0)
df.vba.value_counts()

#C++
df['C++'] = df['Job Description'].apply(lambda x: 1 if 'C++' in x else 0)
df['C++'].value_counts()

#portfolio_theory
df['portfolio_theory'] = df['Job Description'].apply(lambda x: 1 if 'portfolio' in x.lower() else 0)
df.portfolio_theory.value_counts()

#derivatives
df['derivatives'] = df['Job Description'].apply(lambda x: 1 if any(elem in x.lower() for elem in ['derivatives','equity','interest rates','exotic']) else 0)
df.derivatives.value_counts()

#trading
df['trading'] = df['Job Description'].apply(lambda x: 1 if 'trading' in x.lower() else 0)
df.trading.value_counts()

#data_science
df['data_science'] = df['Job Description'].apply(lambda x: 1 if any(elem in x.lower() for elem in ['machine learning','deep learning','data science']) else 0)
df.data_science.value_counts()

#trading
df['sql'] = df['Job Description'].apply(lambda x: 1 if 'sql' in x.lower() else 0)
df.sql.value_counts()

df.columns

df_out = df.drop(['Competitors','Headquarters'], axis =1)

df_out.to_csv('salary_data_cleaned.csv',index = False)
