import pandas as pd
import numpy as np
from sklearn.metrics import classification_report
from imblearn.over_sampling import RandomOverSampler
from sklearn.preprocessing import StandardScaler 
import matplotlib.pyplot as plt
import time
import os
from dotenv import load_dotenv
# Global variables that will be used to reduce the string ussage
close = "Close"
MA = "Moving_Average"
LogR = "Logistic_Regression"
LinR = "Linear_Regression"
display = [close,MA,LogR,LinR]

def file_processing(cols):
   # Loading the dot-env file to extract the address of the file
   load_dotenv()
   file_address = os.getenv("FILE_ADDRESS")
   print(f"\n\nFILE-ADDRESS : {file_address} \n\n")
   df = pd.read_csv(file_address)
   for i in cols:
      df[i] = None
   return df

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

# def logistic_regression():

# def scaling(df,oversampling = False):
   
# def accuracy_of_logistic_regression():
   
   
def main():
   # Add these columns in the data-frame
   cols = ["Moving_Average","Logistic_Regression","Linear_Regression"]
   df = file_processing(cols) 
   p = int(input("\nEnter the P value : \n"))
   df[MA].iloc[0] = df[close].iloc[0] 
   for i in range(1,len(df)):
      df[MA].iloc[i] = Moving_P_Avg(df,i,p)
   
   print("\n\nThe Data Set is : \n\n")
   print(df[display])
   
   

main()