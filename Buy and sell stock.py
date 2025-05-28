def Profit(prices):
    min_price = float('inf')
    max_profit = 0
    for i in prices:
        if i < min_price:
            min_price = i
        else:
            p = i - min_price
            if p > max_profit:
                max_profit = p
    return max_profit

print(Profit([5,3,8,4]))