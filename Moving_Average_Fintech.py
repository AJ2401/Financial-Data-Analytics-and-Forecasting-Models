import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
from dotenv import load_dotenv
import time
load_dotenv()
address = os.getenv("FILE_ADDRESS")
close = "Close"
MA = "Moving_Avg"
MAP = "MA(P)" 
Devi = "Deviation_Percentage"

def Moving_Avg(df,position:int)->float:
   sum = 0
   for i in range(position):
      sum += df[close].iloc[i]
   average = sum/(position)
   return round(average,3)

def Moving_P_Avg(df,position:int,p:int)->float:
   sum = 0.00
   if position > p:
      for i in range(position-p,position):
         sum += df[close].iloc[i] 
      return round(sum,3)
   else:
      return Moving_Avg(df,position)
   
def difference(df,position:int)->float:
   per = df[close].iloc[position] - df[MA].iloc[position]
   per /= df[close].iloc[position]
   
   return per*100

def accuracy(df)->None:
   hits = 0
   miss = 0
   for i in range(0,len(df)):
      if (df[close].iloc[i] - df[MA].iloc[i])/df[close].iloc[i] < 0.10:
         hits += 1
      else:
         miss += 1
   hit_ratio = hits/len(df)
   miss_ratio = miss/len(df)
   print(f"The Number of Hits are : {hits}\nThe Number of Misses are : {miss}\nThe HIT-RATIO is : {hit_ratio * 100} %\nThe MISS-RATIO is : {miss_ratio * 100} %\n\n")
   
   
def main():
   cols = ["Date","Open","Close"]
   df = pd.read_csv(address,usecols=cols)
   df[MA] = 0.000
   df[Devi] = 0.00
   df[MAP] = 0.00
   
   st = time.time()
   p = int(input("Enter the P value :\n"))
   for i in range(1,len(df)):
      df.at[i,MA] = Moving_Avg(df,i)
      df.at[i,Devi] = difference(df,i)
      df.at[i,MAP] = Moving_P_Avg(df,i,p)
   end = time.time()
   print(df)
   print(f"\n\nTIME TAKEN FOR THE WHOLE PROCESS IS : {end-st:.6f} ms\n\n")
   print("\n\n\nThe Accuracy of the Moving Average is : \n\n\n")
   accuracy(df)
   
   plt.plot(df[close],marker="x",label="CLOSE")
   plt.plot(df[MA],marker="o",label="MOVING_AVG")
   plt.plot(df[MAP],marker="|",label="MA(P)")
   plt.legend()
   plt.show()
   
main()