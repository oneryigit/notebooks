import pandas as pd
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import seaborn as sns 
from numpy import sqrt, exp, pi


z=np.linspace(-5,5,100)
#Normal PDF
n_pdf = 1/sqrt(2*pi)*exp(-((z**2)/2))
#logistic PDF
l_pdf = exp((z-0)/1)/(1*(1+exp((z-0)/1))**2)
# with different mean and variance
n1=((1/(sqrt(2*pi)))*exp(-(z**2)/2))
n2=((1/(0.64*sqrt(2*pi)))*exp(-(z**2)/(2*0.64)))
n3=((1/(0.16*sqrt(2*pi)))*exp(-((z-2)**2)/(2*0.16)))

n4=1/(1+exp(-(z-0)/1))


import matplotlib.style as style
style.available
['Solarize_Light2',
 '_classic_test_patch',
 'bmh',
 'classic',
 'dark_background',
 'fast',
 'fivethirtyeight',
 'ggplot',
 'grayscale',
 'seaborn',
 'seaborn-bright',
 'seaborn-colorblind',
 'seaborn-dark',
 'seaborn-dark-palette',
 'seaborn-darkgrid',
 'seaborn-deep',
 'seaborn-muted',
 'seaborn-notebook',
 'seaborn-paper',
 'seaborn-pastel',
 'seaborn-poster',
 'seaborn-talk',
 'seaborn-ticks',
 'seaborn-white',
 'seaborn-whitegrid',
 'tableau-colorblind10']
style.use(style= 'seaborn-whitegrid')
fig, ax=plt.subplots(2,2, figsize=(10,8))


plt.suptitle('PDF and CDF of Standard Normal and Logistic',family='serif', size=14)


ax[0,0].plot(z, n_pdf, color='gray', lw=2, ls='-.')
ax[0,0].plot(z, l_pdf, color='gray', lw=2, ls='-')
ax[0,1].plot(z, n1,color='gray', lw=2, ls='-')
ax[0,1].plot(z, n2,color='gray', lw=2, ls='-.')
ax[0,1].plot(z, n3,color='gray', lw=2, ls=':')
ax[1,0].plot(z, n4,color='gray', lw=2, ls='-')
ax[1,0].plot(z, norm.cdf(z),color='gray', lw=2, ls='-.')
ax[1,1].set_visible(False)

ax[0,0].set_title('Figure 1: Standar Normal and Logistic PDF',
                  fontsize=12,family='serif')
ax[0,0].set_xlabel('z', 
           family='serif', 
           color='black', 
           weight='normal', 
           size = 12,
           labelpad = 6)

ax[0,0].set_ylabel('Pr(Y=1)', 
           family='serif', 
           color='black', 
           weight='normal', 
           size = 12,
           labelpad = 6)

ax[0,0].annotate('Standard Normal PDF',xy=(-1,0.28),
                 size=10, color='#404040',xytext=(-5.3,0.35),
                 arrowprops=dict(width=1, headwidth=4, headlength=3, color='#A0A0A0'))


ax[0,0].annotate('Logistic PDF',xy=(2.5,0.08),
                 size=10, color='#404040',xytext=(3,0.21),
                 arrowprops=dict(width=1, headwidth=4, headlength=3, color='#A0A0A0'))


ax[0,1].set_title('Figure 2: Different Variance and Mean (PDF)',
                  fontsize=12,family='serif')
ax[0,1].set_xlabel('z', 
           family='serif', 
           color='black', 
           weight='normal', 
           size = 12,
           labelpad = 6)

ax[0,1].set_ylabel('Pr(Y=1)', 
           family='serif', 
           color='black', 
           weight='normal', 
           size = 12,
           labelpad = 6)

ax[0,1].annotate('$\mu=0,\ \sigma^2=1$',xy=(0,0.4), size=10, xytext=(-4,1),
                 color='k',
                 arrowprops=dict(arrowstyle='simple', color='#A0A0A0'))
ax[0,1].annotate('$\mu=0,\ \sigma^2=0.64$',xy=(0,0.6), size=10, xytext=(-2,1.5),
                 arrowprops=dict(arrowstyle='simple',color='#A0A0A0'))
ax[0,1].annotate('$\mu=2,\ \sigma^2=0.16$',xy=(2.7,1), size=10, xytext=(2.5,2),
                 arrowprops=dict(arrowstyle='simple',color='#A0A0A0'))


ax[1,0].set_title('Figure 3: Standar Normal and Logistic CDF',
                  fontsize=12,family='serif')
ax[1,0].set_xlabel('z', 
           family='serif', 
           color='black', 
           weight='normal', 
           size = 12,
           labelpad = 6)

ax[1,0].set_ylabel('Pr(Y=1)', 
           family='serif', 
           color='black', 
           weight='normal', 
           size = 12,
           labelpad = 6)
ax[1,0].annotate('Standard Normal CDF',xy=(0.9,0.79), size=10, xytext=(-5,0.96),
                 color='#404040',
                 arrowprops=dict(arrowstyle='simple',color='#A0A0A0'))
ax[1,0].annotate('Logistic CDF',xy=(2,0.88), size=10, xytext=(3,0.4),
                 color='#404040',
                 arrowprops=dict(arrowstyle='simple',color='#A0A0A0'))


fig.tight_layout()
plt.savefig('Figure123.pdf')
