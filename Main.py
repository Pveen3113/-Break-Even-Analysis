import matplotlib.pyplot as plt
from prettytable import PrettyTable
import sys

revenue = []
cost = []
avgcost = []
profit = []
qty = []


def MainMenu():
    print("1. Enter Details\n")
    print("2. Cost Calculation\n")
    print("3. Revenue Calculation\n")
    print("4. Profit Calculation\n")
    print("5. Graphs of Revenue, Cost and Profit\n")
    print("6. Graphs of Average Cost Function\n")
    print('7. Break-Even Analysis\n')
    print('8. Exit\n')


def Details(Qty):
    productname = input("Enter product name: ")
    while not productname.isalpha():
        if ' ' in productname and not any(str.isdigit(c) for c in productname):
            break
        else:
            productname = input("Re-enter product name: ")

    while True:
        try:
            fixedcost = float(input("Enter the fixed cost to set up the business: "))
            while fixedcost < 0:
                fixedcost = float(input("Re-enter the fixed cost to set up the business: "))
            break
        except ValueError:
            print("Invalid value. Try again...")

    while True:
        try:
            variablecost = float(input(f'Enter the cost of making per {productname}: '))
            while variablecost < 0:
                variablecost = float(input(f'Re-enter the cost of making per {productname}: '))
            break
        except ValueError:
            print("Invalid value. Try again...")

    while True:
        try:
            cogs = float(input(f'Enter the selling price of a {productname}: '))
            while cogs < variablecost:
                cogs = float(input(f'Re-enter the selling price of a {productname}: '))
            break
        except ValueError:
            print("Invalid value. Try again...")

    while True:
        try:
            salesvolume = int(input(f"Enter the maximum number of sales volume: "))
            while salesvolume < 0:
                salesvolume = int(input(f"Re-enter the maximum number of sales volume: "))
            break
        except ValueError:
            print("Invalid value. Try again...")
    sales = int(salesvolume / 10)
    qty = 0
    for x in range(0, 10):
        qty += sales
        Qty.append(qty)

    return productname, fixedcost, variablecost, cogs


def Calculation(Revenue, Cost, Profit, AvgCost, fcost, vcost, scost, Qty, pname):
    for x in Qty:
        cost = fcost + vcost * x
        Cost.append(cost)

    for x in Qty:
        revenue = scost * x
        Revenue.append(revenue)

    itr1 = 0
    # print(itr1)
    for x in Qty:
        profit = Revenue[itr1] - Cost[itr1]
        Profit.append(profit)
        itr1 += 1

    itr2 = 0
    # print(itr1)
    for x in Qty:
        avg = Cost[itr2] / x
        AvgCost.append(avg)
        itr2 += 1


def costGraph(Cost, pname, Qty):
    print("\n\n")
    table = PrettyTable(['Quantity', 'Cost(RM)'])
    itr = 0
    for x in Qty:
        table.add_row([Qty[itr], Cost[itr]])
        itr += 1
    print(table)
    print("\n\n")
    plt.plot(Qty, Cost, color='green', linestyle='dashed', linewidth=3, marker='o', markerfacecolor='blue',
             markersize=12)

    plt.ylabel('Price (RM) ')
    plt.xlabel(f'Quantity of {pname}')

    plt.title('Graphs of Cost')

    plt.show()


def revenueGraph(Revenue, pname, Qty):
    print("\n\n")
    table = PrettyTable(['Quantity', 'Revenue(RM)'])
    itr = 0
    for x in Qty:
        table.add_row([Qty[itr], Revenue[itr]])
        itr += 1
    print(table)
    print("\n\n")
    plt.plot(Qty, Revenue, color='yellow', linestyle='dashed', linewidth=3, marker='o', markerfacecolor='orange',
             markersize=12)

    plt.ylabel('Price (RM) ')
    plt.xlabel(f'Quantity of {pname}')

    plt.title('Graphs of Revenue')

    plt.show()


def profitGraph(Profit, Qty, pname):
    print("\n\n")
    table = PrettyTable(['Quantity', 'Profit(RM)'])
    itr = 0
    for x in Qty:
        table.add_row([Qty[itr], Profit[itr]])
        itr += 1
    print(table)
    print("\n\n")
    plt.plot(Qty, Profit, color='red', linestyle='dashed', linewidth=3, marker='o', markerfacecolor='pink',
             markersize=12)

    plt.ylabel('Price (RM) ')
    plt.xlabel(f'Quantity of {pname}')

    plt.title('Graphs of Profit')

    plt.show()


def allGraph(Cost, Revenue, Profit, Qty, pname):
    print("\n\n")
    table = PrettyTable(['Quantity', 'Revenue(RM)', 'Cost(RM)', 'Profit(RM)'])
    itr = 0
    for x in Qty:
        table.add_row([Qty[itr], Revenue[itr], Cost[itr], Profit[itr]])
        itr += 1
    print(table)
    print("\n\n")
    plt.plot(Qty, Cost, color='green', linestyle='dashed', linewidth=3, marker='o', markerfacecolor='blue',
             markersize=12, label='Cost')
    plt.plot(Qty, Revenue, color='yellow', linestyle='dashed', linewidth=3, marker='o', markerfacecolor='orange',
             markersize=12, label='Revenue')
    plt.plot(Qty, Profit, color='pink', linestyle='dashed', linewidth=3, marker='o', markerfacecolor='red',
             markersize=12, label='Profit')

    plt.ylabel('Price (RM) ')
    plt.xlabel(f'Quantity of {pname}')

    plt.title('Graphs of Revenue, Cost and Profit')
    plt.legend()
    plt.show()


def avgGraph(pname, AvgCost, scost, Qty):
    print("\n\n")
    table = PrettyTable(['Quantity', 'Average Cost(RM)'])
    itr = 0
    for x in Qty:
        table.add_row([Qty[itr], AvgCost[itr]])
        itr += 1
    print(table)
    print("\n\n")
    x = []
    for y in Qty:
        x.append(scost)

    plt.plot(Qty, AvgCost, color='darkmagenta', linestyle='dashed', linewidth=3, marker='o', markerfacecolor='orchid',
             markersize=12, label="Average Cost")
    plt.plot(Qty, x, color='crimson', linestyle='dashed', linewidth=2, label="Market Price")
    plt.ylabel('Average Cost (RM) ')
    plt.xlabel(f'Quantity of {pname}')
    plt.title('Graphs of Average Cost')
    plt.legend()
    plt.show()


def analysis(pname, fcost, vcost, scost):
    breakeven = fcost / (scost - vcost)
    print("\n\n*************************************************************************************************")
    print(f'The break-even point is: {breakeven}')
    print("*************************************************************************************************")
    print("\n\n*************************************************************************************************")
    print(f'More than {round(breakeven) + 1} {pname} need to sell in order to make profit.')
    print("*************************************************************************************************\n\n")