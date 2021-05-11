# =============================================================================
# Import Some Packages
# =============================================================================

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.style as style

import seaborn as sns
import statsmodels.api as sm

# =============================================================================
# Loading the datasets
# =============================================================================
murder=pd.read_stata('statemurder.dta')

y=murder['murder'] #dependent var
x=murder[['unemp', 'hsdip', 'prcapinc', 'police', 'south',
       'deathst']] #independent vars
# =============================================================================
# OLS and Predictions
# =============================================================================
model=sm.OLS(y,x).fit()
model.summary()

y_hat=model.predict() #y_hat values.

resid=model.resid #y-y_hat residuals

y=pd.DataFrame(y)
y.rename(columns={'murder':'y'}, inplace=True)

y_hat=pd.DataFrame(y_hat)
y_hat.rename(columns={0:'y_hat'},inplace=True)

resid=pd.DataFrame(resid)
resid.rename(columns={0:'resid'},inplace=True)

# =============================================================================
# Adding yhat and residuals into the original dataset for plotting.
# =============================================================================
true_vs_pred=pd.concat([y,y_hat,resid], axis=1)

finaldf=pd.concat([murder, true_vs_pred], axis=1) 


# =============================================================================
# Lets Plot!
# =============================================================================
#import matplotlib.style as style
#style.available #to see styles
#style.use('seaborn-darkgrid')
sns.set_theme(style="whitegrid")



fig,ax=plt.subplots(nrows=2,ncols=2, figsize=(8,8))
plt.suptitle('Part I—Model Specification')
sns.scatterplot(x='y',y='y_hat',data=finaldf,color='gray', ax=ax[0,0])
sns.residplot(data=finaldf, x='y_hat', y='resid',color='gray', ax=ax[0,1])
sns.residplot(data=finaldf, x='unemp', y='resid',color='gray', ax=ax[1,0])

ax[0,0].set_xlabel('Murder Rate (True Values)', 
           family='serif', 
           color='black', 
           weight='normal', 
           size = 9,
           labelpad = 10)

ax[0,0].set_ylabel('Murder Rate (Predicted Values)', 
           family='serif', 
           color='black', 
           weight='normal', 
           size = 9,
           labelpad = 6)

ax[0,0].title.set_text('Figure 1: True vs Predicted Values')

ax[0,1].set_xlabel('Murder Rate (Predicted Values)', 
           family='serif', 
           color='black', 
           weight='normal', 
           size = 9,
           labelpad = 10)

ax[0,1].set_ylabel('Residuals', 
           family='serif', 
           color='black', 
           weight='normal', 
           size = 9,
           labelpad = 6)

ax[0,1].title.set_text('Figure 2: Residuals vs Predicted Values')


ax[1,0].set_xlabel('Unemployment Rate', 
           family='serif', 
           color='black', 
           weight='normal', 
           size = 9,
           labelpad = 10)

ax[1,0].set_ylabel('Residuals', 
           family='serif', 
           color='black', 
           weight='normal', 
           size = 9,
           labelpad = 6)

ax[1,0].title.set_text('Figure 3: Residuals vs Unemployment Rate')

ax[1,1].set_visible(False)
plt.tight_layout()
plt.savefig('Figure123.pdf')


# =============================================================================
# Heteroscedasticity test
# =============================================================================
from statsmodels.compat import lzip

#perform Bresuch-Pagan test
names = ['Lagrange multiplier statistic', 'p-value',
        'f-value', 'f p-value']
test = sm.stats.het_breuschpagan(model.resid, model.model.exog)

lzip(names, test)

format(float('4.989371962556134e-05'),'.5f')

#We reject the null hypothesis, which is the model is Homoscedastic.
#However we found that p-values is p<0.05,
#so model has hateroscadasticity issue, and it is not Homoscedastic.


# =============================================================================
# Part II—Out of Sample Plots
# =============================================================================


# =============================================================================
# Load Protest dataset
# =============================================================================
mm=pd.read_stata('mm.dta')
mm1=mm[['country', 'ccode', 'year','protestnumber','demand_price']]
mm_y_c=mm1.groupby(by=['ccode','year'])['protestnumber', 'demand_price'].count()                                                                                                                                             
mm_y_c.reset_index(inplace=True)
mm_y_c.drop(columns='demand_price', inplace=True)
mm_y_c.isnull().sum()
# =============================================================================
# Load Polity
# =============================================================================
polity16=pd.read_stata('polity2016.dta')
pol=polity16[(polity16['year']>1989)&(polity16['year']<2015)]
polity_small=pol[['ccode', 'year','polity2']]
polity_small.reset_index(inplace=True)
polity_small.drop(columns='index',inplace=True)

# =============================================================================
# Mergeing Protest and Polity
# =============================================================================

merge1=pd.merge(polity_small, mm_y_c,
         left_on=['ccode','year'],
         right_on=['ccode','year'])

merge1.shape
merge1.isnull().sum()
merge1.dropna(inplace=True)



# =============================================================================
# Merging a new data called PWT to our merged dataset (polity+protest) 
# =============================================================================
pwt=pd.read_stata('PWT.dta')

pwt['ccode']=pwt['ccode'].astype('int')

pwt_small=pwt[['sname', 'ccode',
     'year', 'pop','rgdpna', 'emp','pl_c',
     'pl_i', 'pl_g','pl_x', 'pl_m', 'pl_k','csh_c',
       'csh_i', 'csh_g', 'csh_x', 'csh_m', 'csh_r']]

pwt_small.isnull().sum()


merge2=pd.merge(merge1, pwt_small, left_on=['ccode','year'],
                right_on=['ccode','year'])
merge2.shape
merge2.isnull().sum()

# =============================================================================
# transform "region" variable, the region is event-year.
# I need country-year 'region' variable.
# =============================================================================
mm.columns
aaa=mm[['ccode','year','country', 'region']]

bbb=aaa.drop_duplicates()
# =============================================================================
# Last merge! I promise. I add 'region' into our dataset.
# =============================================================================

merge3=pd.merge(merge2, bbb,left_on=['ccode','year'],
                right_on=['ccode','year'])

merge3.columns
merge3=merge3[['ccode', 'country', 'region','year', 'polity2', 'protestnumber', 'pop', 'rgdpna',
       'emp', 'pl_c', 'pl_i', 'pl_g', 'pl_x', 'pl_m', 'pl_k', 'csh_c', 'csh_i',
       'csh_g', 'csh_x', 'csh_m', 'csh_r']]

merge3.to_csv('finaldf_l3.csv')
merge3.shape
merge3.isnull().sum()
# =============================================================================

merge3.info()

merge3.groupby('region') ['protestnumber'].count()
dummies=pd.get_dummies(merge3['region'])

df=pd.concat([merge3, dummies],axis=1)
df.columns

df=df.set_index(['ccode','year'])


# =============================================================================
# 
# # Panel OLS (optional, country-year data is panel data)
# from linearmodels import PanelOLS
# 
#y=df['protestnumber']
#exog_vars=df[['polity2','pop','rgdpna','emp','pl_c','Europe']]
#
# x=sm.add_constant(exog_vars)
# mod=PanelOLS(y,x, entity_effects=True)
# fe_res=mod.fit()
# print(fe_res)
# 
# 
# =============================================================================

# =============================================================================
# Simple OLS (for the purpose of this exercise)
# =============================================================================
df1=df[['protestnumber','polity2','pop','rgdpna','emp','pl_c','Europe']]

df1.shape
y=df1['protestnumber']
x1=df1[['polity2','pop','rgdpna','emp','pl_c','Europe']]

x=sm.add_constant(x1)
mod=sm.OLS(y,x)
results=mod.fit()
results.summary()
# =============================================================================
# stargazer, making nice LATEX output.
# =============================================================================
from stargazer.stargazer import Stargazer

stargazer=Stargazer([results])
stargazer.custom_columns('Model I')
stargazer.significant_digits(3)

stargazer.covariate_order(['polity2','pop','rgdpna','emp',
                           'pl_c','Europe','const'])


stargazer.rename_covariates({'polity2':'Polity Score',
                             'pop':'Population (Million)',
                             'rgdpna':'GDP',
                             'emp':'# of Employed',
                             'pl_c':'Household Consumption',
                             'Europe':'Europe (dummy)',
                             'const':'Constant'})

stargazer.cov_spacing = 3
print(stargazer.render_latex())

# =============================================================================
# PART II
# =============================================================================



# =============================================================================
# Out of samle, Original Dataset with variables of interest only. 
# =============================================================================

df1['pop_mean']=np.mean(df1['pop'])
df1['rgdp_mean']=np.mean(df1['rgdpna'])
df1['eu']= 1

df1['emp_mean']=np.mean(df['emp'])
df1.columns

df1.to_csv('df1.csv')

# =============================================================================
# Create a sample where all variables at their mean.
# To see polity score effect on number of protests
# =============================================================================
x1=np.linspace(-10,10,100,dtype='int')
sample=pd.DataFrame(x1)
sample=sample.rename({0:'polity2'}, axis=1)

a=df1['protestnumber'].sample(100)

a=pd.DataFrame(a)
a=a.reset_index()
a=a.drop(columns=['ccode','year'], axis=1)

sample['pop']=np.mean(df1['pop'])
sample['rgdpna']=np.mean(df1['rgdpna'])
sample['europe']=1
sample['emp']=np.mean(df1['emp'])
sample['pl_c']=np.mean(df1['pl_c'])
sample['protestnumber']=a

sample.to_csv('sample1.csv')


# =============================================================================
# Household Consumption at its 10th % percentile.
# Rest of the other variables are at their mean.
# =============================================================================

x1=np.linspace(-10,10,100,dtype='int')
sample10=pd.DataFrame(x1)
sample10=sample.rename({0:'polity_x1'}, axis=1)

a=df1['protestnumber'].sample(100)

a=pd.DataFrame(a)
a=a.reset_index()
a=a.drop(columns=['ccode','year'], axis=1)

sample10['pop']=np.mean(df1['pop'])
sample10['rgdpna']=np.mean(df1['rgdpna'])
sample10['Europe']=1
sample10['emp']=np.mean(df1['emp'])
sample10['pl_c']=np.percentile(df1['pl_c'],10)
sample10['protestnumber']=a

sample10.drop(columns=['pop_','rgdp_mean','eu','plc_mean'],inplace=True)

sample10.to_csv('sample10.csv')

# =============================================================================
# Household Consumption at its 90th % percentile.
# Rest of the other variables are at their mean.
# =============================================================================

x1=np.linspace(-10,10,100,dtype='int')
sample90=pd.DataFrame(x1)
sample90=sample.rename({0:'polity_x1'}, axis=1)

a=df1['protestnumber'].sample(100)

a=pd.DataFrame(a)
a=a.reset_index()
a=a.drop(columns=['ccode','year'], axis=1)

sample90['pop']=np.mean(df1['pop'])
sample90['rgdpna']=np.mean(df1['rgdpna'])
sample90['Europe']=1
sample90['emp']=np.mean(df1['emp'])
sample90['pl_c']=np.percentile(df1['pl_c'],90)
sample90['protestnumber']=a

sample90.drop(columns=['pop_','rgdp_mean','eu','plc_mean'],inplace=True)

sample90.to_csv('sample90.csv')

