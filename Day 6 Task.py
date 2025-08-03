import csv
import pandas as pd
data={"name":["muhammad omar","mayar muhammad","ahmad muhammad","mazen murad"], "email":["momargmail.com","mm66@hotmail.org","ahmeddm77@gmacom","mazmour55@yahoo.com"]}
rows = []
for i in range(len(data["name"])):
    rows.append({"names": data["name"][i], "emails": data["email"][i]})
with open("data.csv","w",newline="")as newfile:
    writer=csv.DictWriter(newfile,fieldnames=["names","emails"])
    writer.writeheader()
    writer.writerows(data)

