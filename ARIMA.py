import pandas as pd
import time
import os
from dotenv import load_dotenv
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller 
from statsmodels.graphics.tsaplots import plot_pacf,plot_acf
# Import this auto_arima to get best ARIMA model p,q,d values for our ARIMA model
from pmdarima import auto_arima
from statsmodels.tsa.arima.model import ARIMA
load_dotenv()
address = os.getenv("FILE_ADDRESS")
close = "Close"
Lag = 12 
ord =(1,0,0)

def stationary_check(df)->float:
   print("\n------------------------------------------------------------\n")
   test = adfuller(df[close],autolag = "AIC")
   print(f"\n\nADF VALUE  : {test[0]}\n")
   print(f"P-VALUE : {test[1]}\n")
   print(f"Number of Lags : {test[2]}\n")
   print(f"Number of Observation Taken into Account : {test[3]}\n")
   print("Critical Values : \n")
   for key,value in test[4].items():
      print(f"\t{key} :  {value}")

   return test[1]

def Accuracy(test,predictions):
   hits = 0
   miss = 0
   for i in range(len(test)):
      value = test.iloc[i] -  predictions.iloc[i]
      if value < 0:
         value *= -1
      if value/test.iloc[i] < 0.01:
         hits += 1 
      else:
         miss += 1
   
   hit_ratio = hits/len(test)*100
   miss_ratio = miss/len(test)*100
   print(f"\nThe Number of Hits are : {hits}\nThe Number of Misses are : {miss}\nThe HIT-RATIO :{hit_ratio}\nThe MISS-RATIO : {miss_ratio}\n\n")
   
def deviations(test,predictions):
   res = []
   for i in range(len(test)):
      res.append(round(test.iloc[i]-predictions.iloc[i],3))
   
   return res

def main():
   df = pd.read_csv(address,index_col="Date",parse_dates=True)
   print(df.head())
   # If there is void/null data then it is removed 
   # Basically data cleansing
   df = df.dropna()
   plt.plot(df[close],color="blue",label="Closing Price")
   plt.legend()
   plt.show()
   # Here First We will test the data if it is stationary or not ? 
   # Using the AIC test 
   Pvalue = stationary_check(df)
   if Pvalue < 0.5:
      print("\nThe Data Set is Sigificantly Stationary !\n")
   elif Pvalue == 0.5:
      print("\nThe Data Set is Stationary \n")
   else:
      print("\nThe Data Set is Significantly Not Stationary !\n")
   print("\n-----------------------------------------------------------------------------\n")
   # Here we find best fit values for ARIMA Model  
   # Parameter can be starting point (p) , ending point (q) , difference number of values (d) ,etc
   # Trace = True :  will print out each step
   # It will try different types of combinations 1 0 0 , 0 0 1, 1 1 1 ,etc 
   # For Every Combination it will assign a Score which is called as AIC.
   # The Model's Goal is to reduce the AIC
   finding = auto_arima(df[close],trace=True)
   # It also gives the Best Model reccomendation.
   print(finding.summary())
   plot_acf(df[close],lags=Lag)
   plot_pacf(df[close],lags=Lag)
   plt.show()
   
   # Now we will start with ARIMA Model 
   train,test = df[close].iloc[0:int(0.70*len(df))],df[close].iloc[int(0.71*len(df)):]
   print("\nThe Training Set is : \n")
   print(train)
   print("\nThe Testing Set is : \n")
   print(test)
   
   st1 = time.time()
   model = ARIMA(train,order=ord)
   model = model.fit()
   print("\n\nSummary of ARIMA MODEL \n\n")
   # Here we also get the coefficient for each lag
   print(model.summary())
   end1 = time.time()
   predictions = model.predict(start = len(train),end = len(train)+len(test)-1,type='levels')
   predictions.index    = df.index[len(train):len(train)+len(test)+1]
   print("\nThe Prediction Values : \n")
   print("\n\tACTUAL VALUE\tPREDICTIVE VALUES\t")
   for i in range(0,len(test)):
      print(f"\t{round(test.iloc[i],3)}\t\t\t{round(predictions.iloc[i],3)}")
   print("\n\n")
   plt.plot(predictions,marker="o",color="red",label="Predictions")
   plt.plot(test,marker="x",color="green",label="Testing")
   plt.legend()
   plt.show()
   print("\n\nThe Accuracy of the Model is : \n")
   Accuracy(test,predictions)
   res = deviations(test,predictions)
   print("\nThe Deviations are : \n")
   for _ in res:
      print(_)
   print(f"\n\nThe Time Taken by the Model is : {end1-st1:.6f} \n\n")
main()