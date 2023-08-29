import pandas as pd
import requests

class Stock:

    def __init__(self, company, mode, key, full = True):
        self.__mode = mode
        if full:
            self.__url = "https://www.alphavantage.co/query?function="+mode+"&symbol="+company+"&interval=5min&adjusted=true&outputsize=full&apikey="+key
        else:
            self.__url = "https://www.alphavantage.co/query?function="+mode+"&symbol="+company+"&interval=5min&adjusted=true&apikey="+key

        r = requests.get(self.__url)
        self.json = r.json()
        self.meta_data = self.json["Meta Data"]

        if self.__mode == 'TIME_SERIES_INTRADAY':
            stocks_data = self.json['Time Series (5min)']
            data_time = [item for item in stocks_data]

            stocks = []
            for item in data_time:
                stock = dict(time = item,
                    open = stocks_data[item]["1. open"],
                    high = stocks_data[item]["2. high"],
                    low = stocks_data[item]["3. low"],
                    close = stocks_data[item]["4. close"],
                    volume = stocks_data[item]["5. volume"]
                )
                stocks.append(stock)

            self.df = pd.DataFrame(stocks)

            self.df.time = pd.to_datetime(self.df.time)
            self.df.open = pd.to_numeric(self.df.open)
            self.df.high = pd.to_numeric(self.df.high)
            self.df.low = pd.to_numeric(self.df.low)
            self.df.close = pd.to_numeric(self.df.close)
            self.df.volume = pd.to_numeric(self.df.volume)



        elif self.__mode == 'TIME_SERIES_DAILY':
            stocks_data = self.json['Time Series (Daily)']
            data_time = [item for item in stocks_data]

            stocks = []
            for item in data_time:
                stock = dict(time = item,
                             open = stocks_data[item]["1. open"],
                             high = stocks_data[item]["2. high"],
                             low = stocks_data[item]["3. low"],
                             close = stocks_data[item]["4. close"],
                             volume = stocks_data[item]["5. volume"]
                             )
                stocks.append(stock)

            self.df = pd.DataFrame(stocks)

            self.df.time = pd.to_datetime(self.df.time)
            self.df.open = pd.to_numeric(self.df.open)
            self.df.high = pd.to_numeric(self.df.high)
            self.df.low = pd.to_numeric(self.df.low)
            self.df.close = pd.to_numeric(self.df.close)
            self.df.volume = pd.to_numeric(self.df.volume)


        elif self.__mode == 'TIME_SERIES_WEEKLY':
            stocks_data = self.json['Weekly Time Series']
            data_time = [item for item in stocks_data]

            stocks = []
            for item in data_time:
                stock = dict(time = item,
                             open = stocks_data[item]["1. open"],
                             high = stocks_data[item]["2. high"],
                             low = stocks_data[item]["3. low"],
                             close = stocks_data[item]["4. close"],
                             volume = stocks_data[item]["5. volume"]
                             )
                stocks.append(stock)

            self.df = pd.DataFrame(stocks)

            self.df.time = pd.to_datetime(self.df.time)
            self.df.open = pd.to_numeric(self.df.open)
            self.df.high = pd.to_numeric(self.df.high)
            self.df.low = pd.to_numeric(self.df.low)
            self.df.close = pd.to_numeric(self.df.close)
            self.df.volume = pd.to_numeric(self.df.volume)


        elif self.__mode == 'TIME_SERIES_MONTHLY':
            stocks_data = self.json['Monthly Time Series']
            data_time = [item for item in stocks_data]

            stocks = []
            for item in data_time:
                stock = dict(time = item,
                             open = stocks_data[item]["1. open"],
                             high = stocks_data[item]["2. high"],
                             low = stocks_data[item]["3. low"],
                             close = stocks_data[item]["4. close"],
                             volume = stocks_data[item]["5. volume"]
                             )
                stocks.append(stock)

            self.df = pd.DataFrame(stocks)

            self.df.time = pd.to_datetime(self.df.time)
            self.df.open = pd.to_numeric(self.df.open)
            self.df.high = pd.to_numeric(self.df.high)
            self.df.low = pd.to_numeric(self.df.low)
            self.df.close = pd.to_numeric(self.df.close)
            self.df.volume = pd.to_numeric(self.df.volume)

        elif self.__mode == 'TIME_SERIES_WEEKLY_ADJUSTED':
            stocks_data = self.json['Weekly Adjusted Time Series']
            data_time = [item for item in stocks_data]

            stocks = []
            for item in data_time:
                stock = dict(time = item,
                             open = stocks_data[item]["1. open"],
                             high = stocks_data[item]["2. high"],
                             low = stocks_data[item]["3. low"],
                             close = stocks_data[item]["4. close"],
                             adjusted_close = stocks_data[item]["5. adjusted close"],
                             volume = stocks_data[item]["6. volume"],
                             divident_amount = stocks_data[item]["7. dividend amount"]
                             )
                stocks.append(stock)

            self.df = pd.DataFrame(stocks)

            self.df.time = pd.to_datetime(self.df.time)
            self.df.open = pd.to_numeric(self.df.open)
            self.df.high = pd.to_numeric(self.df.high)
            self.df.low = pd.to_numeric(self.df.low)
            self.df.close = pd.to_numeric(self.df.close)
            self.df.adjusted_close = pd.to_numeric(self.df.adjusted_close)
            self.df.divident_amount = pd.to_numeric(self.df.divident_amount)
            self.df.volume = pd.to_numeric(self.df.volume)

        elif self.__mode == 'TIME_SERIES_MONTHLY_ADJUSTED':
            stocks_data = self.json['Monthly Adjusted Time Series']
            data_time = [item for item in stocks_data]

            stocks = []
            for item in data_time:
                stock = dict(time = item,
                             open = stocks_data[item]["1. open"],
                             high = stocks_data[item]["2. high"],
                             low = stocks_data[item]["3. low"],
                             close = stocks_data[item]["4. close"],
                             adjusted_close = stocks_data[item]["5. adjusted close"],
                             volume = stocks_data[item]["6. volume"],
                             divident_amount = stocks_data[item]["7. dividend amount"]
                             )
                stocks.append(stock)



            self.df = pd.DataFrame(stocks)

            self.df.time = pd.to_datetime(self.df.time)
            self.df.open = pd.to_numeric(self.df.open)
            self.df.high = pd.to_numeric(self.df.high)
            self.df.low = pd.to_numeric(self.df.low)
            self.df.close = pd.to_numeric(self.df.close)
            self.df.adjusted_close = pd.to_numeric(self.df.adjusted_close)
            self.df.divident_amount = pd.to_numeric(self.df.divident_amount)
            self.df.volume = pd.to_numeric(self.df.volume)

#CRYPTO CRYPTO CRYPTO CRYPTO CRYPTO CRYPTO CRYPTO CRYPTO CRYPTO CRYPTO CRYPTO CRYPTO CRYPTO CRYPTO CRYPTO CRYPTO CRYPTO

class Crypto:
    def __init__(self, currency, mode, market, key):


        self.__mode = mode
        self.__currency = currency
        self.__market = market

        self.__url = "https://www.alphavantage.co/query?function="+self.__mode+"&symbol="+self.__currency+"&market="+self.__market+"&apikey="+key

        r = requests.get(self.__url)
        self.json = r.json()
        self.meta_data = self.json["Meta Data"]

        if self.__mode == 'DIGITAL_CURRENCY_WEEKLY':
            stocks_data = self.json["Time Series (Digital Currency Weekly)"]
            data_time = [item for item in stocks_data]

            stocks = []
            for item in data_time:
                stock = dict(time = item,
                             a_open = stocks_data[item][f"1a. open ({self.__market})"],
                             b_open = stocks_data[item]["1b. open (USD)"],
                             a_high = stocks_data[item][f"2a. high ({self.__market})"],
                             b_high = stocks_data[item]["2b. high (USD)"],
                             a_low = stocks_data[item][f"3a. low ({self.__market})"],
                             b_low = stocks_data[item]["3b. low (USD)"],
                             a_close = stocks_data[item][f"4a. close ({self.__market})"],
                             b_close = stocks_data[item]["4b. close (USD)"],
                             volume = stocks_data[item]["5. volume"],
                             market_cap = stocks_data[item]["6. market cap (USD)"]
                             )
                stocks.append(stock)

            self.df = pd.DataFrame(stocks)

        elif self.__mode == 'DIGITAL_CURRENCY_DAILY':
            stocks_data = self.json['Time Series (Digital Currency Daily)']
            data_time = [item for item in stocks_data]

            stocks = []
            for item in data_time:
                stock = dict(time = item,
                             a_open = stocks_data[item][f"1a. open ({self.__market})"],
                             b_open = stocks_data[item]["1b. open (USD)"],
                             a_high = stocks_data[item][f"2a. high ({self.__market})"],
                             b_high = stocks_data[item]["2b. high (USD)"],
                             a_low = stocks_data[item][f"3a. low ({self.__market})"],
                             b_low = stocks_data[item]["3b. low (USD)"],
                             a_close = stocks_data[item][f"4a. close ({self.__market})"],
                             b_close = stocks_data[item]["4b. close (USD)"],
                             volume = stocks_data[item]["5. volume"],
                             market_cap = stocks_data[item]["6. market cap (USD)"]
                             )
                stocks.append(stock)

            self.df = pd.DataFrame(stocks)

        elif self.__mode == 'DIGITAL_CURRENCY_MONTHLY':
            stocks_data = self.json['Time Series (Digital Currency Monthly)']
            data_time = [item for item in stocks_data]

            stocks = []
            for item in data_time:
                stock = dict(time = item,
                             a_open = stocks_data[item][f"1a. open ({self.__market})"],
                             b_open = stocks_data[item]["1b. open (USD)"],
                             a_high = stocks_data[item][f"2a. high ({self.__market})"],
                             b_high = stocks_data[item]["2b. high (USD)"],
                             a_low = stocks_data[item][f"3a. low ({self.__market})"],
                             b_low = stocks_data[item]["3b. low (USD)"],
                             a_close = stocks_data[item][f"4a. close ({self.__market})"],
                             b_close = stocks_data[item]["4b. close (USD)"],
                             volume = stocks_data[item]["5. volume"],
                             market_cap = stocks_data[item]["6. market cap (USD)"]
                             )
                stocks.append(stock)

            self.df = pd.DataFrame(stocks)


class Commodity:

    def __init__(self, function, interval, key):

        self.__function = function
        self.__interval = interval


        self.__url = f'https://www.alphavantage.co/query?function={function}&interval={interval}&apikey={key}'

        r = requests.get(self.__url)
        self.json = r.json()

        data = self.json['data']

        elements = []

        for item in data:
            if item["value"] != '.':
                element = dict(
                    date = item["date"],
                    value = item["value"]
                )
            else:
                break

            elements.append(element)

        self.df = pd.DataFrame(elements)

        self.df.date = pd.to_datetime(self.df.date)
        self.df.value = pd.to_numeric(self.df.value)


class EconomicIndicator:
    def __init__(self, function, interval, key):

        self.__function = function
        self.__interval = interval

        self.__url = f'https://www.alphavantage.co/query?function={function}&interval={interval}&apikey={key}'

        r = requests.get(self.__url)
        self.json = r.json()

        data = self.json['data']

        elements = []

        for item in data:
            if item["value"] != '.':
                element = dict(
                    date = item["date"],
                    value = item["value"]
                )
            else:
                break

            elements.append(element)

        self.df = pd.DataFrame(elements)
        self.df.date = pd.to_datetime(self.df.date)
        self.df.value = pd.to_numeric(self.df.value)
#%%

#%%
