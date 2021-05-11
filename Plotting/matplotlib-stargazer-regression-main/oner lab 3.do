clear all

*** I preprocessed (merging, cleaning, droping NAN etc.) the data on Python. I created small csv datasets. 

*** df1.csv is the main dataset. 

*** sample1.csv is the dataset where I put all variables at their mean. Europe is dummy variable, so I leave it as it is.

*** sample10.csv is the dataset where I put keep Price level of household consumption (pl_c) at its  90th % percentaile.
*** Other variables are still at their means.

*** sample90.csv  is the dataset where I put keep Price level of household consumption (pl_c) at its  10th % percentaile.
*** Other variables are still at their means.


import delimited "/Volumes/GoogleDrive/My Drive/Semesters/BU Semesters/Spring'20/Statistics II/Labs/L3/df1.csv", encoding(ISO-8859-1)

reg protestnumber polity2 pop rgdpna emp pl_c europe

import delimited "/Volumes/GoogleDrive/My Drive/Semesters/BU Semesters/Spring'20/Statistics II/Labs/L3/sample1.csv", encoding(ISO-8859-1)clear


predict yhat1, xb

predict se1, stdp

gen lb= yhat1-(1.96*se1)

gen ub= yhat1+(1.96*se1)

twoway (rspike ub lb polity2, lpattern(dash)) (line yhat polity2, lpattern(solid) lcolor(red)),legend(off) ytitle("# of Protests (Predicted)") xtitle("Polity Score") title(Predicted # Protests across Range of Polity,lcolor(black))
graph export polity1.pdf, as(pdf) replace

*************************** 10% percentaile for hausehold 

import delimited "/Volumes/GoogleDrive/My Drive/Semesters/BU Semesters/Spring'20/Statistics II/Labs/L3/sample10.csv", encoding(ISO-8859-1)clear
predict yhat1, xb

predict se1, stdp

gen lb= yhat1-(1.96*se1)

gen ub= yhat1+(1.96*se1)

twoway (rspike ub lb polity2, lpattern(dash)) (line yhat polity2, lpattern(solid) lcolor(red)),legend(off) ytitle("# of Protests (Predicted)") xtitle("Polity Score") title(Predicted # Protests given low household consumption,lcolor(black))
graph export polity10.pdf, as(pdf) replace

**************************90% percentaile for hausehold 

import delimited "/Volumes/GoogleDrive/My Drive/Semesters/BU Semesters/Spring'20/Statistics II/Labs/L3/sample90.csv", encoding(ISO-8859-1)clear

predict yhat1, xb

predict se1, stdp

gen lb= yhat1-(1.96*se1)

gen ub= yhat1+(1.96*se1)

twoway (rspike ub lb polity2, lpattern(dash)) (line yhat polity2, lpattern(solid) lcolor(red)),legend(off) ytitle("# of Protests (Predicted)") xtitle("Polity Score") title(Predicted # Protests given high household consumption,lcolor(black))
graph export polity90.pdf, as(pdf) replace
