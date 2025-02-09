import csv
from pprint import pprint

# A function that reads a file into a list of dicts
def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = {
                'name' : row[0],
                'shares' : int(row[1]),
                'price' : float(row[2])
            }
            portfolio.append(record)
    return portfolio

portfolio = read_portfolio('Data/portfolio.csv')
"""
print([s for s in portfolio if s['shares'] > 100])

print(sum([s['shares']*s['price'] for s in portfolio]))

print({ s['name'] for s in portfolio })

totals = { s['name']: 0 for s in portfolio }
for s in portfolio:
    totals[s['name']] += s['shares']

print(f"Totals: ", totals)

from collections import Counter

totals = Counter()
for s in portfolio:
    totals[s['name']] += s['shares']

print(f"Totals: ",totals)

print(totals.most_common(2))

more = Counter()

more['IBM'] = 75
more['AA'] = 200
more['ACME'] = 30
print(f"More: ", more)

print(totals + more)
"""
from collections import *
import readrides
rows = readrides.read_rides_as_dicts('Data/ctabus.csv')
print(rows[1])

route_counter = Counter(row['route'] for row in rows)

num_routes = len(route_counter)

print("Number of bus routes in Chicago:", num_routes)

by_num = defaultdict(list)
for row in rows:
    by_num[(row['route'], row['date'])].append(row['rides'])

print(by_num[('22', '02/02/2011')])
"""
total_rides = Counter()
for row in rows:
    total_rides[row['route']] += int(row['rides'])
...
# Now total_rides contains the total rides per bus route
for route, rides in total_rides.items():
    print(f"Route {route}: {rides} rides")
"""

rides2001 = Counter()
rides2011 = Counter()

# Loop over each row and accumulate rides based on the year.
for row in rows:
    # Extract the year from the date (assuming 'mm/dd/yyyy' format)
    year = row['date'].split('/')[-1]
    rides_val = int(row['rides'])
    if year == '2001':
        rides2001[row['route']] += rides_val
    elif year == '2011':
        rides2011[row['route']] += rides_val

# Compute the ten-year increase per route: rides in 2011 minus rides in 2001.
increases = {}
for route in set(rides2001) | set(rides2011):  # union of routes from both years
    increases[route] = rides2011.get(route, 0) - rides2001.get(route, 0)

# Sort the routes by increase (in descending order) and get the top five.
top5 = sorted(increases.items(), key=lambda x: x[1], reverse=True)[:5]

# Display the results.
for route, diff in top5:
    print(f"Route {route} had an increase of {diff} rides from 2001 to 2011")