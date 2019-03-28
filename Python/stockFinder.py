# the indices are the time in minues past trade open time (9:30 am)
# the values are the price in US dollars
# if a stock costs 500 at 10:30am then stock_prices[60] = 500
# stock_prices = [10, 7, 5, 8, 11, 9]
# buy at 5 sell at 11 so you make 6$


def get_max_profit(stock_prices):
	
	min_price = stock_prices[0]
	max_price = stock_prices[0]
	for j in range(len(stock_prices)):
		if min_price > stock_prices[j]:
			min_price = stock_prices[j]
	
	for i in range(len(stock_prices)):
		if max_price < stock_prices[i]:
			max_price = stock_prices[i]

	if stock_prices.index(max_price) > stock_prices.index(min_price):
		grossproduct = max_price - min_price
		return grossproduct
	else:
		print(" Stocks lost value, should have bought yesterday, max value was "+ str(max_price))


stock_prices = [10,9,8,7,6,5]

print(get_max_profit(stock_prices))