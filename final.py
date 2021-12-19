import pandas as pd
import csv 
import matplotlib.pyplot as plt


df = pd.read_csv("filteredStars.csv")
df.head()
df.drop(["Unnamed: 0"],axis = 1,inplace = True)
name = df["Star_name"].to_list()
distance = df["Distance"].to_list()
Mass = df["Mass"].to_list()
Radius = df["Radius"].to_list()
Gravity = df["Gravity"].to_list()

finalDictionary = []
tempDict = {}
for i in range(0,len(name)):
    tempDict["name"] = name[i]
    tempDict["distance"] = distance[i]
    tempDict["Mass"] = Mass[i]
    tempDict["Radius"] = Radius[i]
    tempDict["Gravity"] = Gravity[i]
    finalDictionary.append(tempDict)
           
    
plt.figure(figsize=(10,5))
plt.title("Stars VS Mass")
plt.bar(name[0:9],Mass[0:9])
plt.show()
plt.figure(figsize=(10,5))
plt.title("Stars VS Radius")
plt.bar(name[0:9],Radius[0:9])
plt.show()
plt.figure(figsize=(10,5))
plt.title("Stars VS Distance")
plt.bar(name[0:9],distance[0:9])
plt.show()
plt.figure(figsize=(10,5))
plt.title("Stars VS Gravity")
plt.bar(name[0:9],Gravity[0:9])
plt.show()