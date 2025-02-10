import csv
f = open('Data/portfolio.csv')
f_csv = csv.reader(f)
headers = next(f_csv)
rows = list(f_csv)




