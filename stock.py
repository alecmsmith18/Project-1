stock_amount = int(input("Amount of Shares Bought:"))
money_for_stock = stock_amount * 40
commission1 = .03 * money_for_stock
sold_for_stock = 42.75 * stock_amount
commission2 = .03 * sold_for_stock
total_left = sold_for_stock - commission1 - commission2

print("Amount of Money Paid For Stocks")
print("---------------------------------")
print("$", format(money_for_stock, ',.2f'))
print("Amount of Commission Paid to Broker")
print("------------------------------------")
print("$", format(commission1, ',.2f'))
print("Amount of Stock Sold For")
print("--------------------------")
print("$",format(sold_for_stock, ',.2f'))
print("Commission Amount paid to Broker for Sold Stock")
print("--------------------------------------------------")
print("$",format(commission2, ',.2f'))
print("Total Left Over")
print("-----------------")
print("$",format(total_left, ',.2f'))
if total_left > money_for_stock:
    print("You Made a Profit!")
if total_left < money_for_stock:
    print("You Lost Money")
