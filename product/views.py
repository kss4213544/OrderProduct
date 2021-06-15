import csv
r=open('C:/Users/1234/OneDrive/바탕 화면/BI팀플/product.csv',encoding='cp949')
data=csv.reader(r)
for rr in data :
    print(rr)

