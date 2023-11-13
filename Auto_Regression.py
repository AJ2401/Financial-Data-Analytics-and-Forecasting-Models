import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import os
from dotenv import load_dotenv
from statsmodels.tsa.ar_model import AutoReg
# This is imported to check the stationarity of the data 
# This is a Stationarity-Test Function
from statsmodels.tsa.stattools import adfuller
# importing acf and pacf plots 
from statsmodels.graphics.tsaplots import plot_pacf,plot_acf 
load_dotenv()
address = os.getenv("FILE_ADDRESS")
close = "Close"
lag = 2
LAG = 12


def Accuracy(predictions,test)->None:
   hits = 0
   miss = 0
   for i in range(len(predictions)-1):
      value = test.iloc[i] - predictions.iloc[i]
      if value < 0:
         value *= -1 
      if value/test.iloc[i] < 0.10:
         hits += 1
      else:
         miss += 1
   
   hit_ratio = hits/(len(predictions)-1) * 100
   miss_ratio = miss/(len(predictions)-1) * 100
   
   print(f"The Number of Hits are : {hits}\nThe Number of Misses are : {miss}\nThe HIT-RATIO is : {hit_ratio}\nThe MISS-RATIO is : {miss_ratio}\n\n")

def deviations(predictions,test)->[float]:
   deviation = []
   for i in range(len(test)):
      deviation.append(test.iloc[i]-predictions.iloc[i])
      
   return deviation

def main():
   df = pd.read_csv(address)
   print(df)   
   plt.plot(df[close],marker="o",color="green",label="Closing")
   plt.show()
   # The Series should be stationary means statistical values should be constant.( mean = ,vaiance,cyclicity = no
   # It is Dicky Fuller Test 
   # if ‘AIC’ (default) or ‘BIC’, then the number of lags is chosen to minimize the corresponding information criterion.
   # To make stationary if AIC method cannot make it.
   # Here if the P-value is greater than 0.5 then the Time Series is Not Stationary but if the P-value  < 0.5 then the time series is stationary
   StationaryTest = adfuller(df[close],autolag="AIC")
   # The adfuller function returns a tuple of statistics from the ADF test such as the Test Statistic, P-Value, Number of Lags Used, Number of Observations used for the ADF regression and a dictionary of Critical Values.
   # If the P-Value is less than the Significance Level defined, we reject the Null Hypothesis that the time series contains a unit root.
   print(f"\n\nADF Test Value : {StationaryTest[0]}\n")
   print(f"P-Value : {StationaryTest[1]}\n")
   print(f"Number of Lags : {StationaryTest[2]}\n")
   print(f"Number of Observations Used for ADF Test  : {StationaryTest[3]}\n")
   print(f"Critical Values :")
   for key,value in StationaryTest[4].items():
      print(f"\t{key} : {value}")   
   
   # Now to do Auto-Regression we plot pacf and acf to understand the correlation.
   # Gives the relationship how in different time periods.
   acf = plot_acf(df['Close'],lags = LAG)
   # Importance is pacf graph gives the direct effect of previous time lags on current time lag.
   pacf = plot_pacf(df['Close'],lags = LAG)
   plt.show()
   # Now from Pacf deciding the number of lags to take in account.
   
   # Now to divide the data into 2 parts :
   train,test = df[close].iloc[0:int(0.70*len(df))] , df[close].iloc[int(0.71*len(df)):]
   print("\nThe Training Set is : \n\n")
   print(train)
   print("\nThe Testing Data Set is :\n")
   print(test)
   # There we will be calling the Auto-regression Model 
   st1 = time.time()
   model = AutoReg(train,lags = lag).fit()
   print("\n\nModel Performance Summary \n\n")
   print(f"\n{model.summary()}\n")
   
   # Now we are predicting 
   predictions = model.predict(start = len(train),end = len(df),dynamic = False) 
   
   end1 = time.time() 
   print("\nThe Prediction Values are : \n\n")
   print(predictions)
   
   # Plotting the graph for both the predictions and testing set
   plt.plot(predictions,marker="o",color="green",label="PREDICTIONS")
   plt.plot(test,marker="x",color="blue",label="TESTING")
   plt.legend()
   plt.show()
   
   print(f"\nThe Time Taken by the Model Training and Prediction is : {end1-st1:.6f}\n")
   print("The Deviations are : \n\n")
   deviation = deviations(predictions,test)
   for _ in deviation:
      print(_)
   print("\n\nThe Accuracy of the Model is : \n\n")
   Accuracy(predictions,test)
   
main() 