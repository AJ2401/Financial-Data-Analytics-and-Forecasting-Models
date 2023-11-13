import time
import pandas as pd
import os
from dotenv import load_dotenv
import matplotlib.pyplot as plt
load_dotenv()
address = os.getenv("FILE_ADDRESS")
close = "Close"
Wma = "Weighted_Moving_Avg"
deviations = "Deviations"
vol = "Volume"

def weights(position,index)->float:
   if position == 0:
      return 0.1
   return round(position/index,4)

def WMA(df,position:int)->float:
   if position == 0:
      return round(df[close].iloc[position],3)
   else:
      sum = 0.00
      total_weight = 0.00
      for i in range(position,-1,-1):
         total_weight += weights(i,position)
         sum += df[close].iloc[i] * weights(i,position)
      return round(sum/total_weight,3)
   
def Deviation(df,position:int)->float:
   return round(df[close].iloc[position] - df[Wma].iloc[position],3) 

def Accuracy(df)->None:
   hits = 0
   miss = 0 
   for i in range(len(df)):
      if (df[close].iloc[i] - df[Wma].iloc[i])/df[close].iloc[i] < 0.01:
         hits += 1
      else:
         miss += 1
   
   hit_ratio = hits/len(df)
   miss_ratio = miss/len(df)
   
   print(f"\nThe Number of hits are : {hits}\nThe Number of Misses are : {miss}\nThe HIT-RATIO is : {hit_ratio*100} %\nThe MISS-RATIO is : {miss_ratio*100} %\n\n")
   return
         
def main():
   cols = ["Date","Open","Close"]
   df = pd.read_csv(address,usecols = cols)
   df[Wma] = 0.00
   df[deviations] = 0.00
   
   st = time.time()
   for i in range(0,len(df)):
      df.at[i,Wma] = WMA(df,i)
      df[deviations].iloc[i] = Deviation(df,i)
   end1 = time.time()
   print(df)
   print(f"\n\nThe Time Taken for the Analysis is : {end1-st:.6f} ms\n\n")
   print("Accuracy of the Model is : \n")
   Accuracy(df)
   
   plt.plot(df[close],marker = "o" ,color="green",label="CLOSING")
   plt.plot(df[Wma],marker="x",color="black",label="EMA")
   plt.legend()
   plt.show()
   
main()



