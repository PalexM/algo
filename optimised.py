import csv

def optimised(stocks, budget):
    sorted_stocks = sorted(stocks, key=lambda x :x[3], reverse=True)
    cost = 0
    profit = 0
    buyed = []
    for stock in sorted_stocks:
        if cost + stock[1] <= budget:
            cost += stock[1]
            profit += stock[3]
            buyed.append((stock))
    with open('optimised.txt', 'a') as f:
        f.write(" Meilleures combinations : "+str(buyed)+" \n Meilleur profit : "+str(profit)+ "\n Cost :"+str(cost))
    return cost, profit, buyed



actions = []

# Citirea primului fisier CSV
with open('data1.csv', 'r') as f1:
    reader1 = csv.reader(f1)
    next(reader1)  # Sari peste header daca exista
    for row in reader1:
        stock = (row[0], float(row[1]), float(row[2]))
        stocks.append(stock)

# Citirea celui de-al doilea fisier CSV
with open('data2.csv', 'r') as f2:
    reader2 = csv.reader(f2)
    next(reader2)  # Sari peste header daca exista
    for row in reader2:
        stock = (row[0], float(row[1]), float(row[2]))
        stocks.append(stock)

stocks = [(stock, cost, prc, (profit / 100) * cost) for stock, cost, prc in stocks if  cost > 0 and profit > 0]


optimised(stocks,500)
