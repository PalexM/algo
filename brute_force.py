import itertools
import csv

def brute_force(stocks, budget):
    best_profit = 0
    best_combination = []

    # Générer toutes les combinaisons possibles d'actions
    for i in range(1, len(stocks) + 1):
            combinations = itertools.combinations(stocks, i)
            # Parcourir chaque combinaison
            for combination in combinations:
                total_cost = sum(stock[1] for stock in combination)

                # Vérifier si le coût total est inférieur ou égal au budget
                if total_cost <= budget:
                    total_profit = sum(stock[3] for action in combination)
                    # Vérifier si le profit total est supérieur au meilleur profit actuel
                    if total_profit > best_profit: 
                        best_profit = total_profit
                        best_combination = combination
                        cost = total_cost
                        print(best_profit)
    with open('combinations.txt', 'a') as f:
                f.write(" Meilleures combinations : "+str(best_combination)+" \n Meilleur profit : "+str(best_profit)+ "\n Cost :"+str(cost))
    return best_combination, best_profit, cost
 
stocks = []


with open('data1.csv', 'r') as f1:
    reader1 = csv.reader(f1)
    next(reader1)  # Sari peste header daca exista
    for row in reader1:
        stock = (row[0], float(row[1]), float(row[2]))
        stocks.append(stock)

with open('data2.csv', 'r') as f2:
    reader2 = csv.reader(f2)
    next(reader2)  # Sari peste header daca exista
    for row in reader2:
        stock = (row[0], float(row[1]), float(row[2]))
        stocks.append(stock)


stocks = [(stock, cost, prc, (profit * 100) / cost) for stock, cost, prc in stocks if  cost > 0 and prc > 0]

