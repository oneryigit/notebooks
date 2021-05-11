import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
# =============================================================================
# LOADING THE DATASET
# =============================================================================
#Loading the datasets
vdem=pd.read_stata('vdem1.dta')
vdem.dropna(inplace=True) #drop all the missing values.
vdem.head()

qog=pd.read_stata('qog1.dta')
qog.dropna(inplace=True)
qog['year']=qog['year'].astype('int')
qog.head()

median=pd.read_stata('medianvoter.dta')
median.dropna(inplace=True)
median.head()

med2=median[['natname', 'elecdate', 'turnout', 'elecsize']]

#Here I make elecdate variable to string type so that I can slice.
med2['elecyear']=med2.elecdate.astype('string')

#Slicing the last two digits in the variable. I take only the first four num.
med2['elecyear']=med2["elecyear"].str.slice(0,4)

#drop the previous elecdate variable.  
med2.drop('elecdate', axis=1, inplace=True)

#Making the datatype of elecyear as interval again. 
med2['elecyear']=med2['elecyear'].astype('int')

med2['turn_percent']= ((med2['turnout']/med2['elecsize'])*100)



med2=med2.pivot_table(index=['natname','elecyear'])
med2=med2.reset_index()




#merging vdem and qog datasets on both cowcode and year
vq=pd.merge(vdem, qog, how='inner',on=['cowcode','year'])
vq.isnull().sum() #to check if we succesfully drop all nulls.
vq.head()



#Final merge
finaldf=pd.merge(vq, med2, how='inner',
                 left_on=['country_x', 'year'],
                 right_on=['natname','elecyear'])
finaldf.head()
finaldf.isnull().sum()
finaldf.columns
finaldf.drop(['country_y','elecyear', 'natname','lifeex', 'popdens' ],
             axis=1, inplace=True)

finaldf.to_stata('finaldf.dta')
# =============================================================================
# REGRESSION MODEL WITH STATSMODEL
# =============================================================================
import statsmodels.api as sm


y=finaldf['turn_percent']
x1=finaldf[['oppospower',
       'sepowerdist', 'gdpcap', 'youthunemp']]

x2=finaldf[['propwomen','oppospower',
       'sepowerdist', 'gdpcap', 'youthunemp']]

x=sm.add_constant(x1)
x_withfemale=sm.add_constant(x2)

model1=sm.OLS(y,x).fit()
model2=sm.OLS(y,x_withfemale).fit()


model1.summary()
model2.summary()

# =============================================================================
# STARGAZER MODEL OUTPUTS
# =============================================================================
from stargazer.stargazer import Stargazer

stargazer=Stargazer([model1,model2])
stargazer.custom_columns(['Base Model', 'Spesified Model'], [1, 1])
stargazer.significant_digits(2)
stargazer.covariate_order(['const','propwomen','oppospower', 
                           'gdpcap', 'sepowerdist',
                           'youthunemp'])

stargazer.rename_covariates({'const': 'Constant',
                             'oppospower':'Opposition Power',
                             'gdpcap': 'GDP($)',
                             'sepowerdist':'Class Political Power',
                             'youthunemp':'Unemployed Youth %',
                             'propwomen':'Female Property Rights'})

stargazer.cov_spacing = 3
print(stargazer.render_latex())




