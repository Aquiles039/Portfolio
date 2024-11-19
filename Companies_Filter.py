import yfinance as yf

Stock_in_criteria = []

def less_than(stocks, price_goal):
    for stock in stocks:
        global Stock_in_criteria
        stock_price = yf.Ticker(str(stock)).info['currentPrice']
        if stock_price < price_goal:
            Stock_in_criteria.append(stock)
    return Stock_in_criteria

def more_than(stocks, price_goal):
    for stock in stocks:
        global Stock_in_criteria
        stock_price = yf.Ticker(str(stock)).info['currentPrice']
        if stock_price > price_goal:
            Stock_in_criteria.append(stock)
    return Stock_in_criteria

def between(stocks, low_price, high_price):
    for stock in stocks:
        global Stock_in_criteria
        stock_price = yf.Ticker(str(stock)).info['currentPrice']
        if (stock_price > low_price) & (stock_price< high_price):
            Stock_in_criteria.append(stock)
    return Stock_in_criteria

def in_industry(stocks, industry):
    for stock in stocks:
        global Stock_in_criteria
        try:
            company_industry = yf.Ticker(str(stock)).info['industry']
            if company_industry.upper() == industry.upper():
                Stock_in_criteria.append(stock)
        except:
            company_industry = "Null"

    return Stock_in_criteria

def comp_currency(stocks, currency):
    for stock in stocks:
        global Stock_in_criteria
        try:
            company_industry = yf.Ticker(str(stock)).info['currency']
            if company_industry.upper() == currency.upper():
                Stock_in_criteria.append(stock)
        except:
            currency = "Null"

    return Stock_in_criteria
