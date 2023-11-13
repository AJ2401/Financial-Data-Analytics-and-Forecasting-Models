# here we use order differencing 
# Stationary we should have constant mean, constant variance,No seasonality
import pandas as pd
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv
load_dotenv()
address = os.getenv("FILE_ADDRESS")

def stationary_func(df,perform = False):
   if perform :
      for i in range(1,len(df['Close'])):
         df.at[i-1,'Close'] = df.at[i,'Close'] - df.at[i-1,'Close']
      return df
   else:
      return "Exceeded the Limit !"
   
def main():
   df = pd.read_csv("/Users/abhishekjhawar/Desktop/Project/Fintech/BAJAJFINSV.NS.csv")
   plt.plot(df.index,df['Close'])
   plt.legend()
   plt.show()
   print(df['Close'].values)
   command = "Continue"
   while command == "Continue" or command == "continue" or command == "CONTINUE" or command == "yes" or command == "YES" or command == "Yes":
      df = stationary_func(df,perform=True)
      df.drop(df.index[0])
      df.drop(df.index[len(df)-1])
      plt.plot(df.index,df['Close'])
      plt.legend()
      plt.show()
      command = input("Enter your Command \n")

main()