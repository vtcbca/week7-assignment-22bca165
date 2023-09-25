import csv

import pandas as pd

 data = [
     ["P1", "orange", 2500, 5400, 3300, 1900, 1000, 4100],
     ["P2","apple", 1900, 1800, 1000, 2300, 1500, 5000],
     ["P3", "banana", 1800, 1500, 4000, 2600, 1500, 2500],
     ["P4", "fig", 1700, 4600, 1800, 2000, 1100, 2700],
     ["P5", "guava", 2900, 1800, 1400, 1800, 1000, 2500],
 ]

with open("product.csv","w", newline="") as file:
     w = csv.writer(file)
     w.writerow(["Prod_No", "Prod_Name", "Jan", "Feb", "Mar", "Apr", "May", "Jun"])
     w.writerows(data)

l = []

#1. Add 12 Records. Take input from user.

for i in range(12):
    prod_no = input("Enter Product Number: ")
    prod_name = input("Enter Product Name: ")
    jan = int(input("Enter January Sales: "))
    feb = int(input("Enter February Sales: "))
    mar = int(input("Enter March Sales: "))
    apr = int(input("Enter April Sales: "))
    may = int(input("Enter May Sales: "))
    jun = int(input("Enter June Sales: "))
    t = [prod_no, prod_name, jan, feb, mar, apr, may, jun]
    l.append(t)

with open("product.csv","a", newline="") as file:
     w = csv.writer(file)
     w.writerows(l)

#2. Create dataframe.

df = pd.read_csv("product.csv")

#3. Change Column Name Product No, Product Name, January, February, March, April, May, June.

df.columns = ["Product No", "Product Name", "January", "February", "March", "April", "May", "June"]

#4. Add column "Total Sell" to count total of all month and "Average Sell"

df["Total Sell"] = df.iloc[:, 2:].sum(axis=1)
df["Average Sell"] = df.iloc[:, 2:8].mean(axis=1)

df.to_csv("final_roduct.csv")

#5. Add 2 row at the end.

df = df.append({"Product No": "P18", "Product Name": "blackberry", "January": 500, "February": 400, "March": 700,
                "April": 800, "May": 900, "June": 1000, "Total Sell": 4300, "Average Sell": 716.67}, ignore_index=True)
df = df.append({"Product No": "P19", "Product Name": "tomato", "January": 300, "February": 1800, "March": 2000,
                "April": 1000, "May": 1700, "June": 1400, "Total Sell": 8200, "Average Sell": 1366.67}, ignore_index=True)

#6. Add 2 row after 3rd row.

r3 = pd.Series(["P20", "strawberry", 550, 760, 700, 980, 1000, 1200, 6500, 550],
                 index=["Product No", "Product Name", "January", "February", "March", "April", "May", "June",
                        "Total Sell", "Average Sell"])
df = pd.concat([df.iloc[:3], r3, df.iloc[3:]]).reset_index(drop=True)

#7. Print first 5 row.

print(df.head())

#8. Print Last 5 row.

print(df.tail())

#9. Print row 6 to 10.

print(df.iloc[5:10])

#10. Print only product name.

print(df["Product Name"])

#11. Print sell of January month with product id and product name.

print(df[["Product No", "Product Name", "January"]])

#12. Print only those product id , product name where january sell is > 5000 and February sell is >8000

print(df[(df["January"] > 5000) & (df["February"] > 8000)][["Product No", "Product Name"]])

#13. Print record in sorting order of Product name.

print(df.sort_values("Product Name"))

## 14. Display only odd index number column records

print(df.iloc[:, 1::2])

#15. Display alternate row.

print(df.iloc[1::2,])


