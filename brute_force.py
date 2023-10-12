import itertools
import csv
from time import perf_counter


start_time = perf_counter()

def brute_force(stocks, budget):
    best_profit = 0
    best_combination = []

    # Générer toutes les combinaisons possibles d'stocks
    for i in range(1, len(stocks) + 1):
            combinations = itertools.combinations(stocks, i)
            # Parcourir chaque combinaison
            for combination in combinations:
                total_cost = sum(stock[1] for stock in combination)

                # Vérifier si le coût total est inférieur ou égal au budget
                if total_cost <= budget:
                    total_profit = sum(stock[1] * stock[2] for stock in combination)
                    # Vérifier si le profit total est supérieur au meilleur profit actuel
                    if total_profit > best_profit: 
                        best_profit = total_profit
                        best_combination = combination
                        cost = total_cost
    with open('brute_force.txt', 'a') as f:
                f.write(" Meilleures combinations : "+str(best_combination)+" \n Meilleur profit : "+str(best_profit)+ "\n Cost :"+str(cost))
    return best_combination, best_profit, cost
 
stocks = [
    ("stock-1",20,0.05),
    ("stock-2",30,0.1),
    ("stock-3",50,0.15),
    ("stock-4",70,0.2),
    ("stock-5",60,0.17),
    ("stock-6",80,0.25),
    ("stock-7",22,0.07),
    ("stock-8",26,0.11),
    ("stock-9",48,0.13),
    ("stock-10",34,0.27),
    ("stock-11",42,0.17),
    ("stock-12",110,0.09),
    ("stock-13",38,0.23),
    ("stock-14",14,0.01),
    ("stock-15",18,0.03),
    ("stock-16",8,0.08),
    ("stock-17",4,0.12),
    ("stock-18",10,0.14),
    ("stock-19",24,0.21),
    ("stock-20",114,0.18)
]

stocks = [(stock, cost, prc, (prc * 100) / cost) for stock, cost, prc in stocks if  cost > 0 and prc > 0]


brute_force(stocks,500)
end_time = perf_counter()
execution_time = end_time - start_time
print(f"Temps d'execution: {execution_time} seconds.")
