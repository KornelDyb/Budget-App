import requests
import pandas as pd

# API = 
# response = response.get
df = pd.read_csv("budget_app/data.csv")
print(sum(df[df["operation"]=="Income"]["amount"]) - sum(df[df["operation"]=="Expenses"]["amount"]))