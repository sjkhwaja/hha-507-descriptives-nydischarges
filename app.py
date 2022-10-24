### import packages
import pandas as pd
import numpy as np
import math
import statistics
import matplotlib.pyplot as plt
import scipy.stats
from statsmodels.formula.api import ols
import seaborn
import researchpy as rp
from tableone import TableOne, load_dataset
### pull data
data = pd.read_csv('https://health.data.ny.gov/resource/gnzp-ekau.csv')
### about data 
data.shape
data.columns
data.dtypes
### mean, var, and descriptives
data['length_of_stay'].mean()
data['length_of_stay'].var()
rp.summary_cont(data['length_of_stay'])
### counts + pie chart
race_counts = data['race'].value_counts()
race_counts
piechart_race = race_counts.plot(kind='pie')

gender_counts = data['gender'].value_counts()
gender_counts
piechart_gender = gender_counts.plot(kind='pie')

agegroup_counts = data['age_group'].value_counts()
agegroup_counts
 
### TableOne 
df = data.copy()
df.dtypes
list(df)

df_columns = ['hospital_county', 'age_group', 'gender', 'race', 'ethnicity', 'length_of_stay', 'type_of_admission', 'ccs_diagnosis_description']
df_cat = ['age_group', 'gender', 'race', 'ethnicity', 'hospital_county', 'type_of_admission', 'ccs_diagnosis_description']
df_groupby = ['race']

df_tableone = TableOne(df, columns=df_columns, categorical=df_cat, groupby=df_groupby, pval=False)
print(df_tableone.tabulate(tablefmt="fancy_grid"))