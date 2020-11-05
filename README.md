# Quantitative Analyst Salary Prediction : Project Overview
**I would like to say that the realization of this project was 100 percent inspired by Project Walk-Through taught by Youtuber and data scientist Ken Jee on his Youtube channel. However, although they are similar, I wrote all the different scripts and notebook myself, since Ken Jee predicts the salary of a data scientist, and I predict the salary of a quant. So I learned a lot and faced many problems that were not presented in Ken Jee's class, which I overcame.**
* Created a tool that estimates quant salaries (MAE ~ $ 33K) to have an idea of quantitative analyst salary in USA.
* Scraped over 1000 job descriptions from glassdoor using python and selenium
* Engineered features from the text of each job description to quantify the value companies put on python, excel, aws, spark, finance, mathematics, statistics, C++, modeling and many more 
* Support Vector Regression, Decision Tree, and Random Forest Regressors using GridsearchCV to reach the best model. 
* Built a client facing API using flask

## Code and Resources Used 
**Python Version:** 3.7  
**Packages:** pandas, numpy, sklearn, matplotlib, seaborn, selenium, flask, json, pickle  
**For Web Framework Requirements:**  ```pip install -r requirements.txt```  
**Scraper Github:** https://github.com/arapfaik/scraping-glassdoor-selenium  
**Scraper Article:** https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905  
**Flask Productionization:** https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2
**Ken Jee project of data scientist salary prediction and youtube channel:** https://github.com/PlayingNumbers/ds_salary_proj
https://www.youtube.com/playlist?list=PL2zq7klxX5ASFejJj80ob9ZAnBHdz5O1t

## Web Scraping
Tweaked the web scraper github repo (above) to scrape 1000 job postings from glassdoor.com. With each job, I got the following:
*	Job title
*	Salary Estimate
*	Job Description
*	Rating
*	Company 
*	Location
*	Company Size
*	Company Founded Date
*	Type of Ownership 
*	Industry
*	Sector
*	Revenue

## Data Cleaning
After scraping the data, I had to clean it up so that it would be usable for our model. I made the following changes and created the following variables:

*	Parsed numeric data out of salary 
*	Made columns for employer provided salary and hourly wages 
*	Removed rows without salary 
*	Parsed rating out of company text 
*	Made a new column for company state  
*	Transformed founded date into age of company 
*	Made columns for if different skills were listed in the job description:
    * Python  
    * R  
    * Excel  
    * AWS  
    * Spark
    * Mathematics
    * Finance
    * Modeling
    * C++
    * Portfolio_theory
    * Derivatives
    * Trading
    * sql
*	      Column for simplified job title and Seniority 
*	      Column for description length

## EDA
I looked at the distributions of the data and the value counts for the various categorical variables. Below are a few highlights from the pivot tables. 

![alt text](https://github.com/Daniel11OSSE/Quant_Salary_pred/blob/master/different_quant_salary.PNG "Salary by Position")
![alt text](https://github.com/Daniel11OSSE/Quant_Salary_pred/blob/master/salary_by_state.png "Job Opportunities by State")
![alt text](https://github.com/Daniel11OSSE/Quant_Salary_pred/blob/master/correlation.png "Correlations")

## Model Building 

First, I transformed the categorical variables into dummy variables. I also split the data into train and tests sets with a test size of 20%.   

I tried three different models and evaluated them using Mean Absolute Error.    

I tried three different models:
*	**Support Vector Regression** 
*	**Decision Tree Regressor** 
*	**Random Forest**

## Model performance
The Random Forest model far outperformed the other approaches on the test and validation sets. 
*	**Support Vector Regression** : MAE = 33
*	**Decision Tree Regressor**: MAE = 44
*	**Random Forest**: MAE = 36

## Productionization 
Now comes the step of building a "flask" type API hosted on a local web server. This task was inspired by the TDS mentioned above. The API takes a query with a list of values from a list of jobs and returns a salary estimate. 


