import matplotlib.pyplot as plt
import time
import os
from dotenv import load_dotenv
import pandas as pd
load_dotenv()
address = os.getenv("FILE_ADDRESS")
deviation = "Deviation"
close = "Close"
Ema = "Exponential_Moving_Average"

def Exponential(df,position:int,smoothing:int)->float:
   if position == 0:
      return df[close].iloc[position]
   else: 
      present = df[close].iloc[position]
      yesterday = df[close].iloc[position-1] 
      smooth = smoothing/(1+position)
      value = present * smooth + yesterday * (1-smooth)
      
      return value
   
def deviations(df,position:int)->float:
   value = df[close].iloc[position] - df[Ema].iloc[position]
   return value
   
def accuracy(df):
   hits = 0
   miss = 0
   for i in range(len(df)):
      if (df[close].iloc[i] == df[Ema].iloc[i])/df[close].iloc[i] < 0.05:
         hits += 1 
      else:
         miss += 1
   hit_ratio = hits/len(df) 
   miss_ratio = miss/len(df)
   print(f"\nThe Number of Hit are : {hits}\nThe Number of Misses are : {miss}\nThe HIT-RATIO : {hit_ratio*100} %\nThe MISS-RATIO : {miss_ratio*100} %\n\n")
   
   
def main():
   cols = ["Date","Open","Close"]
   df = pd.read_csv(address,usecols = cols)
   df[Ema] = 0.00
   df[deviation] = 0.00
   
   smoothing = int(input("\n\nEnter the Smoothing Value : \n\n"))
   st1 = time.time()
   for i in range(0,len(df)):
      df.at[i,Ema] = Exponential(df,i,smoothing)
      df.at[i,deviation] = deviations(df,i)
   
   end1 = time.time()
   print(df)
   print(f"\n\nExecution Time Taken : {end1-st1:.6f} ms\n\n")
   print("\n\nThe Accuracy of the Model :\n\n")
   accuracy(df)
   plt.plot(df[close],marker = "|",color="green",label = "CLOSING PRICE" )
   plt.plot(df[Ema],marker = "o",color = "black",label="Exponential Moving Average" )
   plt.legend()
   plt.show()
   
main()