import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
import statistics as stat

df=pd.read_stata('grade_clean.dta')


finalgrade=df['finalgrade']

def sample_mean_calculator(data, n_samples):
    sample_means=[]
    for i in range(n_samples):
        sample=finalgrade.sample(n_samples, replace=True)
        sample_mean=stat.mean(sample)
        sample_means.append(sample_mean)
    return sample_means
        

sns.set_theme(style="whitegrid")
# plt.style.use('ggplot')

fig, ax = plt.subplots(ncols=2,nrows=2,figsize=(12,8))
fig.suptitle('Central Limit Theorem Demonstration')

plt.subplots_adjust(wspace=0.5)
plt.tight_layout()

sns.distplot(ax=ax[0,0],x=sample_mean_calculator(finalgrade, 10),bins=15,color='gray')
sns.distplot(ax=ax[0,1],x=sample_mean_calculator(finalgrade, 100),bins=25,color='gray')
sns.distplot(ax=ax[1,0],x=sample_mean_calculator(finalgrade, 1000),bins=35,color='gray')
sns.distplot(ax=ax[1,1],x=sample_mean_calculator(finalgrade, 10000),bins=45,color='gray')

ax[0,0].set_xlabel('Final Grade Means with 10 Samples')
ax[0,1].set_xlabel('Final Grade Means with 100 Samples')
ax[1,0].set_xlabel('Final Grade Means with 1000 Samples')
ax[1,1].set_xlabel('Final Grade Means with 10000 Samples')


