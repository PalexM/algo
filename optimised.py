import csv
from time import perf_counter


start_time = perf_counter()

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
        f.write(" Meilleures combinations : "+str(buyed)+" \n Meilleur profit : "+str(profit)+ "\n Cout :"+str(cost))
    return cost, profit, buyed



stocks = []

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

# stocks = [
#     ("stock-1",20,0.5),
#     ("stock-2",30,1),
#     ("stock-3",50,15),
#     ("stock-4",70,20),
#     ("stock-5",60,17),
#     ("stock-6",80,25),
#     ("stock-7",22,0.7),
#     ("stock-8",26,11),
#     ("stock-9",48,13),
#     ("stock-10",34,27),
#     ("stock-11",42,17),
#     ("stock-12",110,0.9),
#     ("stock-13",38,23),
#     ("stock-14",14,0.1),
#     ("stock-15",18,0.3),
#     ("stock-16",8,0.8),
#     ("stock-17",4,12),
#     ("stock-18",10,14),
#     ("stock-19",24,21),
#     ("stock-20",114,18)
# ]

stocks = [(stock, cost, prc, (prc / 100) * cost) for stock, cost, prc in stocks if  cost > 0 and prc > 0]



optimised(stocks,500)

end_time = perf_counter()

execution_time = end_time - start_time
print(f"Temps d'execution: {execution_time} seconds.")
